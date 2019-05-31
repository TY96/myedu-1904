# def lianxi():
#     a = open ('zuoye.txt','w+')
#
#     a.write('决战到天亮')
#
# def  lianxi2():
#     b = open('葵花宝典.log','a+')
#     b.write('欲练神功,必先自宫\n')
#
# def lianxi3():
#     c = open('葵花宝典.log','r')
#     print(c.readline())

def jiujiu():
    for i in range (1,10):
        a = i+1
        for a in range(1,a):
            print('%s * %s = %s'%(a,i,a*i),end=('  '))
        print('')

# def shiyan ():
#     for i in range(1, 10):
#         x = i + 1
#         for j in range(1, x):
#             print('%s * %s = %s' % (j, i, j * i), end='   ')
#         print('')




if __name__ == '__main__':
    # jiujiu()
    jiujiu()