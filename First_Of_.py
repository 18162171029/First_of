fterminals=[]
def pterminals(chars):
    global fterminals
    fterminals.append(chars)

def getterminal(cha):
    global diction
    global non_terminals
    att=''
    a=diction[cha]
    if a[0] in non_terminals:
        getterminal(a[0])
    else:
        if '|' in a:
            ind1=a.index('|')
            att=a[0]+a[ind1+1:]
        else:
            att=a[0]
        return att


t=int(input("Enter the total no. of grammar: "))
gra=[]
temp=''
for i in range(t):
    temp=input(f"Enter the elements of {i+1} grammar: ")
    gra.append(temp)
    temp=''

non_terminals=[]
for i in gra:
    temp=i[0]
    non_terminals.append(temp)
    temp=''

diction={}

for i in range(len(gra)):
    diction[non_terminals[i]]=gra[i][3:]
    
tstr=''
for i in range(len(gra)):
    if gra[i][3] not in non_terminals:
        tstr=gra[i][3]
        if '|' in gra[i]:
            ind=gra[i].index('|')
            tstr+=gra[i][ind+1:]
            pterminals(tstr)
        else:
            pterminals(tstr)
    else:
        aa=getterminal(gra[i][3])
        pterminals(aa)
        
print('\n\n')
for i in range(len(fterminals)):
    print(f'First({non_terminals[i]}) -> {fterminals[i]}')
