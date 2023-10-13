#Author: Gustaf Forsberg
#Date: 2023-10-13

print('Ei22 - Praktiskt prov ht23')



resistorer_str =  (input('Ange resistorer:')) # Tar emot input

if resistorer_str: #kollar om inputen har ett värde
   
   resistorer = []

   resistorer = resistorer_str.split() #splittar strängen på ' '

   resistorer = list(map(int, resistorer)) #gör om listan till intar


   parallell_resistorer = []

   for line in resistorer:                   #lägger 1/den inmatade resistansen i en ny lista
      parallell_resistorer.append(1 / line)

   print(f'Serieresistans: {sum(resistorer)} Ohm')       #skriver ut och sumerar
   print(f'Paralellresistans: {1 / sum(parallell_resistorer)} Ohm') #skriver ut och tar 1/ summan av "parallell listan"

else:
   print('Serieresistans: 0')
   print('Paralellresistans: 0')