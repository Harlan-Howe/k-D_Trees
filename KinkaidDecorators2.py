import logging
import time
from typing import Callable, Any
import functools
import traceback


def log_start_stop_method(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Based on an example by Arjan of arjancodes.com: https://www.youtube.com/watch?v=QH5fw9kxDQA
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        indent = "\t"*len(traceback.extract_stack())
        logging.info(f"{indent}Starting method {func.__name__}{("self",)+args[1:]}")
        value = func(*args, **kwargs)
        logging.info(f"{indent}Finishing method: {func.__name__}")
        return value
    return wrapper


def log_duration(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Based on an example from https://www.w3resource.com/python-exercises/decorator/python-decorator-exercise-2.php
    """
    def wrapper2(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        value = func(*args, **kwargs)
        duration = time.perf_counter() - start
        logging.info(f"{func.__name__} took {duration:0.6f} seconds.")
        return value
    return wrapper2
