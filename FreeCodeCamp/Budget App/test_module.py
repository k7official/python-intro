class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = (self.name).center(30, '*')
        display = f"{title}\n"
        total = 0
        for item in self.ledger:
            description = item["description"]
            amount = item["amount"]
            total += amount
            description_width = 23
            if len(description) > description_width:
                description = description[:23]
            line = description.ljust(23, ' ') + str("{:.2f}".format(amount)).rjust(7, ' ')
            display += f"{line}\n"
        display += f"Total: {total}"
        return display

    def deposit(self, amount, description=None):
        if description is None:
            description = ""
        record = {"amount": amount, "description": description}
        self.ledger.append(record)

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def withdraw(self, amount, description=None):
        if description is None:
            description = ""
        if self.check_funds(amount):
            record = {"amount": -abs(amount), "description": description}
            self.ledger.append(record)
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            amount = item["amount"]
            balance += amount
        return balance

    def transfer(self, amount, Category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {Category.name}")
            Category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False


def create_spend_chart(categories):
    number_of_categories = len(categories)

    def round_down(num, divisor):
        return num - (num % divisor)

    withdrawals = []
    total = 0
    for category in categories:
        withdrawal = 0
        for item in category.ledger:
            if item["amount"] < 0:
                withdrawal += abs(item["amount"])
        total += withdrawal
        withdrawals.append({"withdrawal": withdrawal, "name": category.name})
    for dict in withdrawals:
        percentage = dict["withdrawal"] / total * 100
        dict["percentage"] = round_down(percentage, 10)

    output = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        output += f"{i}|".rjust(4) + " "
        category_number = 1
        line = ""
        for dict in withdrawals:
            if dict != withdrawals[-1]:
                if i <= dict["percentage"]:
                    line += "o  "
                else:
                    line += "   "
            else:
                if i <= dict["percentage"]:
                    line += "o  \n"
                else:
                    line += "   \n"
        output += line

    output += "    -" + "---" * number_of_categories + "\n"
    longest_length = 0
    for dict in withdrawals:
        if (len(dict["name"]) > longest_length):
            longest_length = len(dict["name"])
    for i in range(0, longest_length):
        line = "     "
        for dict in withdrawals:
            if dict != withdrawals[-1]:
                if i < len(dict["name"]):
                    line += dict["name"][i].ljust(3)
                else:
                    line += "   "
            else:
                if i < len(dict["name"]):
                    if i != longest_length - 1:
                        line += dict["name"][i].ljust(3) + "\n"
                    else:
                        line += dict["name"][i].ljust(3)
                else:
                    if i != longest_length - 1:
                        line += "   \n"
                    else:
                        line += "   "
        output += line

    return output