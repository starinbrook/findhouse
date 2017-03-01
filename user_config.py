# coding:UTF-8

"""
用户自定义配置
"""

setting = {}

# 区域
# dongcheng: 东城
# xicheng: 西城
# chaoyang: 朝阳
# haidian: 海淀
# fengtai: 丰台
# shijingshan: 石景山
# tongzhou: 通州
# changping: 昌平
# daxing: 大兴
# yizhuangkaifaqu: 亦庄开发区
# shunyi: 顺义
# fangshan: 房山
# mentougou: 门头沟
# pinggu: 平谷
# huairou: 怀柔
# miyun: 密云
# yanqing: 延庆
# yanjiao: 燕郊
setting['region'] = "daxing" # 区域和地铁线只可以设置一个

# 地铁线
# li647: 1号线
# li648: 2号线
# li656: 4号线
# li649: 5号线
# li46107350: 6号线
# li46537785: 7号线
# li659: 8号线
# li43145267: 9号线
# li651: 10号线
# li652: 13号线
# li46461179: 14号线（东段）
# li1110790465974155: 14号线（西段）
# li43143633: 15号线
# li1116796246117001: 16号线
# li653: 八通线
# li43144847: 亦庄线
# li43144993: 昌平线
# li43145111: 房山线
# li654: 机场线
setting['subwayline'] = "" # 区域和地铁线只可以设置一个

# 售价
# p1：200万以下
# p2: 200-250万
# p3: 250-300万
# p4: 300-400万
# p5: 400-500万
# p6: 500-800万
# p7: 800-1000万
# p8: 1000万以上
setting['price'] = "p2" # 可组合，如p1p2

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

# 用途
# sf1: 普通住宅
# sf2: 商业类
# sf3: 别墅
# sf4: 四合院
# sf5: 其他
setting['purpose'] = "sf1"

# 楼层
# lc1: 低楼层
# lc2: 中楼层
# lc3: 高楼层
# lc4: 底层
# lc5: 顶层
setting['floor'] = "lc1lc2lc3"

# 朝向
# f1: 朝东
# f2: 朝南
# f3: 朝西
# f4: 朝北
# f5: 南北
setting['orientation'] = ""

# 楼龄
# y1: 5年以内
# y2: 10年以内
# y3: 15年以内
# y4: 20年以内
# y5: 20年以上
setting['years'] = ""

# 类型
# bt1: 塔楼
# bt2: 板楼
# bt3: 板塔结合
setting['type'] = ""

# 电梯
# ie1: 无电梯
# ie2: 有电梯
setting['elevator'] = ""

# 装修
# de1: 精装修
# de2: 普通装修
# de3: 毛坯房
setting['decoration'] = ""

# 供暖
# hy1: 集体供暖
# hy2: 自供暖
setting['heating'] = "hy1"


# 页数
setting['page_number'] = 1

# 结果产出文件名称
setting['output_fname'] = "find_house_zhuyca0228.txt"