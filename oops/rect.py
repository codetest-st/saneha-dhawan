class rect:
    count=0
    def_init_(self, l=0, b=0):
    self.l=l
    self.b=b
    rect.counts+=1
    self.srno=rect.counts

def area(self):
    return self.l*self.b
def display(self):
    print(f"dimension of rect{self.srno} {self.l}x{self.b}")
    r1=rect()
    r2=rect(6,2)
    r1.l=int(input("enter length of rect1: "))
    r1.b=int(input("enter breadth of rect1: "))
    r1.display()
    r2.display()