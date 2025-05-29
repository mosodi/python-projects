#Make a loan calculator to calculate intrest of a loan for a 10 year period using the for loop
#Starting amount $1000
#Year 1 interest = $1050.0, Year 10 interest  = $1628.89

initial_investment = 1000
interest_rate = 0.05  # 5% annual interest
current_balance = initial_investment
for year in range(1, 11, +1):
    interest_earned = current_balance * interest_rate
    current_balance += interest_earned
    print("Year", year, "interest earned is $",interest_earned )
print("Total = $",current_balance)


