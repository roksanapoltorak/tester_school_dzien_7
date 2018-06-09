import copy

data = {'a': 100, 'b': 10}

print(data['a'])
print(data.get('c', 300))
print(data)

inner = {1: 'foo', 2: 'bar'}
outer = {'a': inner, 'b': dict(inner)}
outer2 = copy.deepcopy(outer)
print(outer)
print(outer2)

outer2['b'] = 3
print(outer)
print(outer2)

outer2['a'][1] = 'baz'
print(outer)
print(outer2)

print(inner[1])
outer2['a'] = 10
print(outer)
print(outer2)