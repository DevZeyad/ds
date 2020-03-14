availableNotas = [100.00,50.00,20.00,10.00,5.00,2.00,1.00]
Amount = int(input())

for Nota in availableNotas:
    print(int(Amount/Nota),"nota(s) de R$",Nota)
    Amount %= Nota