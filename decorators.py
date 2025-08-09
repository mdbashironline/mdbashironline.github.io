def announce(f):
    def wrapper():
        print("About to execute the function...")
        f()
        print("Done executing the function.")
    return wrapper

@announce
def hello():
    print("Hello, world!")
hello()
