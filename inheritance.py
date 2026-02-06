
class ListPlus(list): # ListPlus "inherit from" list
    def removeAll(self, value):
        while value in self:
            self.remove(value)
    def __add__(self, other):
        newList=[]
        
        if len(self) > len(other):
            for index in range(len(other)): 
                newList.append(self[index]+other[index])
            for index in range(len(other), len(self)): 
                newList.append(self[other])
        else:
            for index in range(len(self)):
                newList.append(self[index]+other[index])
            for index in range(len(self), len(other)):
                newList.append(other[index])
                
        return newList

l1=ListPlus()
l1.append(56)
l1.extend([67,56,88,100,56])
l1.insert(0,100)
print(l1)
l1.removeAll(56)
print(l1)

l2=ListPlus()

l2.extend([10,20,36,67])
print(l2)

l3=l1+l2

print(l3)


