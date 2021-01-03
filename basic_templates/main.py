
class Dec():
    def hello(func):
        print("has been runing in hello")
        func()
        print("func has been called")
        return "success"

@Dec.hello
def test():
    print("this is func with decorator success")

#test = newdecorator(test)
test()
