class Poly:
    def __init__(self,no_sides):
        self.n=no_sides
        
    def input_sides(self, side_1, side_2):
        self.a=side_1
        self.b=side_2
        
    def write_file(self):
        f=open("data.txt", "a")
        if self.a==self.b:
            f.write(str(self.b))
            f.write("\n")
        else:
            f.write(str(self.a))
            f.write(" ")
            f.write(str(self.b))
            f.write("\n")
        f.close()        
        

class Square(Poly):
    def __init__(self):
        Poly.__init__(self,4)

    def perimeter(self):
        p=4*self.a
        #print ('Perimeter is %d' %p)
        return p
        
    
class Rectangle(Poly):
    def __init__(self):
        Poly.__init__(self,4)

    def perimeter(self):
        p=2*(self.a+self.b)
        #print ('Perimeter is %d' %p)
        return p


r1= Rectangle()
r1.input_sides(5,7)
r1.write_file()
k=r1.perimeter()

s1=Square()
s1.input_sides(5,5)
s1.write_file()
s1.perimeter()

r1.input_sides(3,9)
r1.write_file()
k=r1.perimeter()

s1=Square()
s1.input_sides(10,10)
s1.write_file()
s1.perimeter()


with open("data.txt","r") as f:
    with open("output.txt","w") as output:
        lst=[]
        for line in f:
            a=[]
            a=line.split(' ')
            #print "length"
            #print len(a)
            if len(a)==1:
                #print "Hello"
                s1.input_sides(int(a[0]),int(a[0]))
                k=s1.perimeter()
                #print k
                output.write("squareSide= "+str(a[0])+"Perimeter of the square "+str(k)+"\n\n")
            else:
                #print "rect"
                r1.input_sides(int(a[0]),int(a[1]))
                k=r1.perimeter()
                #print k
                output.write("length= "+str(a[0])+" "+"width= "+str(a[1])+"Perimeter of the rectangle "+str(k)+"\n\n")
            
                
