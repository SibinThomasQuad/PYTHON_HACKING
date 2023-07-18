import mitmproxy.http
import sys


class RequestLogger:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        print("Request URL:", flow.request.url)
        print("Request method:", flow.request.method)
        print("Request headers:", flow.request.headers)
        print("Request content:", flow.request.content)

addons = [
    RequestLogger()
] 

if __name__ == "__main__":
    from mitmproxy.tools.main import mitmdump
    mitmdump(["-s", __file__] + sys.argv[1:])
