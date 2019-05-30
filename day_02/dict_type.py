import json
a = [21,3,1,32,1,4,5]
X = {'username': "admin", 'password': "123456"}
def dict_select ():
       print (X['username'])
       print (X['password'])
def dict_updata ():
    X['username'] = '我又不乱来'
    print(X['username'])
    X['password'] = 147258
    print(X['password'])
def dict_delete():
    X.pop('username')
    X.pop('password')
    print(X)
def dict_add ():
    X['city'] = '重庆'
    Y ={'age' :[20],'class':(1903,1904)}

    X.update(Y)
    print(X)
def dict_zhuanhuan():
    pass
    # print(type(X))
    # dict_str = json.dumps(X)
    # print(type(dict_str))
    # str_dict = '{"username": "你的", "password": "123456"}'
    # A = json.loads(str_dict)
    # print(type(A))

low={"class":"231","course":"yuwen"}
low1={"class":"15231","course":"yingyu"}
def work():
    print(low["class"])
    low.pop("class")
    low["城市"] = "重庆"
    low["course"]="shuxue"
    low.update(low1)

    print(low)


if __name__ == '__main__':
    # dict_select()
    # dict_updata()
    # dict_delete()
    # dict_add()
    # dict_zhuanhuan()
    work()