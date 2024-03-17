def greet_people(name):
    """_summary_

    Args:
        name (str): name of a person.
    """
    print('Hello',name)
greet_people('Chetan') # doesn't work without name 

def multiply(num1,num2):
    total = num1*num2
    #print(total)
    return total
multiply(4,44)
result = multiply(33,55)
print(result)
# what if we want to allow specific datatype as a argument?

def check_3digit(n):
    return n in range(100,1000)
sum =343+655
check_3digit(434)
check_3digit(22)
check_3digit(sum)


def check_3_digit(l):
    for i in l:
        if i in range(100,1000):
            return True
        else:
            pass
    return False
check_3_digit([33,44,545,3])
check_3_digit([2,4,44])

def check_3_digit(l):
    result = []
    for i in l:
        if i in range(100,1000):
            result.append(i)
    if result:
        return result
    return False
check_3_digit([33,44,545,3])
check_3_digit([2,4,44])