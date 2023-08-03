pets = [
    {"name": "흰둥이1", "weight": 20.5, "age": 23},
    {"name": "흰둥이2", "weight": 19.5, "age": 20},
    {"name": "흰둥이3", "weight": 18.5, "age": 19}
]

def print_pet_info(name, weight=0, age=0):
    print(f"이름: {name}")
    print(f"몸무게: {weight}")
    print(f"나이: {age}개월")
    print()
    
for pet in pets:
    print_pet_info(pet["name"], pet["weight"], pet["age"])
    print()

# ==============================================================
name = ['강아지','순둥이','검둥이']
weight = ['20.3','15.2','22.5']
age = ['23','15','10']
print(name,weight,age)

for i in name:
     print(i, end= ' ')
    
