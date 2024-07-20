import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_pdf(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {filename}")

def main():
    base_url = "https://neetfs.ntaonline.in/NEET_2024_Result/"
    start_number = 110101
    end_number = 470000
    output_directory = "downloaded_pdfs"

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Create a list of tasks
    tasks = []
    for number in range(start_number, end_number + 1):
        url = f"{base_url}{number}.pdf"
        filename = os.path.join(output_directory, f"{number}.pdf")
        tasks.append((url, filename))

    # Use ThreadPoolExecutor for parallel downloads
    with ThreadPoolExecutor(max_workers=1000) as executor:
        futures = [executor.submit(download_pdf, url, filename) for url, filename in tasks]
        
        for future in as_completed(futures):
            future.result()

if __name__ == "__main__":
    main()
