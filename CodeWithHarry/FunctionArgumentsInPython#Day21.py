# def average(a,b):
#     print("The average is",(a+b)/2)

#*awargs
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("average is ",sum/len(numbers))

def name_print(normal,*nameprint,**kwargs):
    print("I am normal argument",normal)
    print(type(nameprint))
    for i in range(len(nameprint)):
        print(nameprint[i])
    for item in nameprint:
        print(item)

    print("\n Now lets see example of kwargs")
    for key,value in kwargs.items():
        print(key,value)


#**kwargs
def name(**name):
    print(type(name))
    print("Hello ,",name["fname"],name["mname"],name["lname"])

#**VVIP We have to first keep Normal argument then args then kwargs
#This is thumb rule.
#args and kwargs are optional
#normal, args,kwargs this is the order.

if __name__=="__main__":
    average(2,3,6,7,4)
    average(1)
    name(mname="bachan",lname="ravi",fname="verma")

    print("#####    Print using args ########")
    name=["ravi","verma","sonu"]
    normal="This is normal arg"
    kwarg={"Rohane":"Monitor","Ravi":"President","sam":"Bahadur"}
    name_print(normal,*name,**kwarg)
    name_print(normal)



"""
output:
average is  4.4
average is  1.0
Hello , verma bachan ravi

"""
