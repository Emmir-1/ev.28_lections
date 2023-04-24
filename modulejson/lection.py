# JSON - (Java Script Object Natation) - это единый текстовы формат даннных был создан для хранение и пердачи данных между сервисами.
# единый текстовый формат данных, был создан для хранение и передачи данных между сервисами
# <filename>.json # файл в формате JSON
# {
#     "id":1,
#     "auter":{
#     "name": "Ed Sheeran",
#     "age": 35
#     },
#     "title": "don't",
#     "feat": false,
# } ------- это JSON


# !!!!
# js object == {key : value}
# Py dict == {key : value}
# JSON == {key : value} 

# Процессы Сериализаций и Десериализаци данных (Коневертация)

# Cериализация (запись данных в JSON) - Это Python из пайтан в JSON формат

# dump - записывает данные в файл формате JSON
# dumps - записывает данные в текст формата JSON

# Десериализация (чтение данных из JSON) - это процесс перевода из JSON в Python dict

# load - функция которая считывает данные из файла JSON 
# loads - функция которая считывает данные из текста JSON 

# -----------------------------------------------------------------

# Процесс сериализации
# import json 

# dict_ = {
#     "name" : "John Snow",
#     "age" : 24,
#     "status" : True,
#     "wife" : False,
#     "cildren" : None,
# }
# print(dict_, type(dict_))
# with open("new.json", "w") as file:
#     json.dump(dict_, file, indent = 4)

    
# json_text = json.dumps(dict_)
# print()
# print(json_text, type(json_text))


# --------------------------------------------------------------------------
# Процесс десериализации 
# import json 

# with open("new.json", "r") as file:
#     json_data = file.read()

# print(json_data, type(json_data))   
# dict_ = json.loads(json_data)
# print()
# print(dict_, type(dict_))

# import json 

# with open("new.json", "r") as file:
#     dict_ = json.load(file)
#     print(dict_, type(dict_))
# --------------------------------------------------------

# from urllib.request import urlopen
# import json 
# import pprint as pp

# url = "https://randomuser.me/api/"

# json_data = urlopen(url)
# # print(json_data, type(json_data))

# dict_ = json.load(json_data)
# pp.pprint(dict_)

# def func1(list_): 
#     res = [] 
#     for i in list_: 
#         i['salary'] = i['salary'] + i['overTime']*200 
#         i.popitem() 
#         return 
# employees = [ {'name': 'Jack', 'salary': 10000, 'overTime': 4}, 
#             {'name': 'Tom', 'salary': 15000, 'overTime': 3}, 
#             {'name': 'Jessica', 'salary': 20000, 'overTime': 9}, 
#             {'name': 'Helen', 'salary': 25000, 'overTime': 2}, 
#             {'name': 'Peter', 'salary': 30000, 'overTime': 7} ] 
# print(func1(employees))

# def func1(list_): 
#     list_new = [] 
#     for x in list_: 
#         x["salary"] = x["salary"] + (x["overTime"] * 200) 
#         x.pop("overTime") 
#         list_new.append(x) 
#         print(list_new) 
#         return list_new 
# employees = [ {'name': 'Jack', 'salary': 10000, 'overTime': 4}, 
#                  {'name': 'Tom', 'salary': 15000, 'overTime': 3}, 
#                  {'name': 'Jessica', 'salary': 20000, 'overTime': 9}, 
#                  {'name': 'Helen', 'salary': 25000, 'overTime': 2}, 
#                  {'name': 'Peter', 'salary': 30000, 'overTime': 7} ] 
# print(func1(employees))

# employees = [ {'name': 'Jack', 'salary': 10000, 'overTime': 4}, 
#              {'name': 'Tom', 'salary': 15000, 'overTime': 3}, 
#              {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#             {'name': 'Helen', 'salary': 25000, 'overTime': 2}, 
#             {'name': 'Peter', 'salary': 30000, 'overTime': 7} ] 

# def func1(lsofdict:dict): 
#     for x in lsofdict: 
#         if 'overTime' in x:
#             x['salary'] += x['overTime'] * 200 
#             x.pop('overTime') 
#     return lsofdict 
# func1(employees)