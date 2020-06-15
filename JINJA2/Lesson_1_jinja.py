'''
использование {{}}  в шаблонах
'''

from jinja2 import Template

name = "Федор"
age = 28

tm = Template("Привет {{name}}")
msg = tm.render(name=name)
print(msg)
# Привет Федор

msg2 = f"Привет {name}"
print(msg2)
# Привет Федор

tm = Template("Привет, меня зовут {{n}} и мне {{a}} лет")
msg = tm.render(n=name, a=age)
print(msg)
# Привет, меня зовут Федор и мне 28 лет

tm = Template("Привет, меня зовут {{n.upper()}} и мне {{a*2}} лет")
msg = tm.render(n=name, a=age)
print(msg)
# Привет, меня зовут ФЕДОР и мне 56 лет

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

per = Person("Alex", 23)
per1 = Person("Alice", 18)

tm = Template("Привет, меня зовут {{p.name}} и мне {{p.age}} лет")
msg = tm.render(p=per)
print(msg)
# Привет, меня зовут Alex и мне 23 лет

tm1 = Template("Привет, меня зовут {{p.getName()}} и мне {{p.getAge()}} лет")
msg1 = tm1.render(p=per1)
print(msg1)
# Привет, меня зовут Alice и мне 18 лет


per = {'name': 'Федор', 'age': 24}
tm = Template("Привет, меня зовут {{p.name}} и мне {{p.age}} лет")
msg = tm.render(p=per)
print(msg)
# Привет, меня зовут Федор и мне 24 лет


