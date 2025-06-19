import random

class ProxyManager:
    def __init__(self, proxies):
        self.proxies = proxies
        self.index = 0

    def get_random_proxy(self):
        return random.choice(self.proxies)

    def rotate_proxy(self):
        proxy = self.proxies[self.index % len(self.proxies)]
        self.index += 1
        return proxy