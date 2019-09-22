
"""Input with no space"""

"""Dictionary for convert notes to number"""
table = {'C' : 1 ,'B#' : 1 , 'C#':2,'Db':2,'D':3 ,'D#':4,'Eb':4,'E':5,'Fb':5,'F':6,'E#':6,'F#':7,'Gb':7,'G':8,
'G#':9,'Ab':9, 'A':10, 'A#':11,'Bb':11,'B':12,'Cb':12 }
convertTable = { 1:'C', 2:'C#',3:'D',4:'D#',5:'E',6:'F',7:'F#',8:'G',9:'G#',10:"A",11:"A#",12:"B" }
print("Type 's' if you want to stop the adding notes ",end="\n\n")
take2 = 't'
musicNotes = []
count = 0
# testVar = input().split()
# print(testVar)
"""Find the this stuck infinite loop problem"""
# while take2!="s" :
#     take = input().split()
#     musicNotes.append(take)
    
#     take2 = "".join(take)
#     print("Take2=",take2 )
#     count += 1

"""Input all notes"""
while True :
    check = 0
    take = input().split()
    string = "".join(take)
    if not string.isspace():

    else: 
        if string == 's':
            #print("This should stop",string)
            break
        if string.isspace():
            pass
        else:
            for a in take:                
                if a not in table.keys():            
                    print("Please enter the NOTES in letters!!! ")
                    check = 1
                    break   
                
        if check == 0:    
            musicNotes.append(take)

Numeral = []
"""Convert Notes to numbers"""
for a in musicNotes:
    temp = []
    for b in a:               
        c = table[b]
        temp.append(c)        
    Numeral.append(temp)

ShiftNotes = []
SizeSpace = 3
convertNum = int(input( "Enter the half note to shift:  "))
print()
"""Shift and change them to notes"""
for a in Numeral:
    temp = []
    for b in a:
        ShiftRes = (b + convertNum) % 12
        if ShiftRes == 0:
            ShiftRes = 12
        try:
            c = convertTable[ShiftRes]
        except KeyError:
            print(ShiftRes,"Error")

        if len(c) == 2:
            c = c + (" ")*SizeSpace
        else:
            c = c + (" ")*(SizeSpace+1)
        temp.append(c)
    temp = "".join(temp)
    ShiftNotes.append(temp)

print("The Result")
for elem in ShiftNotes:
    print(elem)

    
