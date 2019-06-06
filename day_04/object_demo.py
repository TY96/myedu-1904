class game (object):
    def __init__(self,name,type,age):
        self.name = name
        self.type=type
        self.age = age

    def play(self):
        print(self.name+'在上网')

    def sleep(self):
        print(self.name+'做梦')


    def info(self):
        print('%s %s %s'%(self.name,self.age,self.type))


class Tester(game):

    def __init__(self,name,type,age,city):
        self.name = name
        self.type = type
        self.age = age
        self.city = city
        print('%s %s %s %s'%(self.name,self.type,self.age,self.city))

    def sleep(self):
        print(self.name+'上网打豆豆')





if __name__ == '__main__':
    tester = Tester('杰仔', '男', '16','香港富豪')
    tester.sleep()
