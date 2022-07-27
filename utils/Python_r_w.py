save_path = './jsons/write.txt'

print('Begin writing!')
with open(save_path, 'w', encoding='utf-8') as f: # "w" 覆盖写入模式， "a": 追加写入模式
    for i in range(3):
        f.write(f"{i}\n") # wtire must be str!
f.close()
print('Writing finished!')

