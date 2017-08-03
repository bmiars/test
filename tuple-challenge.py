def multiply(*nums):
    total = 1
    for num in nums:
        total *= num
    return total 

print multiply([2,2,2],2)

def combo(iter1, iter2):
    result = []
    
    count = 0
    for i in iter1:
        combine = iter1[count], iter2[count]
        result.append(combine)
        count +=1

    return result

print(combo([1, 2, 3], 'abc'))