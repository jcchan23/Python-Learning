import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("cube Numbers",fontsize = 24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("cube of Value",fontsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0,5100,0,5100**3])
plt.show()