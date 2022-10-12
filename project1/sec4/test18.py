class Rectangle:
    count=0

    def __int__(self,width,height):
        self.width=width
        self.height=height
        Rectangle.count+=1

    #면적
    def calcArea(self):
        Area=self.width*self.height
        print(Area)
        
    @staticmethod
    def isSquare(w,h):
        if(w=h):
            print("정사각형입니다.")
        else:
            print("정사각형ㄴㄴ")
            
    @classmethod
    def printCount(rect):
    
    def __add__(self, other):
        obj = Rectangle

    def __del__(self):
        print("사각형 소멸")