#data=['a','b','c',['abcd','efg']]
#print(data[0])
#print(data[-1])
#print(data[-1][-1])
#b=[1,2,3]
#c=['Life','is','too','short']
#print(b+c)
#f = b+c
#print(f)
#print(b*3)
#guests = ['a','b','c','d']
#guests[0] = 'greenjoa'
#guests[1] = ['greenjoa1','greenjoa2']
#guests[1:2] = ['greejoa1','greenjoa2']
#print(guests)
#data = ['ID1','ID2','ID3']
#print(data)
#data.insert(1,'12345')
#data.insert(3,'green')
#data.insert(5,'joa')
#print(data)
#이름/전화번호
#infor = ['이택용,010123451234','민경태,01056785678','홍춘기,01064797428']
#data.insert(2,infor[0])
#data.insert(5,infor[1])
#data.insert(8,infor[2])
#print(data)
#for steps in range(9) :
#    print(data[steps])
#data2 = range(4)
#print(data2)
#for steps in range(4) :
#    print(steps)

scores = [55,24,63,11,95,84,73]
scores.extend([44,63])
scores.append([44,63,21])

print(scores)
scores.reverse()
print(scores)
print(scores[0:5])
data = ['a','b','c',['abcd','efg']]

for steps in data :
    if isinstance(steps,list) :
        for step in steps :
            print(steps)
    else :
        print(steps)

