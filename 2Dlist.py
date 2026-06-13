nums = [1,2,3,4,5]
print(nums)

TwoDLists = [[1,2,3],[4,5,6],[7,8,9]]
print(TwoDLists)
print(len(TwoDLists))
print(TwoDLists[0][0])
print(TwoDLists[0])

for i in TwoDLists:
    print(i)
List2D = []
#ask user ho many rows and colums and the create a 2D Lists
rows = int(input("Enter the number"))
cols = int(input("Enter the nunmber"))
for i in range(rows):
    temp = []
    for j in range(cols):
        temp.append("🤯")
        
    List2D.append(temp)

for e in range(rows):
    for t in range(cols):
        print(List2D[e][t],end =" ")
    print("\n")

#homework

List2D = []
#ask user ho many rows and colums and the create a 2D Lists
rows = 3
cols = 3
for i in range(rows):
    temp = []
    for j in range(cols):
        temp.append("🫢")
        
    List2D.append(temp)

for e in range(rows):
    for t in range(cols):
        print(List2D[e][t],end =" ")
    print("\n")



