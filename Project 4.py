class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_num = ""
        self.phone = ""
        self.email_id = ""
        self.balance = 0.0
        self.credit_card = []
        self.debit_card = ""

    def add_values_to_customer(self):
        self.cid = input("Enter Customer ID:")
        self.cname = input("Enter Customer Name:")
        self.acc_num = input("Enter Account Number:")
        self.phone = input("Input Phone Number:")
        self.email_id = input("Enter email:")
        self.balance = float(input("Enter balance:"))

    def debit_from(self, sub_amount):
        self.balance -= sub_amount
        return

    def credit_to(self, add_amount):
        self.balance += add_amount
        return

    def display_cust_info(self):
        print("Customer ID:", self.cid)
        print("Customer Name:", self.cname)
        print("Account Number:", self.acc_num)
        print("Phone Number:", self.phone)
        print("Email:", self.email_id)
        print("Balance:", self.balance)
        for x in self.credit_card:
            print("Credit Card(s):", x.card_num)
        print("Debit Card:", self.debit_card)

    def add_credit_card(self, ccard):
        self.credit_card.append(ccard)
    def add_debit_card(self, dcard):
        self.debit_card += dcard

class Card:
    def __init__(self):
        self.card_type = ""
        self.card_num = ""
        self.cvv = ""
        self.expiration = ""
        self.balance = 0.0
    def add_card(self):
        self.card_type = input("Enter Card Type:")
        self.card_num = input("Enter Card Number:")
        self.cvv = input("Enter CVV:")
        self.expiration = input("Enter Expiration Date:")
    def display_card_info(self):
        print("Card Type:", self.card_type)
        print("Card Number:", self.card_num)
        print("CVV:", self.cvv)
        print("Expiration Date:", self.expiration)
        print("Balance:", self.balance)

c1 = Customer()
c1.add_values_to_customer()
card1 = Card()
card1.add_card()
card1.display_card_info()
card2 = Card()
card2.add_card()
card2.display_card_info()
c1.add_debit_card(card1)
c1.add_credit_card(card2)
c1.display_cust_info()

c2 = Customer()
c2.add_values_to_customer()


d = float(input("Enter amount to debit:"))
c1.debit_from(d)
c1.display_cust_info()

c = float(input("Enter amount to credit:"))
c2.credit_to(c)
c2.display_cust_info()