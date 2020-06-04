with open('currency.txt') as f:
    lines = f.readlines()

currencydict = {}

for line in lines:
    parsed = line.split('\t')
    currencydict[parsed[0]] = parsed[1]


# print(currencydict)
amount = int(input("Enter amount\n"))
print("Enter the Country you want to convert amount\n")

[print(item) for item in currencydict.keys()]

country = input("\nEnter one of these\n")

print(f"{amount} INR is equal to {amount * float(currencydict[country])} {country}")

print("Thanks for using my currency converter ")
print("See you next time")