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