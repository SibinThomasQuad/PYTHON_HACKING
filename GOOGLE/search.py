import requests
from bs4 import BeautifulSoup
from googlesearch import search

# Function to perform a Google search and retrieve links
def google_search(query, num_results=10):
    search_results = []

    # Perform the Google search
    for result in search(query, num_results=num_results):
        search_results.append(result)

    return search_results

# Main function
if __name__ == "__main__":
    # Input the search query and number of results from the user
    query = input("Enter your search query: ")
    num_results = int(input("Enter the number of results to retrieve: "))

    # Perform the Google search
    search_results = google_search(query, num_results)

    # Display the search results
    print("Search Results:")
    for i, result in enumerate(search_results, start=1):
        print(f"{i}. {result}")

    # Optionally, you can parse the HTML content of each search result link
    # to extract more information if needed.
    for i, result_link in enumerate(search_results, start=1):
        try:
            response = requests.get(result_link)
            soup = BeautifulSoup(response.text, "html.parser")
            # You can parse and extract information from the HTML here
        except Exception as e:
            print(f"Error processing result {i}: {str(e)}")
