import sqlite3
import random
import sys
import json
from faker import Faker
db = sqlite3.connect('db/pisda.db')
with open('config.json', 'r') as json_file:
    data = json.load(json_file)
    language = (data["lang"])
    phone_num = (data["phone_num"])
    max_age = (data["max_age"])
    min_age = (data["min_age"])

if language == 'ru':
    fake = Faker('ru_RU')
else:
    if language == 'en':
        fake = Faker('en_US')
    else:
        print('Ошибка в файле config.json')
        sys.exit()

if phone_num == 'ru':
    firstRandom = 7900000000
    lastRandom = 7999999999
else:
    if phone_num == 'us':
        firstRandom = 1000000000
        lastRandom = 9999999999
    else:
        print('Ошибка в файле config.json')
        sys.exit()

with open('1.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Создаем список для хранения значений name
names = []

# Проходим по каждому компоненту и извлекаем значение name
for component in data:
    names.append(component['name'])

sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users (id INT, first_name TEXT, last_name TEXT, age INT, phone_num INT, city TEXT) """)

db.commit()


sql.execute("SELECT * FROM users")

k = int(input('На сколько строк заполнить БД:'))
user_id = 1
first_name = fake.first_name()
last_name = fake.last_name()
age = random.randint(min_age, max_age)
phone_num = random.randint(firstRandom, lastRandom)
city = random.choice(names)
for i in range(k):
    sql.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?)", (user_id, first_name, last_name, age, phone_num, city))
    db.commit()
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = random.randint(min_age, max_age)
    phone_num = random.randint(firstRandom, lastRandom)
    city = random.choice(names)
    user_id = user_id + 1
    
print(user_id)