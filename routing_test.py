# -*- coding: utf-8 -*-
"""
Test file for routing module to diagnose folder creation and PDF generation issues
"""
import os
import sys
import pandas as pd
import shutil

# Add the current directory to the path to import routing module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import routing

def test_routing_folder_creation():
    """Test if the routing module can create and find the output folder"""
    print("=" * 60)
    print("TEST 1: Checking folder creation and working directory")
    print("=" * 60)
    
    current_dir = os.getcwd()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    print(f"Current working directory: {current_dir}")
    print(f"Script directory: {script_dir}")
    print(f"Are they the same? {current_dir == script_dir}")
    print()
    
    # Check if reportes_filtrados_pdf exists
    output_pdf_dir = "reportes_filtrados_pdf"
    full_path = os.path.join(current_dir, output_pdf_dir)
    
    print(f"Expected output directory: {output_pdf_dir}")
    print(f"Full path: {full_path}")
    print(f"Directory exists? {os.path.exists(output_pdf_dir)}")
    
    # Try to create it
    if not os.path.exists(output_pdf_dir):
        try:
            os.makedirs(output_pdf_dir)
            print(f"✓ Successfully created directory: {output_pdf_dir}")
        except Exception as e:
            print(f"✗ Failed to create directory: {e}")
    else:
        print(f"✓ Directory already exists: {output_pdf_dir}")
    
    print()

def test_create_sample_data():
    """Create sample data to test routing.main()"""
    print("=" * 60)
    print("TEST 2: Creating sample Excel file for routing")
    print("=" * 60)
    
    # Create sample data
    data = {
        'RP_ID': ['61014', '61014', '61038', '61038'],
        'DATE': ['2024-01-01', '2024-01-02', '2024-01-01', '2024-01-02'],
        'CUSTOMER_NAME': ['Cliente 1', 'Cliente 1', 'Cliente 2', 'Cliente 2'],
        'CUSTOMER_PHONE': ['555-0001', '555-0001', '555-0002', '555-0002'],
        'CUSTOMER_QUERY': ['Consulta 1', 'Consulta 1', 'Consulta 2', 'Consulta 2'],
        'ROUTING_ANSWER': ['Respuesta 1', 'Respuesta 1', 'Respuesta 2', 'Respuesta 2'],
        'CONN_ID': ['conn001', 'conn001', 'conn002', 'conn002']
    }
    
    df = pd.DataFrame(data)
    
    # Save to Excel
    test_file = 'test_routing_data.xlsx'
    try:
        df.to_excel(test_file, index=False)
        print(f"✓ Created test file: {test_file}")
        print(f"  File exists: {os.path.exists(test_file)}")
        print(f"  File location: {os.path.abspath(test_file)}")
        print(f"  Data shape: {df.shape}")
        print(f"  Columns: {list(df.columns)}")
        return test_file
    except Exception as e:
        print(f"✗ Failed to create test file: {e}")
        return None

def test_routing_main():
    """Test the routing.main() function"""
    print("=" * 60)
    print("TEST 3: Testing routing.main() function")
    print("=" * 60)
    
    # Create test data
    test_file = test_create_sample_data()
    if not test_file:
        print("✗ Cannot proceed - test file creation failed")
        return
    
    print()
    
    # Check the output directory before calling main()
    output_dir = "reportes_filtrados_pdf"
    print(f"Output directory before routing.main(): {os.path.exists(output_dir)}")
    
    # Clear any existing PDFs
    if os.path.exists(output_dir):
        for f in os.listdir(output_dir):
            if f.endswith('.pdf'):
                try:
                    os.remove(os.path.join(output_dir, f))
                    print(f"  Removed old PDF: {f}")
                except Exception as e:
                    print(f"  Failed to remove {f}: {e}")
    
    print()
    
    # Call routing.main() with test data
    try:
        print("Calling routing.main()...")
        routing.main(file_path=test_file, rp_id_list=['61014', '61038'])
        print("✓ routing.main() completed successfully")
    except Exception as e:
        print(f"✗ routing.main() raised an exception: {e}")
        import traceback
        traceback.print_exc()
    
    print()
    
    # Check if output directory was created and contains PDFs
    print(f"Output directory exists after routing.main(): {os.path.exists(output_dir)}")
    
    if os.path.exists(output_dir):
        files = os.listdir(output_dir)
        pdf_files = [f for f in files if f.endswith('.pdf')]
        print(f"Total files in directory: {len(files)}")
        print(f"PDF files found: {len(pdf_files)}")
        for pdf_file in pdf_files:
            path = os.path.join(output_dir, pdf_file)
            size = os.path.getsize(path)
            print(f"  - {pdf_file} ({size} bytes)")
    else:
        print("✗ Output directory does not exist!")
    
    # Clean up test file
    if os.path.exists(test_file):
        try:
            os.remove(test_file)
            print(f"\nCleaned up test file: {test_file}")
        except Exception as e:
            print(f"Failed to clean up test file: {e}")

def test_folder_path_resolution():
    """Test how folder paths are resolved"""
    print("=" * 60)
    print("TEST 4: Folder path resolution")
    print("=" * 60)
    
    output_pdf_dir = "reportes_filtrados_pdf"
    
    print(f"Relative path: {output_pdf_dir}")
    print(f"Absolute path: {os.path.abspath(output_pdf_dir)}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"__file__ would resolve to: {os.path.abspath(__file__)}")
    print()
    
    # Test different path scenarios
    scenarios = [
        ("os.path.exists()", os.path.exists(output_pdf_dir)),
        ("os.path.isdir()", os.path.isdir(output_pdf_dir)),
    ]
    
    for desc, result in scenarios:
        print(f"{desc}: {result}")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("ROUTING MODULE DIAGNOSTIC TEST")
    print("=" * 60 + "\n")
    
    test_folder_path_resolution()
    print()
    test_routing_folder_creation()
    print()
    test_routing_main()
    
    print("\n" + "=" * 60)
    print("DIAGNOSTIC TEST COMPLETED")
    print("=" * 60)
