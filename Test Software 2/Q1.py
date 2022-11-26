class Customer:
    list_of_customers = []
    customer_x = 0

    def __init__(self, first_name, last_name, loy_points):
        Customer.customer_x = Customer.customer_x + 1
        self.first_name = first_name
        self.last_name = last_name
        self.loy_points = loy_points

    def increase(self, add_loy):
        self.loy_points = self.loy_points + add_loy
        print(f"{self.first_name} {self.last_name} total points = {self.loy_points}")


# Main Program
# a


c1 = Customer("Mia", "Fluffins", 2)
c2 = Customer("Abdul", "Ammar", 1)
# b


c1.increase(2)
c2.increase(4)
# c
print(f"Total number of Customers: {Customer.customer_x}")




