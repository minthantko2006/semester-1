
from person import Person
from datetime import date

p = Person("Alan John Smith", date(2000, 5, 10))

print(p.initials())
print(p.is_birthday())
