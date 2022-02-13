import random 

print('Enter the number of friends joining (including you):')
a=0
numb=int(input())
if not numb>0 :
    print('\nNo one is joining for the party\n')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    names={}
    for i in range(numb):
        names[input()]=a
    print('Enter the total bill value:\n')
    tot_val=int(input())
    a=tot_val/numb
    for i in names.keys():
        names[i]=int(a) if int(a)==a else round(a,2)
    dicision=input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if dicision=='Yes':
        lucker=random.choice(list(names.keys()))
        print(f'\n{lucker} is lucky one\n')
        names[lucker]=0
        a=tot_val/(numb-1)
        for i in names.keys():
            if not i==lucker:
                names[i]=int(a) if int(a)==a else round(a,2)
    else : print('No one is going to be lucky')
    print(names)