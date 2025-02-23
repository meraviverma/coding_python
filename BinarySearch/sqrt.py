
# Easy one. First we need to search for minimal k satisfying
# condition k^2 > x, then k - 1 is the answer to the question. We can easily
# come up with the solution. Notice that I set right = x + 1
# instead of right = x
# to deal with special input cases like x = 0 and x = 1.
def mysqrt(x:int)->int:
    left,right =0,x+1
    while left < right:
        mid=left + (right - left) //2
        if mid * mid > x:
            right=mid
        else:
            left=mid +1
    return left -1

if __name__=="__main__":
    input=4
    print(mysqrt(input))