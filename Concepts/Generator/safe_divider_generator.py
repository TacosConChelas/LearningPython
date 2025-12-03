"""
5) ------ Safe divider with exception handling
Write safe_divider() that repeatedly expects a tuple (a, b) sent to it. 
It should yield a / b when b is non‑zero, but if a ZeroDivisionError occurs 
it catches the exception and yields the string "inf" instead of propagating the error.
"""
def main():
    safe = safe_divider()
    next(safe)
    print(safe.send((2, 0)))
    print(safe.send((787, 7)))
    
def safe_divider():
    result_operation = None
    
    while True:
        tuple_ = yield result_operation
        if tuple_ is None:   break
        # a, b = tuple
        if tuple_[1] == 0:  result_operation = "Warning, b can't be equals to 0 -> ZeroDivisionError"
        else: result_operation = tuple_[0] / tuple_[1]

if __name__ == "__main__":
    main()