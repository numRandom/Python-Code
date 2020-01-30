def measure():
    """测量温度和湿度"""

    print("测量前……")
    tmp = 39
    wetness = 50
    print("测量结束……")

    # 元组 - 可以半酣多个数据，因此可以使用元组让函数一次返回多个值
    # return (tmp,wetness)
    # 如果函数返回的数据类型是元组，小括号可以省略
    return tmp,wetness

# result 元组
result = measure()
print(result)

# 若需要单独处理温度或湿度
print(result[0])
print(result[1])

# 如果函数返回值类型是元组，同时希望单独的处理元组中的元素
# 可以使用多个变量，一次接收函数的返回结果
# 注意：使用多个变量接收结果是，变量的个数应该和元组中元素的个数保持一致
# 在变量名前用 gl 一般表示全局变量
gl_tmp , gl_wetness = measure()
print(gl_tmp)
print(gl_wetness)