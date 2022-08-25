class test:
    def __init__(self,a,b,c,d):
     self.a=a
     self.b=b
     self.c=c
     self.d=d

    def test_custome(self,v):
       return v-self.a

    def __str__(self):
       return "this is my abstraction class"

o=test(4,5,6,7)
o.test_custome(7)

print(o)

