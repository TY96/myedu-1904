A = '亚索'
def x1():
    b = '洛克'
    print(A+b)
def x2 ():
    global A
    A = '球女+潘森'
    print(A)
if __name__ == '__main__':
    x1()
    x2()