# Reto_4
# Programación Orientada a Objetos - UNAL



## Reto 4.1

Para este reto se utilizaron varias de las mismas clases, excepto que ahora rectangulo hereda de una clase mayor, siendo esta ultima figura, y se le añaden otra subclase mas a figura, siendo esta triangulo, y triangulo tiene varias subclases, siendo estas las clases que pueden existir

### Clase Punto
Veremos como se los metodos de la clase punto, que seria reiniciarlo (ponerlo de nuevo en 0,0), moverlo (cambiarle las coordenadas a un nuevo x,y), y calcular la distancia entre dos puntos propuestos

### Clase Linea 
Veremos como se los metodos de la clase linea, en este caso: calcular la pendiente, calcular la longitud de la linea (utlizando el teorema de pitagoras), si intersecta con el eje x y donde intersecta y si intersecta con el eje y donde intersecta

### Clase figura
La clase figura tiene los siguientes atributos: vertices (como variable tipo lista); aristas (como variable tipo lista); angulos internos (como variable tipo lista); y los metodos: calcular area; calcular perimetro y calcular angulos internos; todo esto se puede ver heredado a las clases triangulo y rectangulo; para la funcion de calcular perimetro como todos las figuras se calculan igual, simplemente se establece en la clase de figura y se llamara desde la figura que sea necesario

### Clase rectangulo
Lo importante a mencionar aqui es que ya tiene por defecto la lista de angulos internos, que serian todos de 90°, ya que un rectangulo siempre tendra esos angulos internos, y ya que cuadrado hereda de rectangulo, va pasar lo mismo para este; para la funcion de calcular el area, como es igual para el rectangulo y cuadrado, simplemente se establece en rectangulo
### Clase triangulo
Lo importante para esta clase es encontrar los angulos y el area, para calcular el area se utiliza el teorema de Heròn (se basa en escribir la formula de un triangulo de una manera que se calcule sin necesidad de encontrar ningun angulo, se halla reescribiendo el area de el triangulo), y para los angulos del triangulo se utiliza el Teorema del coseno, despejando el angulo, dandonos asi el angulo que se tiene enfrente de la linea a la que se le esta hallando principalmente el angulo 
```python
import math


import math


class Point:
    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y
    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y
    def reset(self):
        self.x = 0
        self.y = 0
    def compute_distance(self, point)-> float:
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance

first_point = Point(x=1, y=2)
second_point = Point(x=2, y=3)



class Line:

    def __init__(self,startp,endp):
        self.startp=startp
        self.endp=endp

    def compute_lenght(self):
        self.lenght=(((self.endp.y-self.startp.y))**2+((self.endp.x-self.startp.x)**2))**0.5
        return self.lenght
    def compute_slope(self):
        if self.startp.x!=self.endp.x:
            self.slope=(self.endp.y-self.startp.y)/(self.endp.x-self.startp.x)
        else:
            self.slope=0
        return self.slope
    def compute_degree(self):
        if self.startp.x!=self.endp.x:
            self.degree=math.degrees(math.atan2((self.endp.y-self.startp.y),(self.endp.x-self.startp.x)))
        else:
            self.degree=0
        return self.degree
    
    def compute_vertical_cross(self):
        self.intersecty=self.startp.y-(self.slope*self.startp.x)
        if self.startp.x<=0<=self.endp.x:
            return self.intersecty
        else:
            return False

    def compute_horizontal_cross(self):
        if self.startp.x!=self.endp.x:
            self.intersectx=(self.startp.y*0-self.intersecty)/self.slope

        else:
            self.intersectx=self.startp.x

        if self.startp.y<=0<=self.endp.y:
            return self.intersectx
        else:
            return False

Linea0=Line(startp=first_point,endp=second_point)
print("La longitud de la linea es: " + str(Linea0.compute_lenght()))
print("La pendiente de la linea es: " + str(Linea0.compute_slope()) + ", y eso con un angulo de: " + str(Linea0.compute_degree()) + "°")

if (Linea0.compute_vertical_cross())== False:
    print("La linea no corta el eje Y")
else:
    print("La linea corta en Y en:" + str(Linea0.compute_vertical_cross))

if (Linea0.compute_horizontal_cross())== False:
    print("La linea no corta el eje X")
else:
    print("La linea corta en X en:" + str(Linea0.compute_vertical_cross))


class Shape:
    def __init__(self,edges,vertices):
        self.edges=edges
        self.vertices=vertices

    def compute_area(self):
        raise NotImplementedError("Subclases deben implementar calcular area()")
    
    def compute_perimeter(self):
        a=0
        for const in range(len(self.edges)):
            a+=(self.edges[const]).compute_lenght()
        self.perimeter=a
        return self.perimeter
    
    def compute_inner_angles(self):
        raise NotImplementedError("Subclases deben implementar calcular angulos internos()")
    
    def set_vertices(self, vertices):
        self.vertices=vertices
    
    def get_vertices(self):
        return self.vertices
    
    def set_edges(self, edges):
        self.edges=edges
    
    def get_edges(self):
        return self.edges
    
    def get_perimeter(self):
        return self.perimeter
    
    def get_inner_angles(self):
        return self.inner_angles

    
class Triangle(Shape):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)

    def compute_area(self):
        a=0
        for const in range(len(self.edges)):
            a+=(self.edges[const]).compute_lenght()
        self.perimeter=a
        s=(self.perimeter)/2
        self.area=math.sqrt(s*(s-((self.edges[0]).compute_lenght()))*(s-((self.edges[1]).compute_lenght()))*(s-((self.edges[2]).compute_lenght())))
        return self.area

    def compute_inner_angles(self):
        a = self.edges[0].compute_lenght()
        b = self.edges[1].compute_lenght()
        c = self.edges[2].compute_lenght()
        angle_alpha = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle_beta = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle_gamma = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
        self.inner_angles = [angle_alpha, angle_beta, angle_gamma]
        return self.inner_angles

class Iscoceles(Triangle):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)


class Equilateral(Triangle):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)
        self.inner_angles=[60]*3

class Scalene(Triangle):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)

class Rectangle(Triangle):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)

class Rectangle(Shape):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)
        self.inner_angles=([90]*4)

    def compute_area(self):
        a=1
        for const in range(len(self.edges)):
            a*=(self.edges[const]).compute_lenght()
        self.area=math.sqrt(a)
        return self.area

class Square(Rectangle):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)
        self.inner_angles=([90]*4)


tp1=Point(x=1,y=2)
tp2=Point(x=3,y=5)
tp3=Point(x=5,y=2)

tL1=Line(startp=tp1,endp=tp2)
tL2=Line(startp=tp2,endp=tp3)
tL3=Line(startp=tp3,endp=tp1)

tedges1=[tL1,tL2,tL3]
tvertices1=[tp1,tp2,tp3]

triangulo1=Iscoceles(edges=tedges1,vertices=tvertices1)
print("Los angulos internos del triangulo son:" + str(triangulo1.compute_inner_angles()))


rp1=Point(x=7,y=2)
rp2=Point(x=7,y=5)
rp3=Point(x=12,y=5)
rp4=Point(x=12,y=2)

rL1=Line(startp=rp1,endp=rp2)
rL2=Line(startp=rp2,endp=rp3)
rL3=Line(startp=rp3,endp=rp4)
rL4=Line(startp=rp4,endp=rp1)

redges1=[rL1,rL2,rL3,rL4]
rvertives1=[rp1,rp2,rp3,rp4]

rectangulo1=Rectangle(edges=redges1,vertices=rvertives1)

print("El perimetro del triangulo es de:" + str(triangulo1.compute_perimeter()))
print("El area del triangulo es de:" + str(triangulo1.compute_area()))
print("El area del rectangulo es de:" + str(rectangulo1.compute_area()))
print("El perimetro del rectangulo es de:" + str(rectangulo1.compute_perimeter()))
```


# Restaurante

Ahora nos encontramos en una situacion de un restaurante donde debemos calcular la cuenta de la orden de un cliente

### Diagrama de clases

Antes de empezar a programar debemos plantear como seria la estructura de lo que vamos a programar y como se relacionan las clases entre ellas, asi obtenemos el siguiente diagrama de clases

Empezamos con la clase orden, que se compone de items del menu; en esta clase se pueden, añadir items, calcular el total de la cuenta y mostrar la cuenta

La siguiente clase, los items del menu, que se compodria de nombre, precio y cantidad, y que puede calcular el sub_total, que seria la cantidad del item por el precio del item

Y luego estan las subclases qye heredan de items del menu, que serian las categorias que podria a llegar un menu, y que cada una tiene sus caracteristicas propias
![image](https://github.com/JOUNAL/Reto3/blob/main/Reto_3/Diagrama2(1).png)

Y este seria el codigo, con cada una de las clases y subclases definidas, y lo que seria un ejemplo del una orden de un cliente
```python
class Order:
    def __init__(self):
        self.list =[]

    def total_price(self):
        self.total = sum([item.subtotal for item in self.list])
        return self.total

    def discount(self, discount):
        self.total = sum([item.subtotal for item in self.list])
        self.total -= self.total * (discount / 100)
        return self.total

    def add_item(self, item):
        self.list.append(item)

    def get_list(self):
        print("Nombre                 Precio")
        for item in self.list:
            print(f"{item.name} x {item.quantity}    {item.price}")


class MenuItem:
    def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.subtotal= self.price*self.quantity

class Juice(MenuItem):
    def __init__(self, name, price,quantity,sugar):
        super().__init__(name, price,quantity)
        self.sugar=sugar

class Soup(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.kind=kind
        
class Soda(MenuItem):
    def __init__(self, name, price,quantity,sugar):
        super().__init__(name, price,quantity)
        self.sugar=sugar
        
class IceCream(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.sugar=kind
        
class Beer(MenuItem):
    def __init__(self, name, price,quantity,brand):
        super().__init__(name, price,quantity)
        self.brand=brand
        
class Sandiwch(MenuItem):
    def __init__(self, name, price,quantity,protein):
        super().__init__(name, price,quantity)
        self.protein=protein
        
class MainDish(MenuItem):
    def __init__(self, name, price,quantity,description):
        super().__init__(name, price,quantity)
        self.description=description
        
class Beef(MenuItem):
    def __init__(self, name, price,quantity,grams):
        super().__init__(name, price,quantity)
        self.grams=grams
        
class SideDish(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.kind=kind
        
class Appetizer(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.kind=kind

orden=Order()

orden.add_item(Juice(name="Jugo de mango",price=2000,quantity=3,sugar="No"))
orden.add_item(Soup(name="Sancocho de pescado",price=4000,quantity=2,kind="Sancocho"))
orden.add_item(MainDish(name="Cerdo a la llanera",price=9000,quantity=2,description="Cerdo con salsa de la casa, arroz, patacon y ensalada"))
orden.add_item(Appetizer(name="Parfait",price=3500,quantity=2,kind="Dulce"))

print("El precio total de la orden es:" + str(orden.total_price()))
orden.get_list()
```
El resultado de la terminal seria el siguiente
```
El precio total de la orden es:39000
Nombre                 Precio
Jugo de mango x 3    2000
Sancocho de pescado x 2    4000
Cerdo a la llanera x 2    9000
Parfait x 2    3500
```
