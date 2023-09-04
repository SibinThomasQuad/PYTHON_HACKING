import sys
import mitmproxy.http
from mitmproxy import ctx

class RequestLogger:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        print("Request URL:", flow.request.url)
        print("Request method:", flow.request.method)
        print("Request headers:", flow.request.headers)
        print("Request content:", flow.request.content)

        # Log request cookies
        if flow.request.cookies:
            print("Request Cookies:")
            for name, value in flow.request.cookies.items():
                print(f"  {name}: {value}")

    def response(self, flow: mitmproxy.http.HTTPFlow):
        print("Response Status Code:", flow.response.status_code)
        print("Response headers:", flow.response.headers)

        # Check if the response content type is HTML, JavaScript, or CSS
        content_type = flow.response.headers.get("content-type", "")
        if "text/html" not in content_type and not content_type.endswith(("javascript", "css")):
            print("Response content:")
            print(flow.response.text)

        # Log response cookies
        if flow.response.cookies:
            print("Response Cookies:")
            for name, value in flow.response.cookies.items():
                print(f"  {name}: {value}")

addons = [
    RequestLogger()
]

if __name__ == "__main__":
    from mitmproxy.tools.main import mitmdump
    mitmdump(["-s", __file__] + sys.argv[1:])
