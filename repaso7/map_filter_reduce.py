import math

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