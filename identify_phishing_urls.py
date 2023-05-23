import re

def is_phishing_site(url):
    # Check for suspicious keywords in the URL
    suspicious_keywords = ['login', 'signin', 'verify', 'banking', 'secure', 'update']
    for keyword in suspicious_keywords:
        if keyword in url:
            return True
    
    # Check for URL structure patterns often used in phishing sites
    url_pattern = r"https?://([^\s/$.?#].[^\s]*)"
    match = re.search(url_pattern, url)
    if match:
        domain = match.group(1)
        if len(domain.split(".")) <= 1:  # Phishing sites often use fake domains like "paypal.something.com"
            return True
    
    return False

# Example usage:
urls = [
    "https://www.google.com",
    "https://www.paypal-login.com",
    "https://www.banking-verification.com",
    "https://www.openai.com",
    "https://www.secure-update-account.com"
]

for url in urls:
    if is_phishing_site(url):
        print(f"{url} is a phishing site.")
    else:
        print(f"{url} is not a phishing site.")
