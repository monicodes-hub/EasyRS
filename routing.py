# -*- coding: utf-8 -*-
import pandas as pd
from fpdf import FPDF
import os # Para manejo de rutas y directorios

def create_pdf_from_dataframe(dataframe, output_filename_base, rp_id_value, output_dir):
    """
    Crea un archivo PDF a partir de un DataFrame de Pandas.
    El PDF se guarda en formato A4 horizontal.
    Incluye manejo básico de ancho de columnas, saltos de página y caracteres especiales.
    """
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", 'B', 16)
    title_text = f"Reporte Filtrado - RP_ID: {rp_id_value}"
    pdf.cell(0, 10, title_text.encode('latin-1', 'replace').decode('latin-1'), 0, 1, 'C')
    pdf.ln(2)

    # Subtitle with entries info
    pdf.set_font("Arial", '', 11)
    count = len(dataframe)
    subtitle = f"Se encontraron {count} registros para RP_ID: {rp_id_value}"
    pdf.cell(0, 8, subtitle.encode('latin-1', 'replace').decode('latin-1'), 0, 1, 'C')
    pdf.ln(2)

    pdf.set_font("Arial", size=7)

    df_str = dataframe.astype(str)
    headers = df_str.columns

    available_width = pdf.w - 2 * pdf.l_margin

    # Set fixed width for each column as specified
    max_col_widths = {
        "CUSTOMER_QUERY": 110,
        "CUSTOMER_NAME": 35,
        "CUSTOMER_PHONE": 35,
        "ROUTING_ANSWER": 50,
        "DATE": 25,
        "RP_ID": 10,
        "CONN_ID": 15,
    }

    # Force fixed column widths as specified, in the order of headers
    col_widths = [max_col_widths.get(col, 30) for col in headers]

    # Do NOT rescale col_widths!
    # total_width_calculated = sum(col_widths)
    # if total_width_calculated > available_width:
    #     scale_factor = available_width / total_width_calculated
    #     col_widths = [w * scale_factor for w in col_widths]

    min_col_width = 10
    col_widths = [max(w, min_col_width) for w in col_widths]

    # Encabezados de la tabla
    pdf.set_font("Arial", 'B', 8)
    for i, header in enumerate(headers):
        clean_header = header.encode('latin-1', 'replace').decode('latin-1')
        pdf.cell(col_widths[i], 7, clean_header, 1, 0, 'L')  # <-- Cambiado a 'L'
    pdf.ln()

    # Datos de la tabla
    pdf.set_font("Arial", '', 7)
    cell_height = 6  # Height per line

    for index, row in df_str.iterrows():
        # Calculate lines and texts for each cell
        cell_lines = []
        cell_texts = []
        for i, data_item in enumerate(row):
            clean_data = str(data_item).encode('latin-1', 'replace').decode('latin-1')
            lines = pdf.multi_cell(col_widths[i], cell_height, clean_data, 0, 'L', split_only=True)
            cell_lines.append(len(lines))
            cell_texts.append(lines)
        max_lines = max(cell_lines)
        row_height = cell_height * max_lines

        # --- PAGE BREAK LOGIC: If not enough space, add new page before drawing row ---
        if pdf.get_y() + row_height > (pdf.h - pdf.b_margin):
            pdf.add_page()
            pdf.set_font("Arial", 'B', 8)
            for i, header in enumerate(headers):
                clean_header = header.encode('latin-1', 'replace').decode('latin-1')
                pdf.cell(col_widths[i], 7, clean_header, 1, 0, 'L')
            pdf.ln()
            pdf.set_font("Arial", '', 7)

        # Draw the row (as you already do)
        y_before = pdf.get_y()
        x_before = pdf.get_x()
        for i, lines in enumerate(cell_texts):
            pdf.rect(x_before, y_before, col_widths[i], row_height)
            pdf.set_xy(x_before, y_before)
            cell_content = "\n".join(lines + [''] * (max_lines - len(lines)))
            pdf.multi_cell(col_widths[i], cell_height, cell_content, 0, 'L')
            x_before += col_widths[i]
        pdf.set_y(y_before + row_height)

    # Guardar el PDF
    safe_rp_id_str = "".join(c if c.isalnum() else "_" for c in str(rp_id_value))
    pdf_filename = os.path.join(output_dir, f"{output_filename_base}_{safe_rp_id_str}.pdf")

    try:
        pdf.output(pdf_filename, "F")
        print(f"PDF generado con éxito: {pdf_filename}")
        return pdf_filename
    except Exception as e:
        print(f"Error al guardar el PDF {pdf_filename}: {e}")
        print("Asegúrate de que el archivo no esté abierto o protegido contra escritura.")
        return None

def main(file_path=None, rp_id_list=None):
    print("--- Asistente para Filtrar Excel/HTML y Exportar a PDF ---")
    
    # 1. Get file_path
    if file_path is None:
        file_path = input("Introduce la ruta completa de tu archivo Excel o HTML (.xls, .xlsx, .html): ")
    if not os.path.exists(file_path):
        print(f"Error: El archivo '{file_path}' no se encontró. Verifica la ruta.")
        return

    # 2. Load DataFrame
    if file_path.lower().endswith(('.xls', '.xlsx')):
        try:
            excel_file = pd.ExcelFile(file_path)
            sheet_to_read = 0
            if len(excel_file.sheet_names) > 1:
                print("Hojas disponibles en el archivo:")
                for i, name in enumerate(excel_file.sheet_names):
                    print(f"{i}: {name}")
                try:
                    sheet_choice = input(f"Elige el número o nombre de la hoja a usar (por defecto: '{excel_file.sheet_names[0]}'): ")
                    if sheet_choice.strip() == "":
                        sheet_to_read = excel_file.sheet_names[0]
                    else:
                        try:
                            sheet_to_read = int(sheet_choice)
                        except ValueError:
                            sheet_to_read = sheet_choice
                except Exception:
                    print("Selección de hoja no válida, usando la primera por defecto.")
                    sheet_to_read = excel_file.sheet_names[0]
            else:
                sheet_to_read = excel_file.sheet_names[0]
            main_df = pd.read_excel(excel_file, sheet_name=sheet_to_read)
        except Exception as e:
            print(f"Error al leer el archivo Excel: {e}")
            print("Verifica que el archivo sea válido y que tengas instaladas las librerías necesarias (pandas, openpyxl y/o xlrd).")
            return
    elif file_path.lower().endswith('.html'):
        try:
            dfs = pd.read_html(file_path)
            if not dfs:
                print("No se encontraron tablas en el archivo HTML.")
                return
            main_df = dfs[0]
        except Exception as e:
            print(f"Error al leer el archivo HTML: {e}")
            print("Verifica que el archivo sea válido y que tengas instaladas las librerías necesarias (pandas, lxml y/o html5lib).")
            return
    else:
        print("Error: El archivo proporcionado no parece ser un archivo Excel o HTML válido (.xls, .xlsx, .html).")
        return

    # 3. Get rp_id_list
    if rp_id_list is None:
        rp_ids_str = input("Introduce los RP_ID que quieres filtrar, separados por comas (ej: 61014, 61038): ")
        rp_id_list = [val.strip() for val in rp_ids_str.split(',') if val.strip()]
    if not rp_id_list:
        print("No se ingresaron RP_IDs para filtrar. Saliendo.")
        return

    # Nombre de la columna a filtrar
    filter_column_name = "RP_ID"

    # Verificar si la columna de filtro existe
    if filter_column_name not in main_df.columns:
        print(f"Error: La columna '{filter_column_name}' no existe en el archivo Excel.")
        print(f"Las columnas disponibles son: {main_df.columns.tolist()}")
        return
        
    # Convertir la columna RP_ID del DataFrame a string para asegurar una comparación consistente
    main_df[filter_column_name] = main_df[filter_column_name].astype(str)

    # Seleccionar solo las columnas requeridas para el PDF
    columns_to_export = [
        "RP_ID", "DATE", "CUSTOMER_NAME", "CUSTOMER_PHONE",
        "CUSTOMER_QUERY", "ROUTING_ANSWER", "CONN_ID"
    ]
    # Verificar que todas existan en el DataFrame
    missing_cols = [col for col in columns_to_export if col not in main_df.columns]
    if missing_cols:
        print(f"Error: Faltan las siguientes columnas requeridas en el archivo Excel: {missing_cols}")
        return

    # Crear directorio para los PDFs si no existe
    output_pdf_dir = "reportes_filtrados_pdf"
    if not os.path.exists(output_pdf_dir):
        os.makedirs(output_pdf_dir)
        print(f"Directorio '{output_pdf_dir}' creado para guardar los PDFs.")
    else:
        # Clear old PDFs before generating new ones
        for f in os.listdir(output_pdf_dir):
            if f.endswith(".pdf"):
                os.remove(os.path.join(output_pdf_dir, f))
                
    generated_files_count = 0

    # Before the PDF generation
    for rp_id_value in rp_id_list:
        filtered_df = main_df[main_df[filter_column_name] == rp_id_value]
        if filtered_df.empty:
            print(f"No se encontraron registros para RP_ID: {rp_id_value}.")
            continue

        # Seleccionar solo las columnas requeridas para el PDF
        filtered_df = filtered_df[columns_to_export]

        # Nombre base para el archivo PDF
        output_filename_base = "reporte_filtrado"

        # Generar el PDF
        pdf_file = create_pdf_from_dataframe(filtered_df, output_filename_base, rp_id_value, output_pdf_dir)
        if pdf_file:
            generated_files_count += 1

    if generated_files_count == 0:
        print("No se generaron archivos PDF. Verifica los RP_IDs y los datos del archivo Excel.")
    else:
        print(f"Se generaron {generated_files_count} archivos PDF en el directorio: '{output_pdf_dir}'.")

if __name__ == "__main__":
    main()