import os

# built-in args
print('__file__ : ', __file__)
print('__name__ : ', __name__)

# current (abs) path
print('current abs path : ', os.getcwd())
print('current path : ', os.curdir)
print('current abs path : ', os.path.abspath('.'))

# parent (abs) path
print('parent path : ', os.path.dirname(os.getcwd()))
print('parent path : ', os.path.abspath('..'))
print('parent path : ', os.path.abspath(os.path.join(os.getcwd(), "../")))

# judge whether directory exist
print(os.path.join(os.getcwd(), '../torch-tutorial/utils'))
print(os.path.exists(os.path.join(os.getcwd(), '../torch-tutorial/utils')))

# 文件操作判断
path_1 = './utilss'
print(os.path.abspath(path_1))
path_2 = 'C:/Users/tashuangjie/Desktop/Code/torch-tutorial/utilss'
if not os.path.exists(path_1) and not os.path.exists(path_2):
    print('Dir not exist.')
else:
    print('Dir exists.')