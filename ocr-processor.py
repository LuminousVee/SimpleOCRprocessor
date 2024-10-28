import pytesseract
from PIL import Image
import os
from pathlib import Path
import logging
from datetime import datetime
import sys

class SimpleOCRProcessor:
    def __init__(self, output_dir="output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Setup basic logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            handlers=[logging.StreamHandler()]
        )
        
        # Set and verify Tesseract path
        self.set_tesseract_path()
    
    def set_tesseract_path(self):
        """Set and verify Tesseract executable path."""
        # Common installation paths
        possible_paths = [
            r'C:\Program Files\Tesseract-OCR\tesseract.exe',
            r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
            r'C:\Users\BU\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
        ]
        
        # Try to find Tesseract executable
        tesseract_path = None
        for path in possible_paths:
            if Path(path).exists():
                tesseract_path = path
                break
        
        if not tesseract_path:
            logging.error("Tesseract executable not found. Please install Tesseract OCR and update the path.")
            sys.exit(1)
            
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
        
        # Verify Tesseract installation
        try:
            pytesseract.get_tesseract_version()
        except Exception as e:
            logging.error(f"Error verifying Tesseract installation: {str(e)}")
            sys.exit(1)
    
    def process_image(self, image_path):
        """Process a single image and return extracted text."""
        try:
            image_path = Path(image_path)
            if not image_path.exists():
                logging.error(f"Image file not found: {image_path}")
                return None
                
            if not os.access(image_path, os.R_OK):
                logging.error(f"No read permission for file: {image_path}")
                return None
                
            with Image.open(image_path) as img:
                # Convert to RGB if necessary
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                    
                text = pytesseract.image_to_string(img, lang='eng')
                return text.strip()
        except PermissionError:
            logging.error(f"Permission denied accessing file: {image_path}")
            return None
        except Exception as e:
            logging.error(f"Error processing {image_path}: {str(e)}")
            return None
    
    def save_text(self, text, filename):
        """Save extracted text to a file."""
        output_path = self.output_dir / f"{filename}.txt"
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
            return True
        except PermissionError:
            logging.error(f"Permission denied writing to: {output_path}")
            return False
        except Exception as e:
            logging.error(f"Error saving text: {str(e)}")
            return False
    
    def process_batch(self, directory):
        """Process all images in a directory."""
        directory = Path(directory)
        if not directory.exists():
            logging.error(f"Directory not found: {directory}")
            return
        
        if not os.access(directory, os.R_OK):
            logging.error(f"No read permission for directory: {directory}")
            return
        
        # Process all image files
        image_extensions = {'.png', '.jpg', '.jpeg', '.tiff', '.bmp'}
        found_images = False
        
        for image_path in directory.glob('*'):
            if image_path.suffix.lower() in image_extensions:
                found_images = True
                logging.info(f"Processing: {image_path.name}")
                text = self.process_image(image_path)
                if text:
                    filename = f"ocr_{image_path.stem}_{datetime.now():%Y%m%d_%H%M%S}"
                    if self.save_text(text, filename):
                        logging.info(f"Saved text to: {filename}.txt")
        
        if not found_images:
            logging.warning(f"No image files found in {directory}")

def main():
    # Get directory from command line argument or use current directory
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.getcwd()
    
    # Create processor instance
    processor = SimpleOCRProcessor()
    
    print(f"Processing images in: {directory}")
    processor.process_batch(directory)
    print("Processing complete. Check output folder for results.")

if __name__ == "__main__":
    main()
