def error_retry(fun):
    print("Inside Deco")
    def wrap(*args,**kwargs):
        max_try = kwargs["max_try"]
        kwa = kwargs.pop("max_try")
        for attempt in range(max_try):
            try:
                print("Attempt {}".format(attempt + 1))
                return fun(*args,**kwa)
            except Exception as e:
                if attempt == max_try - 1:
                    raise e
                print("Attempt {} failed with error: {}".format(attempt + 1, e))
                continue
    return wrap

@error_retry
def divide(a,b , *args , **kwargs):
    return a/b

print(divide(10,0 , max_try=4))