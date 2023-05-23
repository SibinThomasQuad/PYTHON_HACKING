from googlesearch import search

def automate_google_dorks(query, num_results):
    dorks = [f"{query} site:.com", f"{query} site:.org", f"{query} site:.gov"]  # Example dorks

    results = []
    for dork in dorks:
        print(f"Searching for dork: {dork}")
        for result in search(dork, num_results=num_results):
            results.append(result)

    return results

# Example usage:
dork_query = "inurl:sibin thomas"  # Specify your desired dork query
num_results = 10  # Specify the number of results you want to retrieve

dork_results = automate_google_dorks(dork_query, num_results)

# Print the results
print("Dork Results:")
for result in dork_results:
    print(result)
