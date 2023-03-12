def find_pair(items, target):
    result = []
    for i,v in enumerate(items[:len(items)-1]):
        for j,k in enumerate(items[i+1:]):
            if v + k == target:
                result.append(i)
                result.append(i+j+1)
            
    return result 

print(find_pair([2,7,8,9], 15))