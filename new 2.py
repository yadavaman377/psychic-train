def maximum_consecutive(lst, n): 
    count = 0 
    result = 0 
    for i in range(0, n): 
        if (lst[i] == 0): 
            count = 0
        else:  
            count+= 1 
            result = max(result, count)        
    return result  


lst=[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]

n=len(lst)

print(maximum_consecutive(lst, n))
