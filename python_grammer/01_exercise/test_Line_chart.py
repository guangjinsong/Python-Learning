# Python数据和Json数据的相互转化
# 导入json模块
import json

# 准备符合json格式要求的Python数据
data_python_before = [{"name": "admin", "age": 18}, {"name": "root", "age": 16}, {"name": "张三", "age": 19}]

# 通过json.dumps()方法把python方法转化为json数据
data_json = json.dumps(data_python_before)

# 通过json.loads()方法把json数据转化为python数据
data_python_after = json.loads(data_json)


# 基础折线图
# 导包, 导入Line功能构建折线图对象
from pyecharts.charts import Line

# 得到折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据
line.add_yaxis("GDP", [30, 20, 10])
# 生成图表
line.render()


