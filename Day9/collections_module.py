from collections import Counter,defaultdict,namedtuple

l = [1,3,5,2,1,5,1,1,6,3,5,1,8,2]
s = 'Msdofksdjaksdnlsd'
sen = 'you never win if you never begin.'
print(Counter(l))
print(Counter(s))
print(Counter(sen.split()))

series = Counter([1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3])
print(series.most_common())
print(series.most_common(2))
print(list(series))


my_dict = defaultdict(lambda: 'nothing')
my_dict['one'] = 'Red'
print(my_dict['two'])
print(my_dict)


person = namedtuple('person',['name','height','weight'])
chetan = person('Chetan',1.76,60)
print(chetan.height,chetan.weight, chetan[2])