import PyPDF2

def read_pdf(file_path):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        # Create PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Get total number of pages
        num_pages = len(pdf_reader.pages)
        
        # Store all text from PDF
        text = ""
        
        # Extract text from each page
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
            
        return text

def search_in_pdf(file_path, search_term):
    # Get PDF content
    content = read_pdf(file_path)
    
    # Convert both content and search term to lowercase for case-insensitive search
    content_lower = content.lower()
    search_term_lower = search_term.lower()
    
    # Find all occurrences
    results = []
    start = 0
    while True:
        index = content_lower.find(search_term_lower, start)
        if index == -1:  # No more occurrences
            break
            
        # Get surrounding context (50 characters before and after)
        context_start = max(0, index - 50)
        context_end = min(len(content), index + len(search_term) + 50)
        context = content[context_start:context_end]
        
        results.append(context)
        start = index + 1
        
    return results

# Example usage
if __name__ == "__main__":
    pdf_path = "biblia/agano-la-kale-suv.pdf"  # Replace with your PDF file path
    
    # Read entire PDF
    print("Reading PDF...")
    full_text = read_pdf(pdf_path)
    print("PDF Content:", full_text[:500], "...\n")  # Print first 500 characters
    
    # Search in PDF
    search_word = input("Enter the word to search: ")
    results = search_in_pdf(pdf_path, search_word)
    
    if results:
        print(f"\nFound {len(results)} matches:")
        for i, result in enumerate(results, 1):
            print(f"\nMatch {i}:")
            print("..." + result + "...")
    else:
        print("\nNo matches found.")
