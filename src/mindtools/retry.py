import time
from functools import wraps


def retry(attempts: int = 3, delay: float = 0.0, exceptions=(Exception,)):
    """Retry a function when one of the specified exceptions is raised.

    Args:
        attempts: Total number of attempts, including the first call.
        delay: Seconds to wait between attempts.
        exceptions: Exception type or tuple of exception types to catch.
    """
    if attempts < 1:
        raise ValueError("attempts must be at least 1")
    if delay < 0:
        raise ValueError("delay cannot be negative")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None

            for attempt in range(attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as error:
                    last_error = error
                    if attempt < attempts - 1 and delay:
                        time.sleep(delay)

            raise last_error

        return wrapper

    return decorator
