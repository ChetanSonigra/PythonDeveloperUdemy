my_text = 'This text is a test'

result = my_text[0]
result2 = my_text[7]
result3 = my_text[-3]
print(result,result2,result3)

result = my_text.index('h')
result2 = my_text.index('text')
result3 = my_text.index('s')
result4 = my_text.index('s',5,12)
print(result, result2, result3, result4)

result = my_text.rindex('s') # reverse index
print(result)