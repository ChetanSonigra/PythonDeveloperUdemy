text = 'We are going to learn six methods today.'
result = text.upper; print(result)
result = text.upper(); print(result)
result = text.lower(); print(result)
result = text.capitalize(); print(result)
result = text.title(); print(result)
result = text.split(); print(result)
result = text.split('o'); print(result)

a = 'learning'
b = 'python'
c = 'is'
d = 'amazing'
e = ' '.join([a,b,c,d])
print(e)

result = text.find('s'); print(result)
result = text.find('q'); print(result)    # returns -1 if not found.

result = text.replace('six', 'a lot of'); print(result)
result = text.replace('a', 'x'); print(result)

