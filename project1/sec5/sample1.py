# # 지방 탄수화물 단백질 입력
# # 총 calory= (fat*9)+(carbon*4)+(protein*4)
#
# fat=int(input("fat : "))
# carbon=int(input("carbon : "))
# protein=int(input("protein : "))
#
# calory= (fat*9)+(carbon*4)+(protein*4)
#
# print(calory)

protein = int(input('단백질 : '))
fat = int(input('지방 : '))
carbohydrate = int(input('탄수화물 : '))

calorie = fat*9 + protein*4 + carbohydrate*4
print(calorie)

class Calorie:
    calorie = 0

    def inputCalorie(self, p, f, c):
        self.protein = p
        self.fat = f
        self.carbon = c

    def calcCalorie(self):
        return (self.protein*9 + self.fat*4 + self.carbon*4)

p1 = int(input)