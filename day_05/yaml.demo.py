import yaml
if __name__ == '__main__':
    A = open('test.yaml',encoding='utf-8')
    B = yaml.load(A, Loader=yaml.Loader)
    print(B)