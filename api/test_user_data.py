import random

# 生成随机姓名
def generate_name():
    xing = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '邓', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '呼', '扈', '丰', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹']
    ming = ['伟', '芳', '娜', '秀英', '敏', '静', '丽', '强', '磊', '军', '洋', '勇', '艳', '杰', '娟', '涛', '明', '超', '秀兰', '霞', '平', '刚', '桂英', '桂军', '世民', '信', '珂', '恬', '德慧', '羽西', '绮','天晴', '慕诗', '诺依', '宁荷', '斐然']
    x = random.choice(xing)
    m = "".join(random.choice(ming) for i in range(1))
    return x + m

# 生成随机手机号
def generate_phone():
    phone = '182'
    for i in range(8):
        phone += str(random.randint(0, 9))
    return phone

# 生成随机身份证号
def generate_id():
    id = '362227'
    for i in range(10):
        id += str(random.randint(0, 12))
    return id

# 生成随机银行卡号
def generate_bank():
    bank = '6222'
    for i in range(12):
        bank += str(random.randint(0, 9))
    return bank

# 生成100条用户信息测试数据
for i in range(100):
    name = generate_name()
    phone = generate_phone()
    id = generate_id()
    bank = generate_bank()
    print(f'{name}\t{phone}\t{id}\t{bank}')
