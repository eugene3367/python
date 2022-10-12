# 3개 단어 입력받아 첫글자 추출
# 반복문, 입/출/슬라이싱 사용

a=input("first word:")
b=input("second word")
c=input("third word")

a.split(sep=' ')
b.split(sep=' ')
c.split(sep=' ')

print(a[0]+b[0]+c[0])

class WordAbbr:
    word = ""

    def inputWord(self):
        in1 = input("첫번째 단어 :")
        in2 = input("두번째 단어 :")
        in3 = input("세번째 단어 :")
        self.word = in1[0] + in2[0] + in3[0]
        return self.word

    def printWord(self):
        print(self.word)

w = WordAbbr()
w.inputWord()
w.printWord()