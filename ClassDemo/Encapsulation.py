class Hero:
    def __init__(self, name):
        self._name = name  # protected attribute

    def _show_name(self):  # protected method
        print(self._name)

if __name__=="__main__":

    h = Hero("Ironman")
    print(h._name)        # Possible, but discouraged
    h._show_name()
