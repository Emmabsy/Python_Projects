class Investment:

    def __init__(self, principal, interest):
        self._principal = principal
        self._interest = interest/100

    def value_after(self, years):
        return self._principal * (1 + self._interest) ** years

    def getPrincipal(self):
        return self._principal

    def setPrincipal(self, principal):
        self._principal = principal

    def __str__(self):
        return "Principal - " + str(self._principal) + \
               "\nInterest - " + str(self._interest)
