import requests

# Define a function to traverse the website URL using a word list
def traverse_url_with_wordlist(url, wordlist_path):
    # Load the word list from the file
    with open(wordlist_path) as f:
        wordlist = f.read().splitlines()

    # Iterate over the words in the word list
    for word in wordlist:
        # Build the full URL path to the directory
        full_url = url + '/' + word
        # Send a GET request to the URL
        response = requests.get(full_url)
        # Check if the response was successful
        if response.status_code == 200:
            print('Directory found:', full_url)
        else:
            print('Directory not found:', full_url)

# Test the function with a sample URL and word list
traverse_url_with_wordlist('https://www.example.com', 'wordlist.txt')
