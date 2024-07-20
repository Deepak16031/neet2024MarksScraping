import os
import pdfplumber
import pandas as pd

def extract_text_from_all_pages(pdf_path):
    """
    Extracts text from all pages of the given PDF file.

    Parameters:
    pdf_path (str): Path to the PDF file.

    Returns:
    str: Text extracted from all pages.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def text_to_csv(text, csv_path):
    """
    Converts text to CSV and saves it to the specified path.

    Parameters:
    text (str): Text to be converted.
    csv_path (str): Path where the CSV file will be saved.
    """
    lines = text.splitlines()
    if len(lines) > 0:
        headers = lines[0].split()
        data = [line.split() for line in lines[1:] if line.strip() != '']
        df = pd.DataFrame(data)
        df.to_csv(csv_path, index=False)

def pdf_to_csv(pdf_path, csv_path):
    """
    Extracts text from a PDF file and saves it as a CSV file.

    Parameters:
    pdf_path (str): Path to the PDF file.
    csv_path (str): Path where the CSV file will be saved.
    """
    text = extract_text_from_all_pages(pdf_path)
    text_to_csv(text, csv_path)

def convert_all_pdfs_in_folder(input_folder, output_folder):
    """
    Converts all PDF files in the specified input folder to CSV files in the specified output folder.

    Parameters:
    input_folder (str): Path to the input folder containing PDF files.
    output_folder (str): Path to the output folder where CSV files will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            csv_filename = f"{os.path.splitext(filename)[0]}.csv"
            csv_path = os.path.join(output_folder, csv_filename)
            pdf_to_csv(pdf_path, csv_path)
            print(f"Converted {pdf_path} to {csv_path}")

# Example usage
input_folder = 'downloaded_pdfs'
output_folder = 'csv'
convert_all_pdfs_in_folder(input_folder, output_folder)

