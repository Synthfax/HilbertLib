from hilbertlib.web_utils.api_handler import APIHandler

def example_api_handler():
    api = APIHandler("https://httpbin.org")
    get_resp = api.call_api("/get", method="GET", payload={"key": "value"})
    print("GET status:", get_resp.status_code)
    print("GET JSON:", get_resp.json())
    
    post_resp = api.call_api("/post", method="POST", payload={"foo": "bar"})
    print("POST status:", post_resp.status_code)
    print("POST JSON:", post_resp.json())

example_api_handler()
