def hello(func):
    print("Hello")
    return func()


@hello
def word():
    print("Word")


word
