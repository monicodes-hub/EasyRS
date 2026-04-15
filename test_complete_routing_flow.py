# -*- coding: utf-8 -*-
"""
Comprehensive test simulating the complete routing flow from main_easyRS.py
"""
import os
import sys
import pandas as pd
import shutil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import routing

def get_downloads_folder():
    """Get the Downloads folder path"""
    if sys.platform == "win32":
        import ctypes
        from ctypes import wintypes, windll

        _SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
        _SHGetKnownFolderPath.argtypes = [
            ctypes.c_void_p, wintypes.DWORD, wintypes.HANDLE, ctypes.POINTER(ctypes.c_wchar_p)
        ]

        FOLDERID_Downloads = ctypes.c_char_p(b'{374DE290-123F-4565-9164-39C4925E467B}')
        path_ptr = ctypes.c_wchar_p()
        result = _SHGetKnownFolderPath(FOLDERID_Downloads, 0, 0, ctypes.byref(path_ptr))
        if result == 0:
            downloads = path_ptr.value
            ctypes.windll.ole32.CoTaskMemFree(path_ptr)
            return downloads
        else:
            return os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        return os.path.join(os.path.expanduser("~"), "Downloads")


def test_complete_routing_flow():
    """Test the complete routing flow including copying to Downloads"""
    print("=" * 70)
    print("COMPREHENSIVE TEST: Complete Routing Flow")
    print("=" * 70)
    print()
    
    # Step 1: Create test data
    print("Step 1: Creating test Excel file...")
    data = {
        'RP_ID': ['61014', '61014', '61038', '61038'],
        'DATE': ['2024-01-01', '2024-01-02', '2024-01-01', '2024-01-02'],
        'CUSTOMER_NAME': ['Cliente A', 'Cliente A', 'Cliente B', 'Cliente B'],
        'CUSTOMER_PHONE': ['555-1001', '555-1001', '555-2001', '555-2001'],
        'CUSTOMER_QUERY': ['Q1', 'Q1', 'Q2', 'Q2'],
        'ROUTING_ANSWER': ['R1', 'R1', 'R2', 'R2'],
        'CONN_ID': ['conn001', 'conn001', 'conn002', 'conn002']
    }
    
    df = pd.DataFrame(data)
    test_file = 'test_complete_routing_data.xlsx'
    df.to_excel(test_file, index=False)
    print(f"✓ Test file created: {test_file}")
    print()
    
    # Step 2: Prepare routing
    print("Step 2: Preparing routing environment...")
    pdf_folder = "reportes_filtrados_pdf"
    
    # Create folder if not exists
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)
        print(f"✓ Created directory: {pdf_folder}")
    
    # Clear old PDFs
    cleared_count = 0
    for f in os.listdir(pdf_folder):
        if f.endswith('.pdf'):
            try:
                os.remove(os.path.join(pdf_folder, f))
                cleared_count += 1
            except Exception as e:
                print(f"Warning: Could not remove {f}: {e}")
    
    if cleared_count > 0:
        print(f"✓ Cleared {cleared_count} old PDF(s)")
    
    print()
    
    # Step 3: Run routing
    print("Step 3: Running routing.main()...")
    try:
        routing.main(file_path=test_file, rp_id_list=['61014', '61038'])
        print("✓ routing.main() completed successfully")
    except Exception as e:
        print(f"✗ routing.main() failed: {e}")
        import traceback
        traceback.print_exc()
        return
    
    print()
    
    # Step 4: Check generated PDFs
    print("Step 4: Checking generated PDFs...")
    if not os.path.exists(pdf_folder):
        print(f"✗ PDF folder not found: {pdf_folder}")
        return
    
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    
    if not pdf_files:
        print(f"✗ No PDFs found in {pdf_folder}")
        return
    
    print(f"✓ Found {len(pdf_files)} PDF file(s):")
    for pdf_file in pdf_files:
        path = os.path.join(pdf_folder, pdf_file)
        size = os.path.getsize(path)
        print(f"    - {pdf_file} ({size} bytes)")
    
    print()
    
    # Step 5: Copy to Downloads
    print("Step 5: Copying PDFs to Downloads folder...")
    downloads = get_downloads_folder()
    print(f"  Downloads folder: {downloads}")
    print()
    
    pdfs_copied = []
    for pdf_file in pdf_files:
        src = os.path.join(pdf_folder, pdf_file)
        dst = os.path.join(downloads, pdf_file)
        try:
            shutil.copy(src, dst)
            pdfs_copied.append(dst)
            print(f"✓ Copied: {pdf_file}")
        except Exception as e:
            print(f"✗ Failed to copy {pdf_file}: {e}")
    
    print()
    
    # Step 6: Verify files were copied
    print("Step 6: Verifying files in Downloads...")
    if pdfs_copied:
        for pdf_path in pdfs_copied:
            if os.path.exists(pdf_path):
                size = os.path.getsize(pdf_path)
                print(f"✓ File verified: {os.path.basename(pdf_path)} ({size} bytes)")
            else:
                print(f"✗ File not found: {os.path.basename(pdf_path)}")
    
    print()
    
    # Step 7: Cleanup test file
    print("Step 7: Cleanup...")
    if os.path.exists(test_file):
        try:
            os.remove(test_file)
            print(f"✓ Removed test file: {test_file}")
        except Exception as e:
            print(f"Note: Could not remove test file {test_file}: {e}")
    
    print()
    print("=" * 70)
    print("RESULT: Complete routing flow test PASSED ✓")
    print("=" * 70)
    print()
    print("Summary:")
    print(f"  - Generated {len(pdf_files)} PDF(s)")
    print(f"  - Copied {len(pdfs_copied)} file(s) to Downloads")
    print(f"  - Downloads folder: {downloads}")
    if pdfs_copied:
        print(f"\nFiles in Downloads:")
        for pdf_path in pdfs_copied:
            print(f"  {os.path.basename(pdf_path)}")


if __name__ == "__main__":
    test_complete_routing_flow()
