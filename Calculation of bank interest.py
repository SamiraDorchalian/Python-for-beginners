def calc_bank_investment(initial_money, num_of_years, rate=0.2):
    result = initial_money

    for i in range(num_of_years):
        result *= (1 + rate)

    return result

print(calc_bank_investment(num_of_years=3, initial_money=1000))
