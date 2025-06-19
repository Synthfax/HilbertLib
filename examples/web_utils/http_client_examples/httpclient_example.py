from hilbertlib.web_utils.http_client import HttpClient

def example_http_client():
    client = HttpClient(retries=2, backoff_factor=0.1)
    response = client.get("https://httpbin.org/get", params={"test": "123"})
    print("Status Code:", response.status_code)
    print("JSON Response:", response.json())

example_http_client()
