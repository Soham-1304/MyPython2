28. **Decorators**
```python
def log_function_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args}, kwargs {kwargs}")
        return func(*args, **kwargs)
    return wrapper