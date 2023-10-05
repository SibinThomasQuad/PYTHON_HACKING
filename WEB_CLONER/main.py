from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

app = FastAPI()

@app.get('/embed-website', response_class=HTMLResponse)
async def embed_website():
    source_url = 'http://kingsgames.in/login '  # Replace with the actual source URL

    try:
        # Fetch the content from the source URL
        response = requests.get(source_url)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Update relative URLs to absolute URLs
            base_url = urlparse(source_url)
            for tag in soup.find_all(['a', 'img', 'link', 'script'], href=True):
                tag['href'] = urljoin(base_url.geturl(), tag['href'])
            for tag in soup.find_all(['img', 'script'], src=True):
                tag['src'] = urljoin(base_url.geturl(), tag['src'])

            # Pass the modified HTML content as response
            return soup.prettify()
        else:
            raise HTTPException(status_code=500, detail='Failed to fetch content from the source URL')
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=500, detail='Failed to fetch content from the source URL')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
