#!/usr/bin/env python3
"""
Debug script to examine PDF content
"""
import pdfplumber

def debug_pdf(pdf_path):
    print(f"Debugging PDF: {pdf_path}")
    print("=" * 50)
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                print(f"\n--- Page {i+1} ---")
                if text:
                    # Show first 1000 characters
                    print(text[:1000])
                    print("\n[...text truncated...]")
                else:
                    print("No text extracted from this page")
                    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_pdf("29154233.pdf")