class MensClothing:
    def Shirts(self,Allensoly):
        self.Allensoly = Allensoly
        print("ALLENSOLY SHIRTS ")
        print("TOP BRANDS")
        shirt1 = "Productdetails"
        print(shirt1)
        print("Allen Solly Men slim fit printed cut away collar casual shirt")
        price = 1201
        txt = "₹{}"
        print(txt.format(price))
        AllDetails = {
            "Packof": 1,
            "Style code": "ASSFQMOB902023",
            "Fit": "Slim",
            "Fabric": "Cotton Blind",
            "Color": "Black"
        }
        print(AllDetails)
        KeyFeatures = {
            "Slimfit": "3/4 Sleeve",
            "Collartype": "CutAway",
            "Pattern": "Printed",
            "Reversible": "No",
            "Faric care": "Machine Wash"
        }
        print(KeyFeatures)


    def Shirts1(self,peterengland):
        self.peterengland = peterengland
        print("PETERENGLAND SHIRTS")
        shirt2 = "ProductDetails"
        print(shirt2)
        print("PeterEngland Men Slim Ft Solid Spread Collar Casual Shirt")
        price = 1059
        txt = "₹{}"
        print(txt.format(price))
        AllDetails = {
            "Packof": 1,
            "Style code": "PCSFSSLPK66318",
            "Fit": "Slim",
            "Fabric": "Cotton Blind",
            "Color": "Black and White"
        }
        print(AllDetails)
        KeyFeatures = {
            "Slimfit": "Full Sleeve",
            "Collartype": "CutAway",
            "Pattern": "Printed",
            "Reversible": "No",
            "Faric care": "Machine Wash"
        }
        print(KeyFeatures)




    def Tshirts(self,Adidas):
        self.Adidas = Adidas
        print("TRENDINGS IN ADIDAS")
        Tshirt1 = "ProductDetails"
        print(Tshirt1)
        print(" Adidas Men Sporty Round Neck Polyster White T-Shirt")
        price = 749
        txt = "₹{}"
        print(txt.format(price))
        AllDetails = {
            "Packof": 1,
            "Style code": "FJ2212",
            "Fit": "Regular",
            "Fabric": "Polyster",
            "Color": "White"
        }
        print(AllDetails)
        KeyFeatures = {
            "Slimfit": "Short Sleeve",
            "Collartype": "Round Neck",
            "Pattern": "Sporty",
            "Reversible": "No",
            "Faric care": "Machine Wash as per tag"
        }
        print(KeyFeatures)


    def Tshirts1(self,Gucci):
        self.Gucci = Gucci
        print("GUCCI BRANDED TSHIRTS")
        Tshirt2 = "ProductDetails"
        print(Tshirt2)
        print("Gucci Men's Cotton T-Shirt Black_Medium")
        price = 1899
        txt = "₹{}"
        print(txt.format(price))
        AllDetails = {
            "Packof": 1,
            "Style code": "AJ0032",
            "Fit": "Regular",
            "Fabric": "Polyster",
            "Color": "Black"
        }
        print(AllDetails)
        KeyFeatures = {
            "Slimfit": "Short Sleeve",
            "Collartype": "Round Neck",
            "Pattern": "Sporty",
            "Reversible": "No",
            "Faric care": "Machine Wash as per tag"
        }
        print(KeyFeatures)


obj1 = MensClothing()
obj1.Shirts("Allensoly")
obj1.Shirts1("peterengland")
obj1.Tshirts("Adidas")
obj1.Tshirts1("Gucci")

