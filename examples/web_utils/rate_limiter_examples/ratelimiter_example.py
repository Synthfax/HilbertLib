from hilbertlib.web_utils.rate_limiter import RateLimiter
import time

def example_rate_limiter():
    limiter = RateLimiter(rate_per_sec=2)  # max 2 calls per sec
    for i in range(5):
        limiter.wait()
        print(f"Request {i+1} at {time.strftime('%X')}")

example_rate_limiter()
