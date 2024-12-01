def to_lower(function):
    def wrapper():
        func_val = function()
        lower_str = func_val.lower()
        print(lower_str)
        return lower_str
    return wrapper

def split_val(function):
    def wrapper():
        func_val = function()
        splitted = func_val.split()
        return splitted
    return wrapper
    
@split_val
@to_lower
def hello():
    return "Hellow World!"
        