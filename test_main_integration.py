# -*- coding: utf-8 -*-
"""
Integration test for main_easyRS_test.py workflow
Tests both conversations and routing flows together
"""
import os
import sys
import pandas as pd
import shutil
import re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the modules as the main application does
import conversations_test as conversations
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


def create_test_conversations_data(filename="test_conversations_data.html"):
    """Create sample conversations data following the expected format (HTML)"""
    print("Creating sample conversations data...")
    
    # Based on conversations.py expectations: CHANNEL, CONN_ID, TO_NAME
    data = {
        'CHANNEL': [
            'AGENT: AgentA, CHATID: 215578526',
            'AGENT: AgentA, CHATID: 215578526',
            'AGENT: AgentB, CHATID: 215578527',
            'AGENT: AgentB, CHATID: 215578527',
        ],
        'FROM': ['cliente@email.com', 'agente@empresa.com', 'cliente2@email.com', 'agente@empresa.com'],
        'FROM_NAME': ['Cliente 1', 'AgentA', 'Cliente 2', 'AgentB'],
        'TO_NAME': ['AgentA', 'Cliente 1', 'AgentB', 'Cliente 2'],
        'DATE': ['2024-01-01 10:00', '2024-01-01 10:30', '2024-01-01 11:00', '2024-01-01 11:30'],
        'MESSAGE': ['Hola, necesito ayuda', 'Claro, ¿qué necesitas?', 'Tengo una consulta', 'Te ayudaré'],
        'CONN_ID': ['215578526', '215578526', '215578527', '215578527'],
        'CUSTOMER_ID': ['cust001', 'cust001', 'cust002', 'cust002'],
        'CUSTOMER_PHONE': ['555-1001', '555-1001', '555-2001', '555-2001'],
    }
    
    df = pd.DataFrame(data)
    df.to_html(filename, index=False)
    print(f"✓ Created: {filename}")
    return filename


def create_test_routing_data(filename="test_routing_data.xlsx"):
    """Create sample routing data"""
    print("Creating sample routing data...")
    
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
    df.to_excel(filename, index=False)
    print(f"✓ Created: {filename}")
    return filename


def test_conversations_flow():
    """Test the conversations flow"""
    print("\n" + "=" * 70)
    print("TEST FLOW 1: Conversations")
    print("=" * 70)
    
    # Create test data
    conv_file = create_test_conversations_data()
    
    print("\nStep 1: Reading conversations file...")
    try:
        if conv_file.endswith('.html'):
            dfs = pd.read_html(conv_file)
            df = dfs[0]
        else:
            df = pd.read_csv(conv_file)
        print(f"✓ File read successfully, shape: {df.shape}")
        print(f"  Columns: {list(df.columns)}")
    except Exception as e:
        print(f"✗ Failed to read file: {e}")
        return False
    
    # Extract agent names
    print("\nStep 2: Extracting agent names...")
    agent_pattern = re.compile(r"AGENT:\s*([^,]+)")
    agent_names = set()
    for val in df["CHANNEL"].astype(str):
        for match in agent_pattern.findall(val):
            agent_names.add(match.strip())
    agent_names = sorted(agent_names)
    print(f"✓ Found agents: {agent_names}")
    
    # Test with first agent
    if not agent_names:
        print("✗ No agents found!")
        return False
    
    selected_agent = agent_names[0]
    print(f"\nStep 3: Testing with agent: {selected_agent}")
    
    # Clear old PDFs
    pdf_folder = "filtrado_conversaciones_pdf"
    if os.path.exists(pdf_folder):
        for f in os.listdir(pdf_folder):
            if f.endswith('.pdf'):
                try:
                    os.remove(os.path.join(pdf_folder, f))
                except Exception as e:
                    print(f"Warning: Could not remove {f}: {e}")
    
    # Run conversations.main()
    print(f"\nStep 4: Running conversations.main()...")
    try:
        conversations.main(file_path=conv_file, agent_name=selected_agent, conv_mode="1")
        print("✓ conversations.main() completed")
    except Exception as e:
        print(f"✗ conversations.main() failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Check for generated PDFs
    print(f"\nStep 5: Checking for generated PDFs in {pdf_folder}...")
    if not os.path.exists(pdf_folder):
        print(f"✗ PDF folder not found: {pdf_folder}")
        return False
    
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    if not pdf_files:
        print(f"✗ No PDFs found in {pdf_folder}")
        return False
    
    print(f"✓ Found {len(pdf_files)} PDF(s):")
    for pdf_file in pdf_files:
        path = os.path.join(pdf_folder, pdf_file)
        size = os.path.getsize(path)
        print(f"    - {pdf_file} ({size} bytes)")
    
    # Copy to Downloads (as the app does)
    print(f"\nStep 6: Copying PDFs to Downloads...")
    downloads = get_downloads_folder()
    pdfs_copied = []
    
    for f in os.listdir(pdf_folder):
        if f.endswith(".pdf"):
            src = os.path.join(pdf_folder, f)
            dst = os.path.join(downloads, f)
            try:
                shutil.copy(src, dst)
                pdfs_copied.append(dst)
                print(f"✓ Copied: {f}")
            except Exception as e:
                print(f"✗ Failed to copy {f}: {e}")
    
    if pdfs_copied:
        print(f"✓ Successfully copied {len(pdfs_copied)} file(s) to Downloads")
        return True
    else:
        print(f"✗ No files were copied")
        return False


def test_routing_flow():
    """Test the routing flow"""
    print("\n" + "=" * 70)
    print("TEST FLOW 2: Routing")
    print("=" * 70)
    
    # Create test data
    routing_file = create_test_routing_data()
    
    print("\nStep 1: Preparing routing test...")
    rp_id_list = ['61014', '61038']
    print(f"✓ RP_IDs to test: {rp_id_list}")
    
    # Clear old PDFs
    pdf_folder = "filtrado_routing_pdf"
    if os.path.exists(pdf_folder):
        for f in os.listdir(pdf_folder):
            if f.endswith('.pdf'):
                try:
                    os.remove(os.path.join(pdf_folder, f))
                except Exception as e:
                    print(f"Warning: Could not remove {f}: {e}")
    
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)
    
    # Run routing.main()
    print(f"\nStep 2: Running routing.main()...")
    try:
        routing.main(file_path=routing_file, rp_id_list=rp_id_list)
        print("✓ routing.main() completed")
    except Exception as e:
        print(f"✗ routing.main() failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Check for generated PDFs
    print(f"\nStep 3: Checking for generated PDFs in {pdf_folder}...")
    if not os.path.exists(pdf_folder):
        print(f"✗ PDF folder not found: {pdf_folder}")
        return False
    
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    if not pdf_files:
        print(f"✗ No PDFs found in {pdf_folder}")
        return False
    
    print(f"✓ Found {len(pdf_files)} PDF(s):")
    for pdf_file in pdf_files:
        path = os.path.join(pdf_folder, pdf_file)
        size = os.path.getsize(path)
        print(f"    - {pdf_file} ({size} bytes)")
    
    # Copy to Downloads (as the app does)
    print(f"\nStep 4: Copying PDFs to Downloads...")
    downloads = get_downloads_folder()
    pdfs_copied = []
    
    for f in os.listdir(pdf_folder):
        if f.endswith(".pdf"):
            src = os.path.join(pdf_folder, f)
            dst = os.path.join(downloads, f)
            try:
                shutil.copy(src, dst)
                pdfs_copied.append(dst)
                print(f"✓ Copied: {f}")
            except Exception as e:
                print(f"✗ Failed to copy {f}: {e}")
    
    if pdfs_copied:
        print(f"✓ Successfully copied {len(pdfs_copied)} file(s) to Downloads")
        print(f"  Downloads folder: {downloads}")
        return True
    else:
        print(f"✗ No files were copied")
        return False


def main():
    """Run all integration tests"""
    print("\n" + "=" * 70)
    print("INTEGRATION TEST: main_easyRS_test.py workflow")
    print("=" * 70)
    
    results = {}
    
    # Test conversations flow
    results['conversations'] = test_conversations_flow()
    
    # Test routing flow
    results['routing'] = test_routing_flow()
    
    # Summary
    print("\n" + "=" * 70)
    print("INTEGRATION TEST SUMMARY")
    print("=" * 70)
    
    for test_name, passed in results.items():
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{test_name.upper()}: {status}")
    
    all_passed = all(results.values())
    
    print()
    if all_passed:
        print("✓ ALL TESTS PASSED - Ready to use main_easyRS_test.py")
    else:
        print("✗ SOME TESTS FAILED - Please review the output above")
    
    print("=" * 70)
    
    return all_passed


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
