a=input('\nEnter First Player Name:\t')
b=input('\nEnter Second Player Name:\t')
char=['X','O']
print(a,'\tYou are player',char[0] )
print(b,'\tYou are player',char[1])
ls=[1,2,3,4,5,6,7,8,9]
i=0
while i<9:
    print(ls[i],'',end='')
    if ls[i]%3==0:
        print()
    i=i+1
i=0
j=0
while j<4:
    print(a,'Play')
    raz=int(input('Enter Your position Number'))
    ls[raz-1]=char[0]
    i=0
    k=0
    while i<3:
        l=0
        while l<3:
            print(ls[k],'',end='')
            l+=1
            k+=1
        print()
        i+=1
    if ls[0]==ls[1]==ls[2] or ls[0]==ls[3]==ls[5] or ls[0]==ls[4]==ls[8] or ls[1]==ls[4]==ls[7] or ls[2]==ls[5]==ls[8] or ls[2]==ls[4]==ls[6] or ls[3]==ls[4]==ls[5] or ls[6]==ls[7]==ls[8] or ls[0]==ls[3]==ls[6]or ls[3]==ls[6]==ls[0]:
        print(a,'Winner')
        break

    print(b,'Your turn')
    t=int(input("Enter Your position"))
    ls[t-1]=char[1]
    k=0
    i=0
    while i < 3:
        l=0
        while l<3:
            print(ls[k], '', end='')
            l+=1
            k+=1
        print()
        i = i + 1
        if ls[0] == ls[1] == ls[2] or ls[0] == ls[3] == ls[5] or ls[0] == ls[4] == ls[8] or ls[1] == ls[4] == ls[7] or ls[2] == ls[5] == ls[8] or ls[2] == ls[4] == ls[6] or ls[3] == ls[4] == ls[5] or ls[6] == ls[7] == ls[
            8]or ls[0]==ls[3]==ls[6]or ls[3]==ls[6]==ls[0]:
            print(b, 'Winner')
            break
    else:
        print("draw match")
