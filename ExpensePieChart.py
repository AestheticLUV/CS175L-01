#CS-175LAB
#Jarek Torres
#Expense Pie Chart 

from matplotlib import pyplot as plt

def main():
    items = []
    spend = []
    expense_file = open("expenses.txt","r")
    rows = expense_file.readlines()  # read all lines

    for line in rows:
        line = line.replace("Payment", " ")
        items.append(str(line.split()[0]))
        spend.append(int(line.split()[1]))
    plt.pie(spend, labels = items)
    plt.axis('equal')
    plt.title("Monthly Expenses")
    plt.show()
      
main()
