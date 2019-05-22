import math
import statistics
from functools import reduce
def area(radius):
    return math.pi*(radius**2)

rds = [1,2,3,4,5]

# forma común y salvaje pero pasable
#agg :v
rdsR=[area(item) for item in rds]

#forma chida como los hombres :v
rdsR2 = list(map(area,rds))

print(rdsR,rdsR2)

# en celsius
temps = [('Berlin',29),('Cairo',36),('Buenis aires',19),('Los angeles',26)]

#convertir  en fahrenheit
newTemps = list(map(lambda tp : (tp[0],(9/5)*tp[1] + 32),temps))

print('Celcius',temps)
print('Fahrenheit',newTemps)

############################################################


data = [1.3,2.7,0.8,4.1,4.3,-0.1]

avg = statistics.mean(data)

# valores que estan por encima de la media
newData = list(filter(lambda element:element>avg,data))
print(newData)

# Remove missing data

countries = ['','Peru','Argentina','','Brazil','','']

newContries = list(filter(None,countries)) # Esto no filtrará todos los valores que se tratan como falsos en una configración booleana que son las cadenas vacias ,0 , listas disccionarios tuplas vacias , es decir se eliminaran todos los datos que se toman como falso
# newContries = list(filter(lambda country :country is not '',countries))

print(newContries)

################

data_2 = [1,2,3,4,5]

var= reduce(lambda x,y:x+y,data_2)
print(var)