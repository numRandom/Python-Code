# 使用 多个键值对，存储 描述一个 物体 的相关信息——描述更复杂的数据信息
# 将 多个字典 放在 一个列表 中，再进行遍历

card_list = [
    {"name":"张三","qq":"123456","phone":"110"},
    {"name":"李四","qq":"654321","phone":"119"}
]

for card_info in card_list:
    print(card_info)