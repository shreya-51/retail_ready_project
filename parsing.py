import fitz
import json

def extract_text_from_pdf(file_path, start_page, end_page):
    document = fitz.open(file_path)
    text = ""
    # Ensure the page numbers are within the valid range
    start_page = max(start_page, 0) - 1 # PDF page indexing starts at 1, not 0
    end_page = min(end_page, document.page_count - 1) - 1 # PDF page indexing starts at 1, not 0
    
    for page_num in range(start_page, end_page + 1):
        page = document[page_num]
        text += page.get_text()
    
    document.close()
    return text

def extract_json(response: str) -> json:
    try:
        json_data = json.loads(response[response.find("{") : response.rfind("}") + 1])
    except:
        # fail if
        #   1. multiple json objects
        #   2. no json objects
        #   3. incorrect json objects
        return None
    return json_data
