class StringClass:
    def __init__(self,demo):
        self.demo=demo
    def lis(self):
        return(list(self.demo))
    def length(self):
        return len(self.demo)
class PairsPossible(StringClass):
    def pair(self,test_list):
        res = [(a,b) for idx,a in enumerate(test_list)for b in test_list[idx+1:]]
        print(res)
class SearchCommonElements(StringClass):
    def common(self, st, demo):
        c = list(set(st) & set(demo))
        print(c)
class EqualPairs(StringClass):
    def pair2(self,test_list):
        res =[[((int(a),int(b))) for idx,a in enumerate(test_list)for b in test_list[idx+1:]]]
        print(set(res))
        print(len(set(res)))

a=input("Enter a string :")
b=StringClass(a)
print(b.lis())
print(b.length())
h=b.lis()
d=PairsPossible(b)
d.pair(h)
st=input("Enter string to compare")
cm=SearchCommonElements(b)
cm.common(a,st)
ep=EqualPairs()
ep.pair2(h)
