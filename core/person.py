import copy
import json
import random

cities = [
    '北京',
    '上海',
    '天津',
    '重庆',
    '哈尔滨',
    '长春',
    '沈阳',
    '呼和浩特',
    '石家庄',
    '太原',
    '西安',
    '济南',
    '乌鲁木齐',
    '西宁',
    '兰州',
    '郑州',
    '南京',
    '武汉',
    '杭州',
    '合肥',
    '福州',
    '南昌',
    '长沙',
    '贵阳',
    '广州',
    '昆明',
    '南宁',
    '海口'  # '拉萨', '成都', '台北', '香港', '澳门'
]

ages = [num for num in range(5, 11)]

genders = ['男', '女']

mbti_types = [
    'INTJ', 'INTP', 'INFJ', 'INFP', 'ISTJ', 'ISTP', 'ISFJ', 'ISFP', 'ENTJ',
    'ENTP', 'ENFJ', 'ENFP', 'ESTJ', 'ESTP', 'ESFJ', 'ESFP'
]

attribute_template = {'魅力': 10, '智力': 10, '健康': 10, '富裕': 10, '幸福度': 10}


def random_normal(minimum=1, maximum=10):
    mean = 4
    std_dev = 1.5

    num = random.gauss(mean, std_dev)
    rounded_num = round(num)
    clipped_num = max(minimum, min(maximum, rounded_num))

    return clipped_num


def initialize():
    city = random.choice(cities)
    age = random.choice(ages)
    gender = random.choice(genders)
    mbti_type = random.choice(mbti_types)
    attribute = copy.deepcopy(attribute_template)
    for attribute_name in attribute:
        attribute[attribute_name] = random_normal(1, attribute[attribute_name])

    return city, age, gender, mbti_type, attribute


class Person:
    def __init__(self) -> None:
        city, age, gender, mbti_type, attribute = initialize()
        self.city = city
        self.age = age
        self.gender = gender
        self.mbti_type = mbti_type
        self.attribute = attribute

    def __str__(self) -> str:
        person_prompt = {
            '性别': self.gender,
            '城市': self.city,
            '年龄': self.age,
            '性格': self.mbti_type,
            '属性': self.attribute
        }
        return json.dumps(person_prompt)


if __name__ == '__main__':
    city, age, gender, mbti_type, attribute = initialize()
    print(f'city: {city}, age: {age}, gender: {gender}, mbti: {mbti_type}')
    print(f'{attribute}')
    print()

    person = Person()
    print(person)
