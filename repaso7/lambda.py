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

help(studenties.sort)
# numbers = [2,5,-9,0,1,68,-8]
# print(numbers.sort())
# print(numbers)
# print(studenties.sort())
# print(studenties)