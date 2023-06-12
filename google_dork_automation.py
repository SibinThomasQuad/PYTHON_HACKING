from googlesearch import search

def google_search(query, num_results):
    search_results = search(query, num_results=num_results, lang='en')
    for result in search_results:
        print(str(result))


query = "?intitle:index.of? xlx mail"
num_results = 10

google_search(query, num_results)
