import fitz  # PyMuPDF

def extract_words_from_pdf(pdf_path):
    # Open the provided PDF file
    doc = fitz.open(pdf_path)

    words = []
    
    # Loop through each page in the PDF
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # Load a specific page
        text = page.get_text("words")  # Extract words as a list of (x0, y0, x1, y1, word)
        
        for word_info in text:
            word = word_info[4]  # The word is the last element in the tuple
            words.append(word)
    
    return words


def main():
    pdf_path = "sample.pdf"  # Path to your PDF file
    words = extract_words_from_pdf(pdf_path)
    
    # Display or save the extracted words
    print(f"Extracted {len(words)} words.")
    print("Sample words:", words[:10])  # Show a sample of the extracted words

if __name__ == "__main__":
    main()
