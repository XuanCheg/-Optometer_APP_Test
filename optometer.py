# 该类储存了所有有关数据
class Optometer:
    def __init__(self):
        # 视力表度数列表
        self.eye_chart_new = [4.0, 4.3, 4.5, 4.6, 4.7, 4.9, 5.0, 5.1, 5.2, 5.3]
        self.eye_chart_old = [0.1, 0.2, 0.3, 0.4, 0.5, 0.8, 1.0, 1.2, 1.5, 2.0]
        # 方向
        self.input_change = {"up": 1, "down": 2, "left": 3, "right": 4, "clear": 5, "unclear": 6}
        # 根据度数输出图片
        self.Graph = ["1.png", "2.png", "3.png", "4.png"]
        self.Dio = ["4.0\\", "4.3\\", "4.5\\", "4.6\\", "4.7\\", "4.9\\", "5.0\\", "5.1\\", "5.2\\", "5.3\\"]
        # correct、wrong为对错次数，flag是连续正确次数，save中保存了历次测试对错，count是记录次数，在按钮事件中保证尝试次数小于5次，
        # diopter是当前度数，break_condition为下次若正确率小于0.6 是否可以输出度数
        self.data_set = {"correct": 0, "wrong": 0, "flag": 0, "save": [], "count": 0, "diopter": 3,
                         "break_condition": 0}


# 判断输入与random产生的方向是否相同
def check(data: Optometer, random_dir: int, usr_put: str, data_set: dict):

    # 视力表随机方向 此方向对应input_change中

    # 当user input为5，6时，即为清晰与否
    if data.input_change[usr_put] == 5:
        data_set["diopter"] += 1
        reset(data_set)
    elif data.input_change[usr_put] == 6:
        data_set["diopter"] -= 1
        reset(data_set)
        if data_set["diopter"] < 0:
            print("视力低于视力表范围")
    elif data.input_change[usr_put] == random_dir:
        data_set["correct"] += 1
        data_set["save"].append(True)
        data_set["count"] += 1
        # 判断前后两次是否同为真，若是，则flag+1，若不是，则flag = 1重置
        if len(data_set["save"]) > 1 and data_set["save"][len(data_set["save"]) - 2]:
            data_set["flag"] += 1
        else:
            data_set["flag"] = 1
    else:
        data_set["count"] += 1
        data_set["wrong"] += 1
        data_set["save"].append(False)


# 在某些条件下需要重置数据，此函数即为该用途
def reset(data_set: dict):
    data_set["correct"] = 0
    data_set["wrong"] = 0
    data_set["flag"] = 0

# 计算正确率
def count_rate(data_set: dict):
    if data_set["correct"] + data_set["wrong"] != 0:
        rate = float(data_set["correct"] / (data_set["correct"] + data_set["wrong"]))
    else:
        rate = -1
    return rate
