# -*- coding: utf-8 -*-
"""
Test file for corrected routing module
"""
import pandas as pd
from fpdf import FPDF
import os

def create_pdf_from_dataframe_FIXED(dataframe, output_filename_base, rp_id_value, output_dir):
    """
    FIXED VERSION: Crea un archivo PDF a partir de un DataFrame de Pandas.
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

    col_widths = [max_col_widths.get(col, 30) for col in headers]
    min_col_width = 10
    col_widths = [max(w, min_col_width) for w in col_widths]

    # Encabezados de la tabla
    pdf.set_font("Arial", 'B', 8)
    for i, header in enumerate(headers):
        clean_header = header.encode('latin-1', 'replace').decode('latin-1')
        pdf.cell(col_widths[i], 7, clean_header, 1, 0, 'L')
    pdf.ln()

    # Datos de la tabla
    pdf.set_font("Arial", '', 7)
    cell_height = 6

    for index, row in df_str.iterrows():
        cell_lines = []
        cell_texts = []
        for i, data_item in enumerate(row):
            clean_data = str(data_item).encode('latin-1', 'replace').decode('latin-1')
            lines = pdf.multi_cell(col_widths[i], cell_height, clean_data, 0, 'L', split_only=True)
            cell_lines.append(len(lines))
            cell_texts.append(lines)
        max_lines = max(cell_lines) if cell_lines else 1
        row_height = cell_height * max_lines

        # PAGE BREAK LOGIC
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
        for i, lines in enumerate(cell_texts):
            pdf.rect(x_before, y_before, col_widths[i], row_height)
            pdf.set_xy(x_before, y_before)
            cell_content = "\n".join(lines + [''] * (max_lines - len(lines)))
            pdf.multi_cell(col_widths[i], cell_height, cell_content, 0, 'L')
            x_before += col_widths[i]
        pdf.set_y(y_before + row_height)

    # Guardar el PDF - FIXED: Removed second parameter "F"
    safe_rp_id_str = "".join(c if c.isalnum() else "_" for c in str(rp_id_value))
    pdf_filename = os.path.join(output_dir, f"{output_filename_base}_{safe_rp_id_str}.pdf")

    try:
        # FIXED: Changed from pdf.output(pdf_filename, "F") to pdf.output(pdf_filename)
        pdf.output(pdf_filename)
        print(f"✓ PDF generado con éxito: {pdf_filename}")
        return pdf_filename
    except Exception as e:
        print(f"✗ Error al guardar el PDF {pdf_filename}: {e}")
        return None


def test_fixed_routing():
    """Test the fixed routing PDF generation"""
    print("=" * 60)
    print("TEST: Fixed routing PDF generation")
    print("=" * 60)
    print()
    
    # Create test data
    data = {
        'RP_ID': ['61014', '61014', '61038'],
        'DATE': ['2024-01-01', '2024-01-02', '2024-01-01'],
        'CUSTOMER_NAME': ['Cliente 1', 'Cliente 1', 'Cliente 2'],
        'CUSTOMER_PHONE': ['555-0001', '555-0001', '555-0002'],
        'CUSTOMER_QUERY': ['Consulta 1', 'Consulta 1', 'Consulta 2'],
        'ROUTING_ANSWER': ['Respuesta 1', 'Respuesta 1', 'Respuesta 2'],
        'CONN_ID': ['conn001', 'conn001', 'conn002']
    }
    
    df = pd.DataFrame(data)
    
    # Create output directory
    output_dir = "reportes_filtrados_pdf"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Clear old files
    for f in os.listdir(output_dir):
        if f.endswith('.pdf'):
            try:
                os.remove(os.path.join(output_dir, f))
                print(f"Removed old file: {f}")
            except Exception as e:
                print(f"Failed to remove {f}: {e}")
    
    print()
    
    # Test with RP_ID 61014
    print("Testing with RP_ID: 61014")
    filtered_df = df[df['RP_ID'] == '61014']
    pdf_file1 = create_pdf_from_dataframe_FIXED(filtered_df, "reporte_filtrado", "61014", output_dir)
    
    print()
    
    # Test with RP_ID 61038
    print("Testing with RP_ID: 61038")
    filtered_df = df[df['RP_ID'] == '61038']
    pdf_file2 = create_pdf_from_dataframe_FIXED(filtered_df, "reporte_filtrado", "61038", output_dir)
    
    print()
    print("=" * 60)
    print("RESULT: Checking generated files")
    print("=" * 60)
    
    if os.path.exists(output_dir):
        files = os.listdir(output_dir)
        pdf_files = [f for f in files if f.endswith('.pdf')]
        print(f"✓ Output directory exists: {output_dir}")
        print(f"  Total files: {len(files)}")
        print(f"  PDF files generated: {len(pdf_files)}")
        for pdf_file in pdf_files:
            path = os.path.join(output_dir, pdf_file)
            size = os.path.getsize(path)
            print(f"    - {pdf_file} ({size} bytes)")
    else:
        print(f"✗ Output directory not found: {output_dir}")


if __name__ == "__main__":
    test_fixed_routing()
