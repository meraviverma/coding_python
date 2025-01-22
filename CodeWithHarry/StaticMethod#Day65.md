Static methods in Python are methods that belong to a class rather than an instance of the class. 
They are defined using the @staticmethod decorator and do not have access to the instance of the 
class (i.e. self). They are called on the class itself, not on an instance of the class. 
Static methods are often used to create utility functions that don't need access to instance data.

class Math:
    @staticmethod
    def add(a, b):
        return a + b
result = Math.add(1, 2)
print(result) # Output: 3

In this example, the add method is a static method of the Math class. It takes two parameters a and b and 
returns their sum. The method can be called on the class itself, without the need to create an instance of 
the class.

When to Use Static Methods in Python:
When you need a function that logically belongs to the class but does not require access to instance variables or methods.
When you have a utility function that works with parameters passed directly into the method, not depending on the state of the instance.

Use static methods when:
1)  The method is related to the class but doesn’t need access to instance data (self) or class data (cls).
2)  The method operates independently and only uses the arguments passed to it (or global variables).
3) You want to group utility functions within the class.
4) The method is a utility or helper function.