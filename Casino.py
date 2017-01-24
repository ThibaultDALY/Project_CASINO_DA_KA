class CASINO(object):
    def __init__(self, roulette_tables, craps_tables, barmen, employee_wage, starting_cash, number_customers, returning_customers, bachelors_customers):
        self.roulette_tables = roulette_tables
        self.craps_tables = craps_tables
        self.barmen = barmen
        self.employee_wage = employee_wage
        self.starting_cash = starting_cash
        self.number_customers = number_customers
        self.returning_customers = returning_customers
        self.bachelors_customers = bachelors_customers

    def simulateEvening(self, ):
