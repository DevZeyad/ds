#This is an uri online judge problem solution
#you have to read int value and calculate the smallest possible number of bank notes in which the value may be decomposed
#Actually , loved this idea :D
#So i decided to post my solution as a first github code for me

availableNotas = [100.00,50.00,20.00,10.00,5.00,2.00,1.00]
Amount = int(input("Enter The Amount Please: "))

for Nota in availableNotas:
    print(int(Amount/Nota),"nota(s) de R$",Nota)
    Amount %= Nota
