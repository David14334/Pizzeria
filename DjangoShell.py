import os

from pizzas.views import comment
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza

pizzas = Pizza.objects.all()

for p in pizzas:
    print(p.id,'  ',p.pizza_name)

p = Pizza.objects.get(id=1)

print(p.pizza_name)

toppings = p.topping_set.all()

for t in toppings:
    print(t.topping_name)

comments = p.comment_set.all()

for c in comments:
    print(c.comment_text)
    print(c.date_added)


