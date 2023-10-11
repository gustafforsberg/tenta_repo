


print('Beräknar differansen av jämna/udda tal....')



udda_lista = []
jamn_lista = []


for i in range(1, 2001, 2):
   udda_lista.append(i)



for i in range(2, 2002, 2):
   jamn_lista.append(i)

summa_udda = sum(udda_lista)
summa_jamn = sum(jamn_lista)




print(f'Differancen = {summa_jamn - summa_udda}')