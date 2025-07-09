"""
__name starts with double underscores → this tells Python:
“Hey, this is private! Don’t let outsiders touch it easily.”
"""
class Hero:
    def __init__(self, name,age):
        self._name = name  # protected attribute
        self.__age=age #Private attribute

    def _show_name(self):  # protected method
        print(self._name)

if __name__=="__main__":

    h = Hero("Ironman",32)
    print(h._name)        # Possible, but discouraged
    h._show_name()
    print(type(h))

    print(h._Hero__age)
