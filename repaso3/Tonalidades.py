import random
tonalidades = ["C","F","G","A","Bb","Eb"]

verbo1=["miraron","conocieron","tropezaron","pelearon","encontraron"]
sustantivo1=["invierno","primavera","verano","otoño","vaciones"]
sustantivo2=["calor","frio","viento","cielo","dia"]
verbo2=["despertaba","lastimaba","acariciaba","iluminaba","tocaba"]
sustantivo3=["nueva","exitante","misteriosa","tenebrosa","peligrosa"]
sustantivo4=["historia","aventura","relacion","miraba"]
verbo3=["comenzaba","iniciaba","terminaba","explotaba","renacia"]


print('Se {} en {},cuando el {} la {} y entonces una {} {} {}'.format(
    verbo1[random.randint(0,4)],
    sustantivo1[random.randint(0,4)],
    sustantivo2[random.randint(0,4)],
    verbo2[random.randint(0,4)],
    sustantivo3[random.randint(0,4)],
    sustantivo4[random.randint(0,3)],
    verbo3[random.randint(0,4)]
))