# BrickLink Order Price Calculator

A comprehensive tool for calculating true item costs from BrickLink PDF invoices by distributing shipping costs and fees proportionally across all items.

## Features

### Multi-Currency Support
- **Automatic detection**: USD, AUD, EUR, GBP, SEK, CAD, NZD, DKK
- **Flexible parsing**: Handles various currency formats and symbols
- **Exchange rate tracking**: Shows original and converted amounts

### Overhead Cost Distribution  
- **Smart calculation**: Automatically calculates overhead percentage from shipping, insurance, and additional charges
- **Proportional distribution**: Each item gets its fair share of total overhead costs
- **True pricing**: Shows both original and adjusted unit prices including all fees

### Advanced PDF Processing
- **Batch processing**: Handles multiple PDF files automatically
- **Robust parsing**: Extracts order details, item information, quantities, and pricing
- **Error handling**: Graceful handling of malformed or complex PDFs
- **Pattern recognition**: Adapts to BrickLink invoice formatting variations

### CSV Output
- **Comprehensive data**: Order number, date, currency, item details, original and adjusted pricing
- **Summary statistics**: Per-currency totals and overhead percentages  
- **Timestamped files**: Automatic file naming with timestamps
- **Excel compatible**: Clean CSV format for further analysis

## Usage

### Quick Start
```bash
python Price_Calculator.py
```

Select option 1: "Convert all PDFs to CSV (Recommended)"

### Menu Options
1. **Convert all PDFs to CSV** - Batch process all PDF files in directory
2. **Process single PDF** - Legacy mode for individual file processing  
3. **Interactive calculator** - Manual cost calculation with custom rates

### Requirements
```bash
pip install pdfplumber
```

## File Structure

```
├── Price_Calculator.py          # Main application
├── CLAUDE.md                   # This documentation
├── Updated_Price_Files/        # Output directory for CSV files
├── *.pdf                      # BrickLink invoice PDFs
├── test_converter.py          # Automated testing script
├── debug_pdf.py               # PDF extraction debugger
├── debug_parsing.py           # Pattern matching debugger
└── test_parsing.py            # Unit tests for parsing logic
```

## Example Output

The CSV output includes these columns:
- `Order_Number`: BrickLink order identifier
- `Order_Date`: When the order was placed
- `Currency`: Original invoice currency
- `Color`: LEGO element color
- `Description`: Item name and details
- `Part_Number`: BrickLink part number
- `Quantity`: Number of pieces
- `Original_Unit_Price`: Base price per unit
- `Overhead_Percentage`: Calculated overhead rate
- `Overhead_Amount`: Additional cost per unit
- `Adjusted_Unit_Price`: True cost including overhead
- `Original_Total`: Base total for item
- `Adjusted_Total`: True total including overhead
- `Weight`: Item weight
- `Order_Subtotal`, `Shipping`, `Insurance`: Order-level costs
- `Additional_Charges`, `Credit`, `Grand_Total`: Final pricing

## Algorithm

### Cost Distribution Logic
1. **Extract Financial Data**: Parse order subtotal, shipping, insurance, additional charges, and credits
2. **Calculate Overhead Rate**: `(shipping + insurance + additional_charges - credits) / subtotal * 100`
3. **Apply to Items**: For each item, add `original_price * overhead_rate` to get true unit cost
4. **Proportional Distribution**: Ensures total overhead distributed equals actual overhead charged

### PDF Parsing Strategy  
1. **Currency Detection**: Pattern matching for currency symbols and codes
2. **Section Identification**: Locate "Items in Order" and related sections
3. **Item Extraction**: Multi-line parsing for color, description, quantities, and pricing
4. **Data Validation**: Cross-reference totals and handle parsing errors

## Supported Invoice Formats

- **BrickLink Standard**: All standard BrickLink invoice formats
- **Multi-page**: Handles invoices spanning multiple pages  
- **International**: Supports global BrickLink stores with various currencies
- **Complex Items**: Parses detailed item names, part numbers, and specifications

## Development Notes

Built with Python 3.x using:
- `pdfplumber`: PDF text extraction and processing
- `csv`: Structured data output
- `re`: Pattern matching for invoice parsing
- `datetime`: Timestamp generation
- `os`, `glob`: File system operations

## Contributing

This tool was developed to solve the common problem of calculating true LEGO part costs when BrickLink orders include shipping and fees that need to be distributed proportionally across items for accurate cost analysis.

---

*Generated with [Claude Code](https://claude.ai/code)*