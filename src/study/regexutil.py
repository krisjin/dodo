import re

# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if matchObj:
#     print
#     "matchObj.group() : ", matchObj.group()
#     print
#     "matchObj.group(1) : ", matchObj.group(1)
#     print
#     "matchObj.group(2) : ", matchObj.group(2)
# else:
#     print
#     "No match!!"


str = '在华为商城即日起至2020年12月11日APP购买指定商品，且同一订单中只有参与活动的商品，在支付时选择银联分期，即日起至2020年12月11日,使用龙卡信用卡分期支付，按期数每月还款，可享受满3000元减100元、满2000元减50元的优惠'
# str = '在华为商城即日起至2020年12月11日APP购买指定商品，且同一订单中只有参与活动的商品，在支付时选择银联分期，即日起至2020年12月11日,使用龙卡信用卡分期支付，按期数每月还款，可享受满3000元减100元、满2000元减50元的优惠'

r1 = r'即日.[到|起|起至|起到|至|到至]\d{4}年\d{1,2}月\d{1,2}日'

p = re.compile(r1)

ret = ''
allDate = p.findall(str)
for d in allDate:
    ret = d + ',' + ret

print(ret)

# line = "Cats are smarter11 22 than dogs";
#
# matchObj = re.findall(r'\d+', line)
# if matchObj:
#     print
#     "match --> matchObj.group() : ", matchObj.group()
# else:
#     print("No match!!")

# pattern = re.compile(r'\d+')  # 查找数字
# result1 = pattern.findall('runoob 123 google 456')
# result2 = pattern.findall('run88oob21235google456')
#
# print(result1)
# print(result2)


# print('Test: 111010-12345')
# a = '^(\d{3})-(\d{3,8})$'
# m = re.match(a, '010-144')
#
#
#
# print(m.group(1))
# print(m.group(2))
#
#
# t = '19:05:3044'
# print('Test:', t)
# # m = re.match(r'(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])', t)
# m = re.match(r'(0[0-9]|1[0-9]|2[0-3]|[0-9])', t)
#
# print(m.groups())
