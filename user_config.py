# coding:UTF-8

"""
用户自定义配置
"""

setting = {}

# 售价
# p1：200万以下
# p2: 200-250万
# p3: 250-300万
# p4: 300-400万
# p5: 400-500万
# p6: 500-800万
# p7: 800-1000万
# p8: 1000万以上
setting['price'] = "p1" # 可组合，如p1p2

# 面积
# a1: 50平以下
# a2: 50-70平
# a3: 70-90平
# a4: 90-110平
# a5: 110-130平
# a6: 130-150平
# a7: 150-200平
# a8: 200平以上
setting['area'] = ""

# 房型
# l1: 一室
# l2: 二室
# l3: 三室
# l4: 四室
setting['layout'] = ""

# 页数
setting['page_number'] = 5

# 结果产出文件名称
setting['output_fname'] = "find_house_zhuyca0228.txt"