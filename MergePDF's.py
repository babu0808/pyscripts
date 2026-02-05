import os
from PyPDF2 import PdfMerger

def merge_pdfs(directory):
    merger = PdfMerger()
    output_file = os.path.join(directory, "merged.pdf")  # Save merged file in the same folder

    # Iterate through and merge all PDFs in the directory
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory, filename)
            merger.append(file_path)
            print(f"Added: {filename}")

    merger.write(output_file)
    merger.close()
    print(f"All PDFs merged into: {output_file}")

if __name__ == "__main__":
    dir_path = input("Enter the directory path with PDFs: ")
    merge_pdfs(dir_path)
