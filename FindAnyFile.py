from googlesearch import search

def find_files(query, file_types):
    """
    Searches for files online using Google Search.

    Args:
        query: The search terms for finding files.
        file_types: List of file types to search for.

    Returns:
        A dictionary where keys are file types and values are lists of URLs containing potentially relevant files.
    """
    file_links = {}
    for file_type in file_types:
        search_term = query + f" filetype:{file_type}"
        results = search(search_term)
        file_links[file_type] = results
    return file_links

def main():
    """
    Prompts the user for a search query and displays results for various file formats.
    """
    query = input("Enter your search query for files: ")
    file_types = ['txt', 'bin', 'asp', 'doc', 'pdf', 'exif', 'xls', 'xlsx', 'xml', 'csv', 'html', 'docx', 'msg', 'json', 'log', 'gdoc']  # Add more file types as needed
    try:
        file_links = find_files(query, file_types)
        for file_type, links in file_links.items():
            if links:
                print(f"Found {file_type.upper()} files:")
                for link in links:
                    print(link)
            else:
                print(f"No {file_type.upper()} files found for your query.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
