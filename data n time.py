from datetime import date

today = date.today()

d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)


d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)