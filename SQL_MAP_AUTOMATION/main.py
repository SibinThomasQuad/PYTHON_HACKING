import subprocess

def run_sqlmap(target_url, parameters):
    try:
        # Build the SQLMap command
        sqlmap_cmd = ["sqlmap", "-u", target_url]

        # Add other parameters such as cookies, headers, etc., based on your needs
        # Example: sqlmap_cmd += ["--cookie", "SESSIONID=12345"]

        # Add common parameters for GET and POST requests
        sqlmap_cmd += ["--batch", "--random-agent", "--level=5", "--risk=3"]

        # Add parameters for POST request
        if parameters.get('method') == 'POST':
            sqlmap_cmd += ["--data", parameters.get('data')]

        # Run SQLMap
        subprocess.run(sqlmap_cmd, check=True)

    except subprocess.CalledProcessError as e:
        print(f"SQLMap process failed with error: {e}")

if __name__ == "__main__":
    # Replace with your target URL and parameters
    target_url = "http://example.com/login"
    post_parameters = {'method': 'POST', 'data': 'username=test&password=test'}

    # Run SQLMap
    run_sqlmap(target_url, post_parameters)
