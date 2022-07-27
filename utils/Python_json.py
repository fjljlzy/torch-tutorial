import json
import addict
from cv2 import add
from imageio import save
from matplotlib.font_manager import json_dump

# loads：把字符串变成数据类型
# dumps：把数据类型变成存储可用的字符串
print('*'*20)

dic = {"name": "joey", "age": 24}
print(dic)
print(type(dic))

json_str = json.dumps(dic)
print(json_str)
print(type(json_str))

print('begin json.loads()')
print(json.loads(json_str))


print('*'*20)

# load：加载文件（open），把文件中的字符串变成数据类型 
# (不推荐load，load需要文件中有且仅有一个字符型的数据类型，推荐用loads，反正越是处理字符串
# dump：把数据类型变成字符串，然后写入到文件中

save_path = './jsons/write.json'

# 用dump先写入到一个json文件中，再打开
print('write something into:', save_path)
with open(save_path, "w") as f: # 将会覆盖之前的文件， "a"为追加模式
    print('写入开始：')
    json.dump(dic, f)
    print("写入完成...")
f.close()

# 打开刚刚写入的文件，使用 load 还是 loads？ 
with open(save_path, 'r', encoding='utf-8') as f:
    print('读入开始')
    
    # 使用load
    d = json.load(f)
    d = addict.Dict(d)
    print('读入完成')
    print(d)
    print("d.name:", d.name)
    print("d.age:", d.age)

    # 使用loads
    for row in f:
        print('用loads读入')
        d = json.loads(row)
        d = addict.Dict(d)
        print('读入完成')
        print(d)
        print("d.name:", d.name)
        print("d.age:", d.age)
