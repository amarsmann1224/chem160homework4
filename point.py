from math import *
class point:
    def __init__(self, dim, data):
        self.dim=dim
        self.data=[]
        for i in range(dim):
            self.data.append(float(data[i]))
    def __repr__(self):
        output=""
        for i in self.data:
            output+=str(i)+" "
        return output
    def scale(self, x):
        for i in range(self.dim):
            self.data[i]*=x
    def dot(self, apoint):
        sum=0
        for i in range(self.dim):
            sum+=self.data[i]*apoint.data[i]
        return sum
    def dist(self,p2):
        distance=sqrt((self.data[0] - p2.data[0])**2+(self.data[1]-p2.data[1])**2+(self.data[2]-p2.data[2])**2)
        return distance
    def mirror(self):
        for i in range(self.dim):
            self.data[i]*=-1
        return self


