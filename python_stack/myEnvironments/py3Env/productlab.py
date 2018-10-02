class Product:
    def __init__(self, price, item_name, item_weight, item_brand, item_status):
        self.price = price
        self.item_name = item_name
        self.item_weight = item_weight
        self.item_brand = item_brand
        if item_status == "":
            self.item_status = "for sale"
        else:
            self.item_status = item_status
        
    def Sell(self):
        self.item_status = "sold"
        return self
    
    def AddTax(self, tax_amount):
        self.price += tax_amount
        return self
    
    def ReturnItem(self, reason_for_return):
        if reason_for_return == "defective":
            self.item_status = "defective"
            self.price = 0
        elif reason_for_return == "like_new":
            self.item_status = "for sale"
        elif reason_for_return == "opened":
            self.item_status = "used"
            self.price -= self.price * 0.20
        return self
    
    def Display_Info(self):
        print("===================================")
        print("        Price: ", self.price)
        print("    Item Name: ", self.item_name)
        print("       Weight: ", self.item_weight)
        print("        Brand: ", self.item_brand)
        print("       Status: ", self.item_status)
        print("===================================")

jeans = Product(30, "Levi's 501 Jeans", "3 pounds", "Levi's", "for sale")
jeans.AddTax(1).Sell()
jeans.Display_Info()

bomber_jacket = Product(70, "Leather Bomber Jacket", "5 pounds", "GAP", "for sale")
bomber_jacket.Sell().ReturnItem("like_new")
bomber_jacket.Display_Info()

shoes = Product(99, "Air Jordans", "2 pounds", "Nike", "defective")
shoes.Sell().ReturnItem("used").AddTax(2).Sell()

shirt = Product(55, "Pique Polo Shirt", "2 pounds", "Ralph Lauren", "used")
shirt.Display_Info()

slacks = Product(75, "Chino Pants", "3 pounds", "American Eagle", "for sale")
slacks.Sell().ReturnItem("opened").AddTax(5).Sell().ReturnItem("defective")
slacks.Display_Info()
