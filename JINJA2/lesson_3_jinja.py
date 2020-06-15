'''
https://www.youtube.com/watch?v=dsUOZXM1GAM&list=PLA0M1Bcd0w8wfmtElObQrBbZjY6XeA06U&index=3
'''

'''
Фильтры и макросы macro, call
'''

from jinja2 import Template

cars = [{'model': 'Audi', 'price': 23000},
        {'model': 'Skoda', 'price': 17300},
        {'model': 'Volvo', 'price': 44300},
        {'model': 'Volkswagen', 'price': 21300}
        ]

tpl = "Суммарная цена автомобилей {{cs | sum(attribute='price')}}"
tm = Template(tpl)
msg = tm.render(cs = cars)
print(msg)


# Суммарная цена автомобилей 105900


digs = [1, 2, 3, 4, 5]
tpl = "{{cs | sum}}"
tm = Template(tpl)
msg = tm.render(cs = digs)
print(msg)

# 15

tpl = "Max цена автомобилей {{cs | max(attribute='price')}}"
tm = Template(tpl)
msg = tm.render(cs = cars)
print(msg)
# Max цена автомобилей {'model': 'Volvo', 'price': 44300}

tpl = "Min цена автомобилей {{cs | min(attribute='price')}}"
tm = Template(tpl)
msg = tm.render(cs = cars)
print(msg)

# Min цена автомобилей {'model': 'Skoda', 'price': 17300}

tpl = "Max цена автомобилей {{(cs | max(attribute='price')).model}}"
tm = Template(tpl)
msg = tm.render(cs = cars)
print(msg)

# Max цена автомобилей Volvo

tpl = "Min цена автомобилей {{(cs | min(attribute='price')).model}}"
tm = Template(tpl)
msg = tm.render(cs = cars)
print(msg)

# Min цена автомобилей Skoda

tpl = "Случайно выбранный автомобиль {{cs | random}}"
tm = Template(tpl)
msg = tm.render(cs = cars)
print(msg)
# Случайно выбранный автомобиль {'model': 'Volkswagen', 'price': 21300}

tpl = "Замена о на О в названии автомобиля {{cs | replace('o', 'O')}}"
tm = Template(tpl)
msg = tm.render(cs = cars)
print(msg)
# Замена о на О в названии автомобиля [{'mOdel': 'Audi', 'price': 23000}, {'mOdel': 'SkOda', 'price': 17300},\
                                     # {'mOdel': 'VOlvO', 'price': 44300}, {'mOdel': 'VOlkswagen', 'price': 21300}]
                                     


persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0},
]

tpl = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor -%}
'''

tm =  Template(tpl)
msg = tm.render(users = persons)
print(msg)

# АЛЕКАЛЕКСЕЙ
# НИКОЛАЙ
# ИВАН

tpl = '''
{%- for u in users -%}
{% filter lower %}{{u.name}}{% endfilter %}
{% endfor -%}
'''

tm =  Template(tpl)
msg = tm.render(users = persons)
print(msg)

# алексей
# николай
# иван


# Макросы ********************************************************************************

html = '''
{% macro input(name, value='',  type='text', size=20) -%}
    <input type="{{type}}" name="{{name}}" value="{{value | e}}" size="{{size}}">
{%- endmacro %}

<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password') }}
'''

tm =  Template(html)
msg = tm.render()
print(msg)

# <p><input type="text" name="username" value="" size="20">
# <p><input type="text" name="email" value="" size="20">
# <p><input type="text" name="password" value="" size="20">



html = '''
{% macro list_users(list_of_users) -%}
<ul>
{% for u in list_of_users -%}
    <li>{{u.name}}
{%- endfor %}
</ul>
{%- endmacro -%}


{{list_users(users)}}
'''

tm = Template(html)
msg = tm.render(users = persons)
print(msg)

# <ul>
# <li>Алексей<li>Николай<li>Иван
# </ul>


html = '''
{% macro list_users(list_of_users) -%}
<ul>
{% for u in list_of_users -%}
    <li>{{u.name}}{{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro -%}

{% call(user) list_users(users) -%}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{%- endcall -%}
'''

tm = Template(html)
msg = tm.render(users = persons)
print(msg)

# <ul>
# <li>Алексей<ul>
#     <li>age: 18
#     <li>weight: 78.5
#     </ul><li>Николай<ul>
#     <li>age: 28
#     <li>weight: 82.3
#     </ul><li>Иван<ul>
#     <li>age: 33
#     <li>weight: 94.0
#     </ul>
# </ul>






