"""
https://www.youtube.com/watch?v=F63wc5nPdho&list=PLA0M1Bcd0w8wfmtElObQrBbZjY6XeA06U&index=2
"""

'''
Экранирование и блоки  raw, for, if
'''

from jinja2 import Template, escape

data = '''Модуль Jinja вместо
определения {{name}}
подставляет соответствующее значение
'''

tm = Template(data)
msg = tm.render(name="Федор")
print(msg)

# Модуль Jinja вместо
# определения Федор
# подставляет соответствующее значение


data = '''{%raw%} Модуль Jinja вместо
определения {{name}}
подставляет соответствующее значение {%endraw%}
'''

tm = Template(data)
msg = tm.render(name="Федор")
print(msg)

# Модуль Jinja вместо
# определения {{name}}
# подставляет соответствующее значение


link = '''В HTML-документе ссылки определяются так:  <a href="#">Ссылка</a>'''
tm = Template(link)
msg = tm.render()
print(msg)
# В HTML-документе ссылки определяются так:  <a href="#">Ссылка</a>

link = '''В HTML-документе ссылки определяются так:  <a href="#">Ссылка</a>'''
tm = Template("{{link | e}}")
msg = tm.render(link = link)
print(msg)

# В HTML-документе ссылки определяются так:  &lt;a href=&#34;#&#34;&gt;Ссылка&lt;/a&gt;
# т.е. символы < и > тэгов отображаются как их буквенные спецсимволы.

# по-другому это же можно решить с помощью класса escscape

msg = escape(link)
print(msg)
# В HTML-документе ссылки определяются так:  &lt;a href=&#34;#&#34;&gt;Ссылка&lt;/a&gt;

# Оператор for ********************************************************

cities = [  {'id':1, 'city': 'Москва'},
            {'id':5, 'city': 'Тверь'},
            {'id':7, 'city': 'Минск'},
            {'id':8, 'city': 'Смоленск'},
            {'id':9, 'city': 'Калуга'},
            ]

link = '''<select name="cities">
{% for c in cities %}
    <option value = "{{c['id']}}">{{c['city']}}</option>
{% endfor %}
</select>
'''

tm = Template(link)
msg = tm.render(cities = cities)

print(msg)
# <select name="cities">
#
#     <option value = "1">Москва</option>
#
#     <option value = "5">Тверь</option>
#
#     <option value = "7">Минск</option>
#
#     <option value = "8">Смоленск</option>
#
#     <option value = "9">Калуга</option>
#
# </select>


link = '''<select name="cities">
{% for c in cities -%}
    <option value = "{{c['id']}}">{{c['city']}}</option>
{% endfor -%}
</select>
'''
# Добавили знак '-' перед % чтобы убрать пробелы

tm = Template(link)
msg = tm.render(cities = cities)

print(msg)
# <select name="cities">
# <option value = "1">Москва</option>
# <option value = "5">Тверь</option>
# <option value = "7">Минск</option>
# <option value = "8">Смоленск</option>
# <option value = "9">Калуга</option>
# </select>

# Оператор if, elif, else  ********************************************************

link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value = "{{c['id']}}">{{c['city']}}</option>
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities = cities)
print(msg)

# <select name="cities">
# <option value = "7">Минск</option>
# <option value = "8">Смоленск</option>
# <option value = "9">Калуга</option>
# </select>

link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value = "{{c['id']}}">{{c['city']}}</option>
{% else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities = cities)
print(msg)

# <select name="cities">
# Москва
# Тверь
# <option value = "7">Минск</option>
# <option value = "8">Смоленск</option>
# <option value = "9">Калуга</option>
# </select>

link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value = "{{c['id']}}">{{c['city']}}</option>
{% elif c.city == "Москва" -%}
    <option value = "{{c['city']}}</option>
{% else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities = cities)
print(msg)

