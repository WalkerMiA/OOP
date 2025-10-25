import pickle
class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_num = ""
        self.phone = ""
        self.email_id = ""
        self.balance = 0.0
        self.credit_card = []
        self.debit_card = []

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
        for card in self.credit_card:
            print("Credit Card(s):", card.card_num)
        for debt in self.debit_card:
            print("Debit Card(s):", debt.card_num)

    def add_credit_card(self, ccard):
        self.credit_card.append(ccard)
    def add_debit_card(self, dcard):
        self.debit_card.append(dcard)


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

customers = []
cards = []

def find_customer(customer_id):
    for x in customers:
        if x.cid == customer_id:
            return x
    return None
while 1:
    print("1. Create Customer")
    print("2. Create Card")
    print("3. Transfer Funds")
    print("4. Assign Cards")
    print("5. Display Customer Info")
    print("6. Display Card Info")
    print("7. Commit")
    print("8. Exit")

    option = input("Enter Option:")

    if option == "1":
        new_customer = Customer()
        new_customer.add_values_to_customer()
        customers.append(new_customer)
    elif option == "2":
        new_card = Card()
        new_card.add_card()
        cards.append(new_card)
    elif option == "3":
        sender_id = input("Enter Customer ID:")
        recipient_id = input("Enter Customer ID:")
        sender = find_customer(sender_id)
        recipient = find_customer(recipient_id)

        if sender and recipient:
            amount = float(input("Enter Amount to Transfer:"))
            sender.debit_from(amount)
            recipient.credit_to(amount)
        else:
            print("One or both customer IDs do not match.")
    elif option == "4":
        cid = input("Enter Customer ID:")
        customer = find_customer(cid)
        if customer:
            card_type = input("Credit or Debit:").lower()
            for x in cards:
                if x.card_type.lower() == card_type:
                    x.display_card_info()

            selected_card_num = input("Enter Card Number:")
            for x in cards:
                if x.card_num == selected_card_num and x.card_type.lower() == card_type:
                    if card_type == "debit":
                        customer.add_debit_card(x)
                    elif card_type == "credit":
                        customer.add_credit_card(x)
                    break
            else:
                print("Card not found.")
        else:
            print("Customer not found.")
    elif option == "5":
        cust = input("Enter Customer ID:")
        for x in customers:
            if x.cid == cust:
                x.display_cust_info()
    elif option == "6":
        card_num = input("Enter Card Number:")
        for x in cards:
            if x.card_num == card_num:
                x.display_card_info()
    elif option == "7":
        f1 = open("cust_and_cards.dat", "wb")
        pickle.dump({"customers": customers, "cards": cards}, f1)
        f1.close()
    elif option == "8":
        break
