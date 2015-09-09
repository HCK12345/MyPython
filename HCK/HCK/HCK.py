#dic1 = {}
#dic2= dict()
#dic = {'name':'pey','phone':'0119993323','birth':'1118'}
#a = {1:'hi'}
#b= {'a':[1,2,3]}
#print(dic['name'])

#a={1:'a'}
#a[2] = 'b'
#a['name'] = 'pey'
#a[3] = [1,2,3]


#c=  {'name':'pey','phone':'01064797428','birth':'1222'}
#k = c.keys()
#print(k)
#k = list(c.keys())

#c=  {'name':'pey','phone':'01064797428','birth':'1222'}
#k = c.values()
#print(k)

#c=  {'name':'pey','phone':'01064797428','birth':'1222'}
#k = c.items()
#print(k)

#movie = {}
#mov = {'홍길동':{'베테랑':'★★★★★','암살':'★★★★'},'고길동':{'베테랑':'★★★★★','암살':'★★'}}
#name = mov.keys()
#print(name)
#star = mov.values()
#print(star)
#print(mov['홍길동']) #홍길동이 영화 뭐뭐 줫는지
#print(mov['홍길동']['암살']) #홍길동이 암살 몇점줬는지

#answer = input ("끝나고 서든할꺼야?")
#if answer.lower() == "yes" :
#    print("그러면 라임으로와")

#구구단을외자 구구단을외자
#for i in range(1,10):
#     for j in range(1,10):
#       print( i, " * ", j,  " = ", i*j )
        
     
import turtle
for steps in range(10):
    turtle.forward(100)
    turtle.right(360/10)
    for moresteps in range(10):
        turtle.forward(50)
        turtle.right(360/10)
                     
