# -*- coding: utf-8 -*-
"""
Test to verify the pdf.output() fix for routing module
"""
import os
import pandas as pd
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_fpdf_output_methods():
    """Test different ways to call FPDF.output()"""
    from fpdf import FPDF
    
    print("=" * 60)
    print("TEST: FPDF.output() method signatures")
    print("=" * 60)
    
    # Create a simple PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Test PDF", 0, 1, 'C')
    
    # Test 1: Using just filename (correct for fpdf2)
    print("\nTest 1: pdf.output(filename)")
    try:
        test_file_1 = "test_output_method1.pdf"
        result = pdf.output(test_file_1)
        if os.path.exists(test_file_1):
            print(f"✓ Success - File created: {test_file_1}")
            os.remove(test_file_1)
        else:
            print(f"✗ Failed - File not created")
    except TypeError as e:
        print(f"✗ Failed with TypeError: {e}")
    except Exception as e:
        print(f"✗ Failed with error: {e}")
    
    # Test 2: Using filename with format parameter (old fpdf syntax)
    print("\nTest 2: pdf.output(filename, format) - OLD API")
    try:
        test_file_2 = "test_output_method2.pdf"
        result = pdf.output(test_file_2, "F")
        if os.path.exists(test_file_2):
            print(f"✓ Success - File created: {test_file_2}")
            os.remove(test_file_2)
        else:
            print(f"✗ Failed - File not created")
    except TypeError as e:
        print(f"✗ Failed with TypeError: {e}")
    except Exception as e:
        print(f"✗ Failed with error: {e}")

if __name__ == "__main__":
    test_fpdf_output_methods()
