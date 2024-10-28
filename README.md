
---

# Simple OCR Processor

A Python-based OCR tool that uses [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and [pytesseract](https://github.com/madmaze/pytesseract) to extract text from images in a specified directory. The script logs processing details and saves extracted text to `.txt` files in an output directory.

## Features
- **Batch Processing**: Processes all images in a directory.
- **Text Extraction**: Extracts text from images and saves each output as a `.txt` file.
- **Error Handling**: Logs missing files, permission issues, and processing errors.
- **Configurable Output**: Allows specifying an output directory.

## Requirements
- Python 3.6 or higher
- Tesseract OCR ([download link](https://github.com/tesseract-ocr/tesseract))
- Python packages: `pytesseract`, `Pillow`

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/LuminousVee/SimpleOCRProcessor.git
cd SimpleOCRProcessor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR
Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).

### 4. Configure Tesseract Path
Ensure Tesseract OCR’s installation path is in the list of default paths in the script. If necessary, manually update the path in the `set_tesseract_path` method in `SimpleOCRProcessor.py`.

## Usage

### Basic Usage
Run the script with the following command to process all images in a directory:
```bash
python ocr-processor.py /path/to/image/directory
```

### Example
```bash
python SimpleOCRProcessor.py ./sample_images
```

### Command-Line Arguments
- **`directory`**: Specify the directory containing images. If no directory is provided, the current working directory is used.

## Output
Processed text files are saved in the `output` directory, created automatically if it doesn't exist. Each file is named using the pattern `ocr_<image_name>_<timestamp>.txt`.

## File Structure
```plaintext
SimpleOCRProcessor/
├── ocr-processor.py    # Main script with OCR functionality
├── README.md                # Documentation file
├── requirements.txt         # Python package dependencies
└── output/                  # Directory to store processed text files
```

## Code Documentation

### Classes and Methods

- **SimpleOCRProcessor**:
  - `__init__(self, output_dir="output")`: Initializes the processor with an output directory.
  - `set_tesseract_path(self)`: Attempts to locate the Tesseract executable.
  - `process_image(self, image_path)`: Processes an image and returns extracted text.
  - `save_text(self, text, filename)`: Saves the extracted text to a `.txt` file.
  - `process_batch(self, directory)`: Processes all images in a directory.

### Sample Logs
The processor logs various operations and issues encountered:
```plaintext
2024-10-27 12:30:01 - Processing: image1.png
2024-10-27 12:30:10 - Saved text to: ocr_image1_20241027_123010.txt
2024-10-27 12:31:15 - Error processing image2.jpg: <error message>
```

## Contribution
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

---

