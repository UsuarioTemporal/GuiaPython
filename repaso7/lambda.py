# from nuevo_paquete.operaciones import *
# o = Operation(45,4)
# print(o.sumar())
# print(o.resta())

g= lambda x :3*x+1
print(g(3))

#supongamos que necesitamos conbinar los nombres y apellidos de un un formulario

full_name = lambda fn,ln : fn.strip().title()+' '+ln.strip().title()

print(full_name('thom ', ' roman '))


#cambiar el orden de apellido luego los nombres

studenties = [' thom roman',' fabrizio condori ','erick chavo',' niuton sumas',' cristian prro']

# help(studenties.sort)
# numbers = [2,5,-9,0,1,68,-8]
# print(numbers.sort())
# print(numbers)
# help(map())
studenties=list(map(lambda item:item.strip(),studenties))
# print(studenties.sort())
studenties=list(map(lambda person:' '.join(person.split(' ')[::-1]),studenties))
# studenties.sort(key=lambda name:name.split(' ')[-1].lower())
studenties.sort(key = lambda person :person)
print(studenties)

# Escribiendo una funcion que hace funciones

def buildFunction(a,b,c):
    return lambda x : a*x**2+b*x+c
f = buildFunction(2,3,-5)
print(f(5))
print(f(4))
print(f(-5))