# Sets are unordered.
# Set elements are unique. Duplicate elements are not allowed.
# A set itself may be modified, but the elements contained in the set must be of an immutable type.

if __name__=='__main__':
    print("Hello")
    myset=set()

    myset.add(1)
    myset.add(2)
    print(myset)
    print(len(myset))

    print(1 in myset)
    print(2 in myset)
    print(3 in myset)

    myset.remove(2)
    print(2 in myset)

    #list to set
    print(set([1,2,3]))

    #set compreshension

    myset={i for i in range(5)}
    print(myset)
    myset.add(2)

#set demo from Real Python

    print("######### set demo from Real Python #############")
    x=set(['foo','bar','baz','foo','qux'])
    print(x)

    s='quux'
    print(list(s))
    print(set(s))  #{'q', 'x', 'u'} from this we understand that set are unordered
    print(set(list(s)))

    print({'foo'})
    print(set('foo'))

    # so the only way to define an empty set is with the set() function:

    x=set()
    print(type(x))

    x={}
    print(type(x))

    x=set()
    print(bool(x))

    x={'foo','bar','baz'}
    print(len(x))

    print('bar' in x)
    print('qux' in x)

#In Python, set union can be performed with the | operator:
    x1={'foo','bar','baz'}
    x2={'baz','qux','quux'}
    print(x1 | x2)

#Python raises an exception if <elem> is not in x:
#x.remove(<elem>)

    x = {'foo', 'bar', 'baz'}
    print(x)
    x.remove('baz')
    print(x)
    x.remove('qux')

#x.discard(<elem>)
# x.discard(<elem>) also removes <elem> from x. However, if <elem> is not in x,
# this method quietly does nothing instead of raising an exception:
    x = {'foo', 'bar', 'baz'}
    x.discard("foo")
    print(x)
    x.discard('qux')
    print(x)

# x.pop()
# Removes a random element from a set.
    x={'foo','bar','baz'}
    print(x.pop())

# x.clear()
# x.clear() removes all elements from x:

################## OUTPUT #########################

# C:\python\python.exe D:\pythonProject\HashSets\HashSetDemo.py
# Traceback (most recent call last):
#   File "D:\pythonProject\HashSets\HashSetDemo.py", line 73, in <module>
#     x.remove('qux')
# KeyError: 'qux'
# Hello
# {1, 2}
# 2
# True
# True
# False
# False
# {1, 2, 3}
# {0, 1, 2, 3, 4}
# ######### set demo from Real Python #############
# {'foo', 'baz', 'bar', 'qux'}
# ['q', 'u', 'u', 'x']
# {'x', 'u', 'q'}
# {'x', 'u', 'q'}
# {'foo'}
# {'f', 'o'}
# <class 'set'>
# <class 'dict'>
# False
# 3
# True
# False
# {'foo', 'qux', 'baz', 'quux', 'bar'}
# {'bar', 'foo', 'baz'}
# {'bar', 'foo'}
#
# Process finished with exit code 1
