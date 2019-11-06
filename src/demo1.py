# ** 表示乘方

a = 3 ** 3

print(a)

a = 0
print(a)

# 列表

l = [1, 2, 3, 4, 5]

# 获取长度
len(l)

# 获取第一个元素
l[0]

l[len(l) - 1] = 99

l= l[:-1]

print(l)

# 获取索引为1的元素到最后一个元素
l = l[1:]

l = l[:3]

# 切片获取 0到2的元素，不包含2的索引
l = l[0:2]

print(l)



# 字典

me = {'height':180}

height =me['height']

me['weight']=70

print(me)

# boolean 使用True False
# if
go = False

if go:
    print("go...")
else:
    print("I'm not go...")
    print("I'm hungry...")


# for

for i in [1,2,3]:
    print(i)


# function

def hello(str):
    print("Hello World! "+str)

hello(" road")

