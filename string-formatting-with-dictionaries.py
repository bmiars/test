
template = "Hi, I'm {name} and I love to eat {food}!"
def string_factory(values):
	return [template.format(**x) for x in values]
	
values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]

print(string_factory(values))