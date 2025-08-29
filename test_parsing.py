#!/usr/bin/env python3
"""
Test the parsing logic directly
"""
from Price_Calculator import extract_items_from_text_advanced, extract_currency_and_amounts_advanced
import pdfplumber

def test_parsing():
    # Get the actual PDF text
    with pdfplumber.open("29154233.pdf") as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() or ""
    
    print("Testing currency extraction:")
    currency, amounts = extract_currency_and_amounts_advanced(full_text)
    print(f"Currency: {currency}")
    print(f"Amounts: {amounts}")
    
    print("\nTesting item extraction:")
    items = extract_items_from_text_advanced(full_text)
    print(f"Found {len(items)} items:")
    
    for i, item in enumerate(items):
        print(f"Item {i+1}: {item}")

if __name__ == "__main__":
    test_parsing()