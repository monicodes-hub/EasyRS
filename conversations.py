import pandas as pd
from fpdf import FPDF
import os
import re

# Set fixed width for each column as specified
max_col_widths = {
    "CHANNEL": 20,
    "FROM": 20,
    "FROM_NAME": 25,
    "TO_NAME": 25,
    "DATE": 30,
    "MESSAGE": 90,
    "CONN_ID": 15,
    "CUSTOMER_ID": 23,
    "CUSTOMER_PHONE": 30,    
    # Add other columns as needed
}

def create_pdf_from_dataframe(dataframe, output_filename_base, agent_name, chatids, output_dir):
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=True, margin=15)

    # Title and global subtitle
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    title_text = f"Conversaciones - AGENTE: {agent_name}"
    pdf.cell(0, 10, title_text.encode('latin-1', 'replace').decode('latin-1'), 0, 1, 'C')
    pdf.ln(2)

    pdf.set_font("Arial", '', 11)
    count = len(dataframe)
    subtitle = f"Se encontraron {count} registros para AGENTE: {agent_name}"
    pdf.cell(0, 8, subtitle.encode('latin-1', 'replace').decode('latin-1'), 0, 1, 'C')

    # Count yellow-highlighted conversations
    highlighted_count = 0
    for chatid in chatids:
        chat_df = dataframe[dataframe["CONN_ID"].astype(str) == chatid]
        if not chat_df.empty and "TO_NAME" in chat_df.columns:
            last_idx = chat_df.index[-1]
            if str(chat_df.loc[last_idx, "TO_NAME"]).strip() == agent_name:
                highlighted_count += 1

    pdf.set_font("Arial", 'B', 11)
    highlighted_subtitle = f"Conversaciones pendientes de contestar por el agente (en amarillo): {highlighted_count}"
    pdf.cell(0, 8, highlighted_subtitle.encode('latin-1', 'replace').decode('latin-1'), 0, 1, 'C')
    pdf.ln(2)
    pdf.set_font("Arial", '', 7)

    dataframe = dataframe.fillna("")
    df_str = dataframe.astype(str)
    headers = df_str.columns
    col_widths = [max_col_widths.get(col, 30) for col in headers]
    cell_height = 6

    for chatid in chatids:
        chat_df = df_str[df_str["CONN_ID"].astype(str) == chatid]
        if chat_df.empty:
            continue

        pdf.add_page()
        pdf.set_font("Arial", 'B', 12)
        subtitle_chat = f"CHATID: {chatid} - Registros: {len(chat_df)}"
        pdf.cell(0, 8, subtitle_chat.encode('latin-1', 'replace').decode('latin-1'), 0, 1, 'C')
        pdf.ln(1)

        pdf.set_font("Arial", 'B', 8)
        for i, header in enumerate(headers):
            clean_header = header.encode('latin-1', 'replace').decode('latin-1')
            pdf.cell(col_widths[i], 7, clean_header, 1, 0, 'L')
        pdf.ln()

        last_idx = chat_df.index[-1]
        highlight_row = False
        if "TO_NAME" in chat_df.columns:
            if chat_df.loc[last_idx, "TO_NAME"].strip() == agent_name:
                highlight_row = last_idx

        pdf.set_font("Arial", '', 7)
        for idx, row in chat_df.iterrows():
            cell_lines = []
            cell_texts = []
            for i, data_item in enumerate(row):
                clean_data = str(data_item).encode('latin-1', 'replace').decode('latin-1')
                lines = pdf.multi_cell(col_widths[i], cell_height, clean_data, 0, 'L', split_only=True)
                cell_lines.append(len(lines))
                cell_texts.append(lines)
            max_lines = max(cell_lines)
            row_height = cell_height * max_lines

            if pdf.get_y() + row_height > (pdf.h - pdf.b_margin):
                pdf.add_page()
                pdf.set_font("Arial", 'B', 8)
                for i, header in enumerate(headers):
                    clean_header = header.encode('latin-1', 'replace').decode('latin-1')
                    pdf.cell(col_widths[i], 7, clean_header, 1, 0, 'L')
                pdf.ln()
                pdf.set_font("Arial", '', 7)

            y_before = pdf.get_y()
            x_before = pdf.get_x()

            if idx == highlight_row:
                pdf.set_fill_color(255, 255, 0)  # Yellow
                fill = True
            else:
                fill = False

            for i, lines in enumerate(cell_texts):
                pdf.set_xy(x_before, y_before)
                pdf.rect(x_before, y_before, col_widths[i], row_height)
                cell_content = "\n".join(lines + [''] * (max_lines - len(lines)))
                pdf.multi_cell(col_widths[i], cell_height, cell_content, 0, 'L', fill=fill)
                x_before += col_widths[i]
            pdf.set_y(y_before + row_height)

            if fill:
                pdf.set_fill_color(255, 255, 255)

    safe_agent = "".join(c if c.isalnum() else "_" for c in str(agent_name))
    pdf_filename = os.path.join(output_dir, f"{output_filename_base}_AGENTE_{safe_agent}.pdf")
    try:
        pdf.output(pdf_filename, "F")
        print(f"PDF generado con éxito: {pdf_filename}")
        return pdf_filename
    except Exception as e:
        print(f"Error al guardar el PDF {pdf_filename}: {e}")
        return None

def main(file_path=None, agent_name=None, conv_mode=None):
    print("--- Exportar conversación por AGENTE y CHATID ---")
    # 1. Get file_path
    if file_path is None:
        file_path = input("Introduce la ruta completa de tu archivo Excel o HTML (.xls, .xlsx, .html): ")
    if not os.path.exists(file_path):
        print(f"Error: El archivo '{file_path}' no se encontró.")
        return

    # 2. Load DataFrame
    if file_path.lower().endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file_path)
    elif file_path.lower().endswith('.html'):
        dfs = pd.read_html(file_path)
        if not dfs:
            print("No se encontraron tablas en el archivo HTML.")
            return
        df = dfs[0]
    else:
        print("Formato de archivo no soportado. Usa .xls, .xlsx o .html")
        return

    # 3. Extract agent names
    agent_pattern = re.compile(r"AGENT:\s*([^,]+)")
    agent_names = set()
    for val in df["CHANNEL"].astype(str):
        for match in agent_pattern.findall(val):
            agent_names.add(match.strip())
    agent_names = sorted(agent_names)

    if not agent_names:
        print("No se encontraron agentes en la columna CHANNEL.")
        return

    # 4. Get agent_name
    if agent_name is None:
        print("Agentes encontrados:")
        for idx, name in enumerate(agent_names, 1):
            print(f"{idx}. {name}")
        while True:
            try:
                agent_idx = int(input("Selecciona el número del AGENTE: "))
                if 1 <= agent_idx <= len(agent_names):
                    agent_name = agent_names[agent_idx - 1]
                    break
                else:
                    print("Número fuera de rango. Intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Ingresa un número.")
    elif agent_name not in agent_names:
        print(f"El agente '{agent_name}' no está en la lista de agentes encontrados.")
        return

    print(f"Has seleccionado el agente: {agent_name}")

    # 5. Find all rows where CHANNEL contains AGENT: agent_name
    agent_mask = df["CHANNEL"].astype(str).str.contains(
        rf"AGENT:\s*{re.escape(agent_name)}\s*(,|$)", regex=True
    )
    agent_rows = df[agent_mask]

    if agent_rows.empty:
        print(f"No se encontraron registros para AGENTE: {agent_name}")
        return

    # 6. For each such row, find the nearest preceding CHATID
    chatids = set()
    channel_list = df["CHANNEL"].astype(str).tolist()
    for idx in agent_rows.index:
        for i in range(idx, -1, -1):
            match = re.search(r"CHATID:\s*([^,]+)", channel_list[i])
            if match:
                chatids.add(match.group(1).strip())
                break

    if not chatids:
        print("No se encontraron CHATID relacionados con el agente.")
        return

    # 7. Count how many CHATIDs end with TO_NAME == agent_name (console info)
    highlighted_count = 0
    for chatid in chatids:
        chat_df = df[df["CONN_ID"].astype(str) == chatid]
        if not chat_df.empty and "TO_NAME" in chat_df.columns:
            last_idx = chat_df.index[-1]
            if str(chat_df.loc[last_idx, "TO_NAME"]).strip() == agent_name:
                highlighted_count += 1
    print(f"Número de CHATIDs donde el último registro es de {agent_name}: {highlighted_count}")

    # 8. Get conv_mode
    if conv_mode is None:
        print("\n¿Deseas exportar:")
        print("1. Todas las conversaciones del agente seleccionado")
        print("2. Solo las conversaciones donde el último mensaje (TO_NAME) corresponde al agente (resaltadas en amarillo)")
        while True:
            conv_mode = input("Elige 1 o 2: ").strip()
            if conv_mode in ("1", "2"):
                break
            print("Opción inválida. Elige 1 o 2.")

    if conv_mode == "2":
        filtered_chatids = set()
        for chatid in chatids:
            chat_df = df[df["CONN_ID"].astype(str) == chatid]
            if not chat_df.empty and "TO_NAME" in chat_df.columns:
                last_idx = chat_df.index[-1]
                if str(chat_df.loc[last_idx, "TO_NAME"]).strip() == agent_name:
                    filtered_chatids.add(chatid)
        chatids = filtered_chatids

    if not chatids:
        print("No se encontraron CHATID que cumplan el criterio seleccionado.")
        return

    output_pdf_dir = "chats_filtrados_pdf"
    if not os.path.exists(output_pdf_dir):
        os.makedirs(output_pdf_dir)

    all_conv_df = df[df["CONN_ID"].astype(str).isin(chatids)]
    print(f"Exportando conversaciones para {len(chatids)} CHATID(s), total filas: {len(all_conv_df)}")
    if not all_conv_df.empty:
        create_pdf_from_dataframe(all_conv_df, "conversacion", agent_name, chatids, output_pdf_dir)
    else:
        print("No se encontraron filas para los CHATID seleccionados.")

if __name__ == "__main__":
    main()