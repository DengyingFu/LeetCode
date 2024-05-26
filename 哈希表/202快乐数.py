#========字典做哈希表========
#当一个数第二次出现时，就不可能是快乐数了，return False
class Solution:
    def isHappy(self, n: int) -> bool:
        res = {}
        while 1:
            n2 = 0
            for num in str(n):
                n2 = n2+int(num)**2
            if n2==1:
                return True
            n = n2
            res[n2] = res.get(n2,0)+1
            if res[n2]>1:
                return False
#=======集合set的哈希表========
class Solution:
    def isHappy(self, n: int) -> bool:
        res = set()
        while n not in res:
            res.add(n)
            tmp = 0
            for num in str(n):
                tmp = tmp+int(num)**2
            if tmp == 1:
                return True
            else:
                n = tmp
        return False
