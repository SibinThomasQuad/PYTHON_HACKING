import re
import requests
from bs4 import BeautifulSoup
def label():
    label_text = '''

░█████╗░██████╗░██╗░░░░░░██╗░░██╗██╗░░░██╗███╗░░██╗████████╗███████╗██████╗░
██╔══██╗██╔══██╗██║░░░░░░██║░░██║██║░░░██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗
███████║██████╔╝██║█████╗███████║██║░░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝
██╔══██║██╔═══╝░██║╚════╝██╔══██║██║░░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗
██║░░██║██║░░░░░██║░░░░░░██║░░██║╚██████╔╝██║░╚███║░░░██║░░░███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
'''
    print(label_text)
    print("-"*100)
    print("Tool to identify the thirdparty urls and apis in a website")
    print("-"*100)

def find_third_party_apis(url):
    # Fetch the HTML content of the website
    response = requests.get(url)
    html_content = response.text

    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find third-party APIs in HTML attributes
    html_apis = []
    for tag in soup.find_all():
        for attr_name, attr_value in tag.attrs.items():
            if re.match(r'^https?://', str(attr_value)):
                html_apis.append(attr_value)

    # Find third-party APIs in JavaScript code
    js_apis = re.findall(r'https?://[^\s/$.?#].[^\s]*', html_content)

    # Combine and deduplicate API references
    all_apis = list(set(html_apis + js_apis))

    return all_apis

if __name__ == "__main__":
    try:
        label()
        website_url = input("Enter the website URL: ")
        third_party_apis = find_third_party_apis(website_url)

        print("Third-party APIs:")
        for api in third_party_apis:
            print("[+] "+str(api))
    except:
        print("[@@] Something went wrong (EXITING..)")
