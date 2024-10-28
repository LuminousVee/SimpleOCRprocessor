# SimpleOCRProcessor

A Python-based OCR (Optical Character Recognition) utility that processes images and extracts text using Tesseract OCR. This tool supports batch processing of images and automatically saves the extracted text to files.

## Features

- Single image and batch processing capabilities
- Supports multiple image formats (PNG, JPG, JPEG, TIFF, BMP)
- Automatic text extraction and saving
- Built-in logging system
- Configurable output directory
- Automatic Tesseract path detection
- Error handling and validation

## Prerequisites

Before using this tool, ensure you have the following installed:

1. Python 3.x
2. Tesseract OCR engine
   - Windows: Download and install from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - Linux: `sudo apt-get install tesseract-ocr`
   - macOS: `brew install tesseract`

## Installation

1. Clone this repository or download the script
2. Install required Python packages:
```bash
pip install pytesseract Pillow
```

## Usage

### Command Line

Run the script from the command line:
```bash
python ocr_processor.py [directory_path]
```
If no directory is specified, it will process images in the current directory.

### As a Module

```python
from ocr_processor import SimpleOCRProcessor

# Create processor instance
processor = SimpleOCRProcessor(output_dir="custom_output")

# Process a single image
text = processor.process_image("path/to/image.png")

# Process all images in a directory
processor.process_batch("path/to/image/directory")
```

## Output

- Extracted text is saved in the specified output directory (defaults to "output")
- Files are named in the format: `ocr_[original_filename]_[timestamp].txt`
- Processing status and errors are logged to the console

## Directory Structure

```
project/
├── ocr_processor.py
├── output/
│   ├── ocr_image1_20241028_123456.txt
│   └── ocr_image2_20241028_123457.txt
└── images/
    ├── image1.png
    └── image2.jpg
```

## Error Handling

The script includes comprehensive error handling for:
- Missing Tesseract installation
- Invalid file permissions
- Missing files or directories
- Image processing errors
- File writing errors

## Supported Image Formats

- PNG (.png)
- JPEG (.jpg, .jpeg)
- TIFF (.tiff)
- BMP (.bmp)

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Notes

- Ensure Tesseract OCR is properly installed and accessible from the system path
- For Windows users, the script automatically checks common Tesseract installation paths
- Processing large images or batches may take some time depending on system capabilities
