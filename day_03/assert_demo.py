def assert_str():
    A = '我'
    B = '我是'
    for i range (2):
    try:
        # assert A == B
        assert A in B
        assert B >= A
    except:
        print('断言失败')

if __name__ == '__main__':
    assert_str()
