from typing import List


class ReverseString:
    def reverse(self,str1:str)->str:
        str2=""
        #print(str1)
        for i in str1:
            str2=i+str2
            #print(i)
        return str2


if __name__ == '__main__':
        abc = ReverseString()
        print(abc.reverse("ravi"))
        print(abc.reverse("sam"))
        print(abc.reverse("monu"))