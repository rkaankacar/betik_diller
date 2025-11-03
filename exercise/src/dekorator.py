from functools import wraps
import time
import csv

def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        t0= time.perf_counter() # 0.andaki time
        result=func(*args,**kwargs)
        total_time=time.perf_counter()-t0
        print("total_time: ", total_time)
        return result
    return wrapper


def required_column(requireds: set[str]):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            if requireds:
                
                rows = kwargs.get("rows", None)
                if rows is None and args:
                    rows = args[0]

                if not rows:
                    raise ValueError("Boş veri seti")

                try:
                    keys = set(rows[0].keys())
                except Exception:
                    raise TypeError("rows, sözlüklerden oluşan bir liste olmalı")

                missing = set(requireds) - keys
                if missing:
                    raise ValueError(f"Eksik kolonlar: {missing}")

            return func(*args, **kwargs)
        return wrapper
    if callable(requireds):
        func = requireds
        requireds = None
        return decorator(func)

    return decorator
        
                