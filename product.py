class Product(object):
  def __init__(self, price, name, weight, brand, status):
    self.price = price
    self.name = name
    self.weight = weight
    self.brand = brand
    self.status = status

  def display_product(self):
    print """
      Name: {}
      Price: {}
      Weight: {}
      Brand: {}
      Status: {}
    """.format(self.name, self.price, self.weight, self.brand, self.status)
    return self

  def sell(self):
    self.status = "Sold"
    print self.status
    return self

  def add_tax(self):
    self.sales_tax = 0.065
    if self.status == 'Sold':
      tax = self.price * self.sales_tax
      final_price = self.price + tax
      print "Final Cost = {}".format('%.2f' % final_price)
    return self

  def return_item(self, defective, used):
    self.defective = defective
    self.used = used
    if defective == 'defective':
      self.status = "Defective"
      self.price = 0
      print """
      New Status: {}
      New Price: {}
      """.format(self.status, self.price)
    elif used == 'used':
      self.status = "For Sale"
      self.price = self.price * .80
      print """
      New Status: {}
      New Price: {}
      """.format(self.status, self.price)


item_1 = Product(59.99, "God of War", 0.5, "PS4", "For Sale")
item_1.display_product().sell().add_tax()
item_1.return_item("defective", False)
item_2 = Product(59.99, "God of War", 0.5, "PS4", "For Sale")
item_2.return_item(False, "used")
item_2.display_product().sell().add_tax()
