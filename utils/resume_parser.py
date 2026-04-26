from pyresparser import ResumeParser
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
import io

def extract_resume_data(file_path):
    """Extract structured data from resume"""
    try:
        data = ResumeParser(file_path).get_extracted_data()
        return data
    except Exception as e:
        print(f"Error parsing resume: {e}")
        return None

def pdf_reader(file):
    try:
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
        page_interpreter = PDFPageInterpreter(resource_manager, converter)

        with open(file, 'rb') as fh:
            for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
                page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

        converter.close()
        fake_file_handle.close()

        return text

    except Exception as e:
        print(f"PDF Reader Error: {e}")
        return ""