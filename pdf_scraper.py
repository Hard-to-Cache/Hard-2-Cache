import fitz  
import os

pdf_folder = "pdfs"  
os.makedirs("scraped_text", exist_ok=True)

for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        filepath = os.path.join(pdf_folder, filename)
        doc = fitz.open(filepath)

        all_text = ""
        for page in doc:
            all_text += page.get_text()

        output_filename = filename.replace(".pdf", ".txt")
        output_path = os.path.join("scraped_text", output_filename)

        with open(output_path, "w", encoding="utf-8") as out_file:
            out_file.write(all_text)

        print(f"Scraped: {filename}")
