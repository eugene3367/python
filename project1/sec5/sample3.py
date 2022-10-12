# 화물요금
# 화물 10kg당 2000원 /10kg미만 화물료없음

a=float(input("weight : "))

if(a>=10):
    tot=a*2000
    print("you pay ",tot,"원")
else:
    print("free")

