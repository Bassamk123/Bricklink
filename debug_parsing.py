#!/usr/bin/env python3
"""
Debug the item parsing step by step
"""
import pdfplumber
import re

def debug_item_parsing():
    # Get the actual PDF text
    with pdfplumber.open("29154233.pdf") as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() or ""
    
    lines = full_text.split('\n')
    
    in_items_section = False
    print("Looking for 'Items in Order' section...")
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        if 'Items in Order' in line:
            print(f"Found 'Items in Order' at line {i}: {line}")
            in_items_section = True
            print("Next 20 lines after 'Items in Order':")
            for j in range(1, 21):
                if i+j < len(lines):
                    next_line = lines[i+j].strip()
                    if next_line:
                        print(f"  {i+j}: {next_line}")
                        
                        # Test our patterns
                        if 'New' == next_line:
                            print(f"    -> Found condition: {next_line}")
                        
                        colors = ['Red', 'Blue', 'Black', 'White', 'Yellow', 'Green', 'Brown', 'Orange', 
                                 'Purple', 'Pink', 'Tan', 'Gray', 'Dark Blue', 'Dark Red', 'Dark Green',
                                 'Light Blue', 'Light Gray', 'Reddish Brown', 'Dark Tan', 'Medium Blue',
                                 'Trans-Clear', 'Trans-Orange', 'Pearl Gold', 'Medium Nougat', 'Dark Orange',
                                 'Dark Azure', 'Bright Light Orange', 'Light Bluish Gray']
                        
                        for color in colors:
                            if next_line.startswith(color):
                                print(f"    -> Found color: {color}")
                                break
                        
                        if 'Part No:' in next_line:
                            print(f"    -> Found part number line: {next_line}")
                        
                        # Test price pattern
                        price_pattern = r'(\d+)\s+AU\s+\$([0-9.]+)\s+AU\s+\$([0-9.]+)\s+([0-9.]+g)'
                        if re.search(price_pattern, next_line):
                            print(f"    -> Found price pattern: {next_line}")
            break

if __name__ == "__main__":
    debug_item_parsing()