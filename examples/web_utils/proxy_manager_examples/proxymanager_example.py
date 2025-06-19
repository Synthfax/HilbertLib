from hilbertlib.web_utils.proxy_manager import ProxyManager

def example_proxy_manager():
    proxies = [
        "http://proxy1.example.com:8080",
        "http://proxy2.example.com:8080",
        "http://proxy3.example.com:8080"
    ]
    manager = ProxyManager(proxies)
    print("Random proxy:", manager.get_random_proxy())
    print("Rotate proxy 1:", manager.rotate_proxy())
    print("Rotate proxy 2:", manager.rotate_proxy())
    print("Rotate proxy 3:", manager.rotate_proxy())
    print("Rotate proxy 4 (wraps around):", manager.rotate_proxy())

example_proxy_manager()
