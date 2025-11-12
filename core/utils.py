import time, functools

def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except AssertionError as e:
                    print(f"❌ Retry {attempt} failed: {e}")
                    time.sleep(1)
            raise AssertionError(f"All {times} retries failed")
        return wrapper
    return decorator
