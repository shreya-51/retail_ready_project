import re

from parsing import extract_text_from_pdf

def normalize_text(text):
    text = text.lower()
    text = re.sub(r'[\u2022\u2023\u25E6\u2043\u2219o]', '', text)
    text = re.sub(r'[\u2010-\u2015\u2212\uFE58\uFE63\uFF0D\-]+', '-', text)
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def verify_sources_in_pdf(json_data, table_of_contents, pdf_path):
    results = {}
    for section, details in table_of_contents.items():
        section_text = extract_text_from_pdf(pdf_path, details['start'], details['end'])
        normalized_section_text = normalize_text(section_text)
        if section in json_data:
            if json_data[section]:
                requirements = json_data[section]['requirements']
                results[section] = {}
                for req in requirements:
                    source = req['source']
                    normalized_source = normalize_text(source)
                    source_in_text = normalized_source in normalized_section_text
                    results[section][source] = source_in_text
    return results

def calculate_percentage_passed(result):
    count = sum(1 for value in result.values() for j in value.values() if j)
    total = sum(len(value) for value in result.values())
    return count/total

def print_negatives(result):
    for key, value in result.items():
        print(key)
        for i, j in value.items():
            if not j:
                print(i)
        print()