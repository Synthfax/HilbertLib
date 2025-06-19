import time
import threading

class RateLimiter:
    def __init__(self, rate_per_sec):
        self.rate = rate_per_sec
        self.lock = threading.Lock()
        self.last_call = 0

    def wait(self):
        with self.lock:
            now = time.time()
            wait_time = 1.0 / self.rate - (now - self.last_call)
            if wait_time > 0:
                time.sleep(wait_time)
            self.last_call = time.time()