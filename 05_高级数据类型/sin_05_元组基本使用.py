info_tuple = ("张三",18,1.75,"张三")

# 1、取值和取索引
print(info_tuple[0])
# 已经知道数组的内容，希望知道该数据在元组中的索引
print(info_tuple.index("张三"))

# 2、统计次数
print(info_tuple.count("张三"))
# 2、统计元组中包含元素的个数
print(len(info_tuple))

print(info_tuple)