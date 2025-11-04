"""
7)-------- Class-method aware logger
Design class_logger that can be applied to any method defined inside a class, 
including @classmethod and @staticmethod. When the method runs, it should 
print <ClassName>.<method_name> called. Use func.__qualname__ (which includes the class name) 
and remember that the first argument may be self or cls.
"""