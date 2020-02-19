def maximum(mesures):
    list_index=[]
    grand=[]
    for k in range(len(mesures)):
        for i in mesures:
            if i > i+1:
                if mesures.index(i) not in list_index:
                    list_index.append(mesures.index(i))
            else:
                if mesures.index(i+1) not in list_index:
                    list_index.append(mesures.index(i+1))
    for y in range(3):
        grand.append(max(list_index))
        max(list_index).remove()
    
me=[10, 0, 5, 10, 30, 10, 20, 30]#1
mes=[60, 0, 5, 10, 30, 10, 20, 30]#0
mesures=  [-2, -24, -48, -34, -18, -19, -25, -31, -20, -28]#0
print(maximum(me))
print(maximum(mes))
print(maximum(mesures))