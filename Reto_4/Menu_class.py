class MethodPay:
  def __init__(self):
    pass

  def pay(self):
    raise NotImplementedError("Subclases deben implementar pagar()")

class Card(MethodPay):
  def __init__(self, number, cvv):
    super().__init__()
    self.number = number
    self.cvv = cvv

  def pay(self, mount,cvv2):
    if self.cvv==cvv2:
        print(f"Pagando {mount} con tarjeta {self.number[-4:]}")
    else:
        print("Contraseña incorrecta")

class Cash(MethodPay):
  def __init__(self, delivered_cash):
    self.delivered_cash = delivered_cash

  def pay(self, mount):
    if self.delivered_cash >= mount:
      print(f"Pago realizado en efectivo. Cambio: {self.delivered_cash - mount}")
    else:
      print(f"Fondos insuficientes. Faltan {mount - self.delivered_cash} para completar el pago.")


pago1 = Card("1234567890123456", 123)
pago2 = Cash(50000)

class Order:
    def __init__(self):
        self.list =[]

    def total_price(self):
        self.total = sum([item.subtotal for item in self.list])
        return self.total

    def set_total_price(self):
        self.total = sum([item.subtotal for item in self.list])
        self.total -= self.total * self.discount
        return self.total

    def add_item(self, item):
        self.list.append(item)

    def get_list(self):
        ([item.name for item in self.list])
        print("Nombre                 Precio")
        for item in self.list:
            print(f"{item.name} x {item.quantity}    {item.price}")
    def discount_n(self):
        if len(self.list)>1:
            for item in self.list:
                if item.menu_item=="MainDish":
                    self.discount=0.10
    def get_discount_n(self):
        return self.discount




class MenuItem:
    def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.subtotal= self.price*self.quantity
    
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    
    def set_price(self, price):
        self.price = price
    def get_price(self):
        return self.price
    
    def get_quantity(self):
        return self.quantity

    def get_subtotal(self):
        return self.subtotal


class Juice(MenuItem):
    def __init__(self, name, price,quantity,sugar):
        super().__init__(name, price,quantity)
        self.menu_item="Juice"
        self.sugar=sugar
    
    def set_sugar(self, sugar):
        self.sugar = sugar

    def get_sugar(self):
        return self.sugar

class Soup(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.menu_item="Soup"
        self.kind=kind
    
    def set_kind(self, kind):
        self.kind = kind

    def get_kind(self):
        return self.kind
     
class Soda(MenuItem):
    def __init__(self, name, price,quantity,sugar):
        super().__init__(name, price,quantity)
        self.menu_item="Soda"
        self.sugar=sugar

    def set_sugar(self, sugar):
        self.sugar = sugar

    def get_sugar(self):
        return self.sugar
        
class IceCream(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.menu_item="IceCream"
        self.kind=kind

    def set_kind(self, kind):
        self.kind = kind

    def get_kind(self):
        return self.kind
        
class Beer(MenuItem):
    def __init__(self, name, price,quantity,brand):
        super().__init__(name, price,quantity)
        self.menu_item="Beer"
        self.brand=brand
    
    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand
        
class Sandiwch(MenuItem):
    def __init__(self, name, price,quantity,protein):
        super().__init__(name, price,quantity)
        self.menu_item="Sandiwch"
        self.protein=protein
    
    def set_protein(self, protein):
        self.protein = protein

    def get_protein(self):
        return self.protein
        
class MainDish(MenuItem):
    def __init__(self, name, price,quantity,description):
        super().__init__(name, price,quantity)
        self.menu_item="MainDish"
        self.description=description

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
        
class Beef(MenuItem):
    def __init__(self, name, price,quantity,grams):
        super().__init__(name, price,quantity)
        self.menu_item="Beef"
        self.grams=grams

    def set_grams(self, grams):
        self.grams = grams

    def get_grams(self):
        return self.grams
        
class SideDish(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.menu_item="SideDish"
        self.kind=kind

    def set_kind(self, kind):
        self.kind = kind

    def get_kind(self):
        return self.kind
        
class Appetizer(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.menu_item="Appetizer"
        self.kind=kind

    def set_kind(self, kind):
        self.kind = kind

    def get_kind(self):
        return self.kind

orden=Order()

orden.add_item(Juice(name="Jugo de mango",price=2000,quantity=3,sugar="No"))
orden.add_item(Soup(name="Sancocho de pescado",price=4000,quantity=2,kind="Sancocho"))
orden.add_item(MainDish(name="Cerdo a la llanera",price=9000,quantity=2,description="Cerdo con salsa de la casa, arroz, patacon y ensalada"))
orden.add_item(Appetizer(name="Parfait",price=3500,quantity=2,kind="Dulce"))

orden.discount_n()
print("El precio total de la orden es:" + str(orden.total_price()))
orden.get_list()
print("Su descuento seria del:" +str((orden.get_discount_n())*100) + "%")
pago1.pay(mount=orden.set_total_price(),cvv2=123)
pago2.pay(mount=orden.set_total_price())