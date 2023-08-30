import os
import re
import PyPDF2

def extract_emails(text):
    email_matches = re.findall(r'\S+@\S+', text)
    return email_matches

def extract_phone_numbers(text):
    phone_matches = re.findall(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', text)
    return phone_matches

def extract_web_urls(text):
    url_matches = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    return url_matches

def extract_info_from_pdf(pdf_path):
    extracted_info = {
        "emails": [],
        "phone_numbers": [],
        "web_urls": []
    }

    try:
        pdf_file = open(pdf_path, "rb")
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            
            extracted_info["emails"].extend(extract_emails(text))
            extracted_info["phone_numbers"].extend(extract_phone_numbers(text))
            extracted_info["web_urls"].extend(extract_web_urls(text))

        pdf_file.close()
    except Exception as e:
        print("An error occurred:", e)

    return extracted_info

if __name__ == "__main__":
    folder_path = "PDF"

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            extracted_info = extract_info_from_pdf(pdf_path)
            
            print(f"Extracted info from {filename}:")
            print("Emails:", extracted_info["emails"])
            print("Phone Numbers:", extracted_info["phone_numbers"])
            print("Web URLs:", extracted_info["web_urls"])
            print("=" * 50)
