if __name__=='__main__':
    print("Dictionary")

    MLB_team={
        'Colorado':'Rockies',
        'Boston':'Red Box',
        'Minnesto':'Twins',
        'seattle':'Mariners'
    }

    MLB_team2 = dict([
        ('Colorado', 'Rockies'),
        ('Boston', 'Red Sox'),
        ('Minnesota', 'Twins'),
        ('Milwaukee', 'Brewers'),
        ('Seattle', 'Mariners')
        ])

    MLB_team3 = dict(
        Colorado = 'Rockies',
        Boston = 'Red Sox',
        Minnesota = 'Twins',
        Milwaukee = 'Brewers',
        Seattle = 'Mariners'
    )

    print(MLB_team)
    print(MLB_team2)
    print(MLB_team3)
    print(MLB_team['Minnesto'])

#If you refer to a key that is not in the dictionary, Python raises an exception:

# Adding an entry to an existing dictionary is simply a matter of assigning a new key and value:

    MLB_team2['Minnesota'] = 'Royals'
    print(MLB_team2)

# d.clear()
# Clears a dictionary.
    d = {'a': 10, 'b': 20, 'c': 30}
    print(d)

    d.clear()
    print(d)

#d.get(<key>[, <default>])
#Returns the value for a key if it exists in the dictionary.

    d = {'a': 10, 'b': 20, 'c': 30}
    print(d.get('b'))
    print(d.get('z'))

#d.get(<key>) searches dictionary d for <key> and returns the associated value if it is found. If <key> is not found,
# it returns None:
#If <key> is not found and the optional <default> argument is specified, that value is returned instead of None:

    print(d.get('z', -1))


# d.items()
# Returns a list of key-value pairs in a dictionary.

    d = {'a': 10, 'b': 20, 'c': 30}
    print(d)

    print(list(d.items()))

    print(list(d.items())[1][0])
    print(list(d.items())[1][1])

# d.keys()
# Returns a list of keys in a dictionary.

    d = {'a': 10, 'b': 20, 'c': 30}

    print(d)
    print(list(d.keys()))

# .pop(<key>[, <default>])
# Removes a key from a dictionary, if it is present, and returns its value.

    d = {'a': 10, 'b': 20, 'c': 30}
    print(d.pop('b'))
    print(d)

    print(d.pop('z', -1))

# .popitem()
# Removes a key-value pair from a dictionary.
# d.popitem() removes the last key-value pair added from d and returns it as a tuple:

    d = {'a': 10, 'b': 20, 'c': 30}
    d.popitem()
    print(d)


############### OUTPUT ########################
# C:\python\python.exe D:\pythonProject\Dictionary\dictionaryDemo.py
# Dictionary
# {'Colorado': 'Rockies', 'Boston': 'Red Box', 'Minnesto': 'Twins', 'seattle': 'Mariners'}
# {'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins', 'Milwaukee': 'Brewers', 'Seattle': 'Mariners'}
# {'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins', 'Milwaukee': 'Brewers', 'Seattle': 'Mariners'}
# Twins
# {'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Royals', 'Milwaukee': 'Brewers', 'Seattle': 'Mariners'}
# {'a': 10, 'b': 20, 'c': 30}
# {}
# 20
# None
# -1
# {'a': 10, 'b': 20, 'c': 30}
# [('a', 10), ('b', 20), ('c', 30)]
# b
# 20
# {'a': 10, 'b': 20, 'c': 30}
# ['a', 'b', 'c']
# 20
# {'a': 10, 'c': 30}
# -1
# {'a': 10, 'b': 20}
#
# Process finished with exit code 0
