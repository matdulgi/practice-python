class Hello:
    def hello(self):
        print('hello')

    def __enter__(self):
        print('enter')
        return self

    # def __end__():
        # print('end')
    def __exit__(self, type, value, traceback):
        print('exit')
        # self.close()
        del self

with Hello() as h:
    h.hello()
    
print('finish')
