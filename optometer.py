class Optometer:
    def __init__(self):
        # 视力表度数列表
        self.eye_chart_new = [4.0, 4.3, 4.5, 4.6, 4.7, 4.9, 5.0, 5.1, 5.2, 5.3]
        self.eye_chart_old = [0.1, 0.2, 0.3, 0.4, 0.5, 0.8, 1.0, 1.2, 1.5, 2.0]
        # 方向转换
        self.input_change = {"up": 1, "down": 2, "left": 3, "right": 4, "clear": 5, "unclear": 6}
        self.Graph = ["1.png", "2.png", "3.png", "4.png"]
        self.Dio = ["4.0\\", "4.3\\", "4.5\\", "4.6\\", "4.7\\", "4.9\\", "5.0\\", "5.1\\", "5.2\\", "5.3\\"]
        self.data_set = {"correct": 0, "wrong": 0, "flag": 0, "save": [], "count": 0, "diopter": 3, "break_condition": 0}


def check(data: Optometer, random_dir, usr_put: str, data_set: dict):
    # 判断
    # 视力表随机方向 此方向对应input_change中
    if data.input_change[usr_put] == 5:
        data_set["diopter"] += 1
        data_set["correct"] = 0
        data_set["wrong"] = 0
        data_set["flag"] = 0
    elif data.input_change[usr_put] == 6:
        data_set["diopter"] -= 1
        data_set["correct"] = 0
        data_set["wrong"] = 0
        data_set["flag"] = 0
        if data_set["diopter"] < 0:
            print("视力低于视力表范围")
    elif data.input_change[usr_put] == random_dir:
        data_set["correct"] += 1
        data_set["save"].append(True)
        data_set["count"] += 1
        if len(data_set["save"]) > 1 and data_set["save"][len(data_set["save"]) - 2]:
            data_set["flag"] += 1
        else:
            data_set["flag"] = 1
    else:
        data_set["count"] += 1
        data_set["wrong"] += 1
        data_set["save"].append(False)


def reset(data_set: dict):
    data_set["correct"] = 0
    data_set["wrong"] = 0
    data_set["flag"] = 0


def count_rate(data_set: dict):
    if data_set["correct"] + data_set["wrong"] != 0:
        rate = float(data_set["correct"] / (data_set["correct"] + data_set["wrong"]))
    else:
        rate = -1
    return rate
