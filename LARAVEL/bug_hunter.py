import requests

def is_downloadable(url):
    try:
        response = requests.head(url, allow_redirects=True)
        if 'content-disposition' in response.headers:
            content_disposition = response.headers['content-disposition']
            if 'attachment' in content_disposition.lower():
                return True
        return False
    except requests.exceptions.RequestException:
        return False
    
def find_matching_words(word_list, large_string):
    matched_words = []
    for word in word_list:
        if word in large_string:
            matched_words.append(word)
    return matched_words

def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.text
    except requests.exceptions.RequestException:
        return None

if __name__ == "__main__":
    base_url = input("Enter the base URL: ")
    words = [
        ".env",
        "/storage",
        "/public",
        "/storage/framework/sessions/",
        "/storage/framework/",
        "/storage/logs/",
        "/storage/logs/laravel.log"

        # Add more words here
    ]
    
    for word in words:
        print("="*100)
        full_url = f"{base_url}/{word}"
        content = fetch_content(full_url)
        if is_downloadable(full_url):
            print("The URL points to a downloadable file.")
        else:
            print("The URL does not point to a downloadable file.")
        if content is None:
            print(f"URL '{full_url}' is inaccessible.")
        elif "404 Not Found" in content or "403 Forbidden" in content:
            print(f"URL '{full_url}' returned a 404 or forbidden status.")
        else:
            print(f"Contents of URL '{full_url}':")
            if "Index of /storage" in content:
                print(f"'{full_url}' Is a directory")
            else:
                word_list = ["Error", "SQL", "Syntax", ".php"]
                large_string = content

                matched_words = find_matching_words(word_list, large_string)

                if matched_words:
                    print("[Error page ditected ]Matched words:", matched_words)
                else:
                    print(content)
    print("="*100)
                
