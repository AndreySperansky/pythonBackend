'''
https://www.youtube.com/watch?v=RYIGMcJMy6g&list=PLA0M1Bcd0w8wfmtElObQrBbZjY6XeA06U&index=6
'''

'''
Наследование расширение шаблонов
'''

from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)

template = env.get_template('about.html')

output = template.render()
print(output)

'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> О сайте </title>
</head>
<body>

<h1>О сайте</h1>
<p>Классный сайт если его доделать</p>

</body>
</html>
'''

file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)

template = env.get_template('about_1.html')

output = template.render()
print(output)


'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> О сайте </title>
</head>
<body>


Блок контента               #

<h1> О сайте </h1>
<p>Классный сайт если его доделать</p>

</body>
</html>
'''

subs = ["Математика", "Физика", "Информатика", "Русский"]

file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)

template = env.get_template('about_2.html')

output = template.render(list_table = subs)
print(output)

'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> О сайте </title>
</head>
<body>

   
    <ul>
        <li>Математика</li>
        <li>Физика</li>
        <li>Информатика</li>
        <li>Русский</li>
        
    </ul>
    

<h1> О сайте </h1>
<p>Классный сайт если его доделать</p>

</body>
</html>
'''

file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)

template = env.get_template('about_3.html')

output = template.render(list_table = subs)
print(output)

'''

    <ul>
        <li>Математика</li>
        <li>Физика</li>
        <li>Информатика</li>
        <li>Русский</li>
        
    </ul>
    
'''

file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)

template = env.get_template('about_4.html')

output = template.render(list_table = subs)
print(output)

'''
<ul>
    <li><p class="item">Математика</p></li>
    <li><p class="item">Физика</p></li>
    <li><p class="item">Информатика</p></li>
    <li><p class="item">Русский</p></li>
    
</ul>
'''