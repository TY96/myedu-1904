# # print ('hello world')
# def test_1 ():
#     A = 20
#     B = 10.3
#     print(type(A))
#     print(type(B))
#     print ('%s%s'%(A,B))
#     C = '%s%s'%(A,B)
#     print(type(C))
#
#
#
#
#
#
#
# def X (m,n):
#     print(m+n)
#     return m+n
#
#
# def _day():
#     pass
#     # w = '我又不乱来'
#     # W = 233333
#     # print ('%s%s'%(w,W))
#     # print (type(str(W)))
#     # print(str(W)+w)
#     # print('%s%s'%(w,W))
# ls = {'yifu':'naike','shouji':'xiaomi'}
# cd = {'qiabi':'wenju'}
# A = [1,12,12,12,4,1,2,5,2]
# import json
# def lianxi():
#     # A.sort(reverse=True)
#     # B=len(A)
#     # print(B)
#     # X = [2,3,3,31,3,4,56,4,1,2]
#     # Y = list(set(X))
#     # print(type(Y))
#     ls['naike'] = 'chenshan'
#     print(ls)

#
# X = [6, 7, 8, 5]
# Y = [1, 3, 43, 1]
# def this():
#     X.append(Y)
#     print(X)
# 求两个数之间的偶数和

# def he(x,y):
#     a = 0
#     if x<y:
#         for i in range(x,y):
#             if  i%2 ==0:
#                 a = a+i
#     elif x>y:
#         for i in range(y,x):
#             if  i%2 ==0:
#                 a = a+i
#     else :
#         'x=y'
#     print(a)

# def sum_demo1(a,b):
#     sum = 0
#     if a<b:
#         for i in range(a,b):
#             if i%2 ==0:
#                 sum = sum+i
#     elif a>b:
#         for i in range(b,a):
#             if i %2 ==0:
#                 sum = sum+i
#     else:
#         print('a和 b 相等')
#
#     print(sum)


# class 声明一个类
class Human(object):
    def __init__(self,teacher,student,father):
        self.teacher=teacher
        self.student=student
        self.father=father
    def study(self):
        print(self.student+'恰饭')
    def ALL(self):
        print('谁是%s, 谁是%s, 谁是%s, 谁是%s'%(self.student,self.father,self.teacher))

class more(Human):
    def __init__(self,teacher,student,father,mother):
        self.teacher = teacher
        self.student = student
        self.father = father
        self.mother = mother
    def surf_internet(self):
        print(self.student+'在上网')




if __name__ == '__main__':

    # people = Human('张三', '李四', '赵二','小张')
    # people.ALL()
    # people.study()
    MORE = more('张三', '李四', '赵二', '小张')
    MORE.surf_internet()