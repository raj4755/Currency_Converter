with open('currency.txt') as f:
    lines = f.readlines()

currencydict = {}

for line in lines:
    parsed = line.split('\t')
    currencydict[parsed[0]] = parsed[1]


# print(currencydict)
try:
    amount = int(input("Enter amount\n"))
except Exception:
    print("Please Enter Amount in Numbers")
print("Enter the Country you want to convert amount\n")

[print(item) for item in currencydict.keys()]
try:
    country = input("\nEnter one of these\n")
except Exception:
    print("Please Enter Country name Correctly")
print(f"{amount} INR is equal to {amount * float(currencydict[country])} {country}")

print("Thanks for using my currency converter ")
print("See you next time")
