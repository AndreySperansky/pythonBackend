"""
https://www.youtube.com/watch?v=Ree-JFi06y8&list=PLA0M1Bcd0w8wfmtElObQrBbZjY6XeA06U&index=5
"""
'''
Конструкции include и import
'''

from jinja2 import Environment, FileSystemLoader, FunctionLoader

# Пример для конструкции INCLUDE

file_loader = FileSystemLoader('Templates')
# file_loader = FileSystemLoader('')             # для корневого каталога
env = Environment(loader = file_loader)

tm = env.get_template('page.html')
msg = tm.render()
print(msg)

'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Header</title>
</head>
<body>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. <br>
    A beatae deserunt dicta ducimus eaque facilis hic iste qui, quia similique.
</p>
</body>
<footer>
    <p>Copyright</p>
</footer>
</html>
'''

file_loader = FileSystemLoader('Templates')
env = Environment(loader = file_loader)

tm = env.get_template('page.html')
msg = tm.render(domain='http://speransky.ru', title="Про jinja")
print(msg)

'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <base href="http://speransky.ru">
    <title>Про jinja</title>
</head>
<body>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. <br>
    A beatae deserunt dicta ducimus eaque facilis hic iste qui, quia similique.
</p>
</body>
<footer>
    <p>Copyright</p>
</footer>
</html>
'''

# Пример для конструкции IMPORT

file_loader = FileSystemLoader('Templates')
env = Environment(loader = file_loader)

tm = env.get_template('page2.html')
msg = tm.render(domain='http://speransky.ru', title="Про jinja")
print(msg)

'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <base href="http://speransky.ru">
    <title>Про jinja</title>
</head>
<body>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. <br>
    A beatae deserunt dicta ducimus eaque facilis hic iste qui, quia similique.
</p>
</body>
<div class="dialog">
    <p class="title">Внимание</p>
    <P class="message">это тестовый диалог</P>
    <p><input type="button" value="Закрыть"></p>
</div>

<footer>
    <p>Copyright</p>
</footer>
</html>
'''