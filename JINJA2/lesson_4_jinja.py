'''
https://www.youtube.com/watch?v=1Dsy2dKNP3Y&list=PLA0M1Bcd0w8wfmtElObQrBbZjY6XeA06U&index=4
https://jinja.palletsprojects.com/en/2.11.x/api/#jinja2.Environment
'''

'''
Загрузчики шаблонов - FileSystemLoader, PackageLoader, DictLoader, FunctionLoader
'''
from jinja2 import Environment, FileSystemLoader, FunctionLoader

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0},
]


file_loader = FileSystemLoader('Templates')
# file_loader = FileSystemLoader('')             # для корневого каталога
env = Environment(loader = file_loader)

tm = env.get_template('main.html')
msg = tm.render(users = persons)
print(msg)

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Tamplate1</title>
# </head>
# <body>
# <ul>
#     <li>Алексей
#     <li>Николай
#     <li>Иван
#     </ul>
# </body>
# <footer>
#     <p>Copyright</p>
# </footer>
# </html>

# использование загрузчика FunctionLoader  ********************************************

def loadTpl(path):
    if path == "index":
        return  "Имя {{u.name}},  возраст {{u.old}}"
    else:
        return  "Данные: {{u}}"

file_loader = FunctionLoader(loadTpl)
env = Environment(loader = file_loader)

tm = env.get_template('index')
msg = tm.render(u = persons[1])
print(msg)

# Имя Николай,  возраст 28

file_loader = FunctionLoader(loadTpl)
env = Environment(loader = file_loader)

tm = env.get_template('index_any')  # т.е. не index  а значит выполняется условие  else
msg = tm.render(u = persons[0])
print(msg)

# Данные: {'name': 'Алексей', 'old': 18, 'weight': 78.5}


