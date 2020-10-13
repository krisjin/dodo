str1 = "我是谁"

strEncode = str1.encode("UTF-8")

print(strEncode.decode("UTF-8"))

count = 0

while True:
    print("count :", count)
    count += 1
    if (count == 10):
        break

print("第二种循环")
count = 0
for count in range(0, 10, 2):
    print("count", count)

print("第三种循环")
count = 0
for count in range(0, 10):
    print("count", count)

print("******************")

for i in range(0, 10):

    if i < 5:
        print("i<5 ->", i)
    else:
        print("else ->", i)
