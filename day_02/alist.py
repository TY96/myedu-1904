alist = ['我又不乱来',156,12,15,23.3,1,'dsad','dsadef']
B = [111,'222',984,411]
def list_select ():
    print (alist[2])
    print(alist[-3])
    print(alist[3:4])
    print (alist[5:])
    print (alist[:6])


def list_delete():
    alist.pop(-2)
    print (alist)


def list_add ():
    blist = [789,456,'147',258,'qwe']
    # blist.append(alist)
    a=blist.extend(alist)
    print (blist)

def list_updata():
    new = [23,54,42,'62',5]
    new [1] = 22
    new[3] = '我又不乱来'

def list_paixu():
    x = [6,5,8,4,1]
    x.sort()
    y = [3,4,1,23]
    y.sort(reverse=True)
    print(x)
    print(y)

def list_quchong ():
    T = [2,2,444,34,34,21,33,33]
    T= list(set (T))
    T.sort(reverse=True)
    print(T)

def list_homework():
    list_work = [121,56,15,33,2]
    print (list_work[2])
    print(list_work[1:4])
    list_work.pop(3)
    print(list_work)
    list_work.append(2)
    print(list_work)
    list_work.append(2333)
    print(list_work)
    list_work[0] ='5'
    print(list_work)
    print(len(list_work))
    list_work.


if __name__ == '__main__':
    # list_delete()
    # list_add()
    # list_paixu()
    # list_quchong()
    list_homework()









