from functools import reduce
def largestelement(x):
    largest = x[0]
    #print(largest)
    for i in range(len(x)):
        if (largest < x[i]):
            largest=x[i]
    return largest

##Using max function
def largest(arr):
    ans=max(arr)
    return ans

##Using sort
def largest1(arr):
    arr.sort()
    return arr[len(arr)-1]

##Using reduce
def largest2(arr):
    ans=reduce(arr)
    return ans

if __name__ == '__main__':
    print(largestelement([2,5,1,3,0]))
    print(largestelement([8,10,5,7,9]))
    print(largest([8,10,5,6,2]))
    print(largest1([2, 5, 1, 3, 0]))
    print(largest2([8, 10, 5, 7, 9]))
