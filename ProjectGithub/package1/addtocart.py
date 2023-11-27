def calculate_total_amount(cart):
    totalcost = 0
    for item in cart:
        totalcost += item['price'] * item['quantity']
    print(f"Total cost: ",[totalcost])
    return totalcost

class ShoppingCart:
    def __init__(self):
        self.cart = []
    def AddProducts(self,productname,price):
        self.cart.append({"productname": productname,"price":price})
    def Viewcart(self):
        if not self.cart:
            print("Cart is Empty")
        else:
            print("Your Cart: ")
            for item in self.cart:
             print(f"{item['productname']} - ₹{item['price']}")
cart = ShoppingCart()
cart.AddProducts("Allensolly",1021)
cart.AddProducts("Gucci",1899)
cart.Viewcart()
cart = [{'price' : 1021,'quantity': 1},{'price':1899,'quantity':2}]
calculate_total_amount(cart)


