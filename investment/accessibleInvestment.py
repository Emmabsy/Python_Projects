from investment import Investment

class AccessibleInvestment(Investment):

    def __init__(self, principal, interest):
        super().__init__(principal, interest)

    def withdraw(self, amount):
        new_principal = super().getPrincipal() - amount
        super().setPrincipal(new_principal)

# Using the classes

inv = AccessibleInvestment(10000, 6)
print(inv)
print(inv.value_after(20))
inv.withdraw(2000)
print(inv)
print(inv.value_after(20))
