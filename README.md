# **Repaso Python**
![Python](/img/logo.jpg)
```python
    # fue creado por Guido Van Rossum a comienzos de los 90 
```
Python es un lenguaje intepratado y de alto nivel, ¿Pero porque de alto nivel?, esto se debe a que su sintaxis es muy paracida al lenguaje humano.
Ademas este lenguje es orientado a objetos , por lo que si venimos de otros lenguajes como java o c++ los conceptos son iguales para todos ,aunque puedes variar en algunos terminos.
Es un lenguaje intepretado esto quiere decir que requiere de un interprete , mas no se compila .
### **Diferencias entre compilación e interpretación** 
Ok quiza sea un poco complicado , lo explicare a continuación :
La palabra compilacion quiere decir que convierte tu codigo fuente a binario o lenguaje que entienda la maquina para ejecutarlo , un ejemplo claro es el siguiente
```c++
    #include<istream>
    using namespace std;
    int main(){
        cout<<"Esto se compilará a 0 y 1 ";
        return 0;
    }
```
En el caso de java es muy interesante ya que primero se compilara dependiendo de S.O y luego gracias a la maquina virtual del java JVM o JRE se interpretara

```java
    public class Java{
        public static void main(String[] args) {
            System.out.println("Esto se compilará a bitcode y luego lo interpretara el JRE");
        }
    }
```
Entonces los lenguajes compilados necesitan de un programa o en linux el mismo sistema lo compila pero en window se necesita en el caso del c++ gcc , en el caso de java el jdk compilara a algo llamado bitcode que es un formato en hexadecial (**del 1 - 9 y a - f**) 
para poder compilar los lenguajes y ser entendidos por la computadora

En el caso de los lenguajes interpretados necesitan de un programa que traduzca directamente el codigo fuente, lo bueno de estos tipos de lenguajes es que al tiempo
de ser escritos las instruccuiones el lenguaje analiza y compila al mismo tiempo, aunque suelen ser mas lentos que un compilador ya que el interprete esta analizando en cada momento todas las lineas de codigo 



> **Los ejemplos se veran en este hermoso repositorio** 

### **Curiosidades**
A diferencia de otros lenguajes este no necesita colocarle el tipo de valor que sera la variable por que lo que se convierte un lenguaje **dinamicamente tipado** y esto hay que tratarlo con pinzas para algunos casos en particular que se veran el repositorio mas adelante

### **Configuración para windows**


Para mas referencias visite [AQUÍ](https://github.com/pystudent1913/ClasePiloto-Python/tree/master/01_tipos_de_datos_en_python)

```python
    # Autor : Thom Maurick Roman Aguilar
    # Estudiante de la carrera Ingeniería de Sistemas
```
https://bitbucket.org/josedurand/tallerplantilla



## PIP

[DESCARGA](https://bootstrap.pypa.io/get-pip.py)<br>

Pip es el sistema que nos ayudara en el control de paquetes y modulos en python , despues de descargarlo ejecutamos el siguiente comando en la terminal
````sh
    cd /c/ubicacion_archivo
````
````sh
    python get-pip.py
````

Para trabajar con BD

````sh
    pip3.7 install PyMySQL
````

Para desinstalar
````sh
    pip3.7 uninstall PyMySQL
````