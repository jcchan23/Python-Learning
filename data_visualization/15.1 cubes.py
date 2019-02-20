import matplotlib.pyplot as plt

x_values = list(range(1,6))
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,edgecolor='none',s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("cube Numbers",fontsize = 24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("cube of Value",fontsize=14)

# 设置每个坐标轴的取值范围
#plt.axis([0,1100,0,1100000])

# 设置刻度标记的大小
plt.tick_params(axis='both',which = 'major',labelsize=14)

plt.show()

# 打印成图片
#plt.savefig('squares_plot.png',bbox_inches='tight')