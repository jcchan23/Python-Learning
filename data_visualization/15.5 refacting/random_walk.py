from random import choice

class Randomwalk():
    """一个生成随机漫步数据的类"""

    def __init__(self,num_points = 5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，知道列表达到指定的长度
        while len(self.x_values) < self.num_points:

            # 决定前进的方向以及沿这个方向前进的距离
            # x_direction =  choice([1,-1])
            # x_distance = choice([0,1,2,3,4])
            # x_step = x_direction * x_distance
            x_step = self.get_step()

            # y_direction =  choice([1,-1])
            # y_distance = choice([0,1,2,3,4])
            # y_step = y_direction * y_distance
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            
            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        """决定前进的方向以及沿这个方向前进的距离"""
        
        direction = choice([1,-1])
        distance = choice(list(range(0,9)))
        self.step = direction * distance
        return self.step



