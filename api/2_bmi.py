#BMI = 体重 / (身高 ** 2)
user_weight = float(input("请输入你的体重（单位：kg）:"))
user_height = float(input("请输入你的身高（单位：m）:"))
user_BMI = user_weight / (user_height) ** 2
print("你的BMI值为：" + str(user_BMI))
