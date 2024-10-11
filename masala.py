f=open("book.txt","w+")

class book:
    def __init__(self,name,id,author ,count ,price):
        self.name = name 
        self.id=id
        self.author=author
        self.count=count
        self.price=price
    def write(self):
        f.write(f"""{self.name} {self.id} {self.author} {self.count} {self.price}""")    
    def get_info_from_file(self,f):
        for i in f.read():
            print(f.read())

    def minus_1(self,id):
        for i in f.read().split('\n'):
            for x in i.split(" "):
                print(x[1])
                if x[1]==id:
                    self.count-=1
                    self.write()
    def delete(self,id):
        for i in f.read().split('\n'):
            for x in i.split(" "):
                if x[1]!=id:
                    self.write()
b1=book("as",1212,"asd",5,1212)
b2=book("as",1312,"asd",6,1312)
b2.write()
b1.write()
b1.minus_1(1212)
# b1.get_info_from_file(f)
f.close()