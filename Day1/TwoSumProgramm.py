def two_sum(nums,target):
    #create a dictionary to store component of each number
    component={}

    #loop through the array
    for i,num in enumerate(nums):
        if num in component:
            return [component[num],i]
        else:
            component[target-num]=i

    return None

if __name__=='__main__':
    print(two_sum([2,3,4,5,6],10))

