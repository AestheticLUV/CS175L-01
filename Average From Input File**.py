#CS-175LAB
#Jarek Torres
#Average From Input File

#NOTES
# The num3 would not print out the number thats why i put the -99 instead of float(file.readline()) #LINE 17
#The other numbers such as num1 and num2 print out perfect in the for loop



def main():

    file = open('numbers.txt', 'r')

    num1 = float(file.readline(4))
    num2 = float(file.readline(8))
    num3 = -99          #float(file.readline(13))  #I tried to print the line but it didnt print for me


    for files in file:
    #print(files)    
        total = num1 + num2 + num3
        a = num1+num2
        b = a+num3
        count = num1 + num2 + num3 
        average = count/3
        print(f'I read in 1 number(s) Current number is: {num1:.2f} Total is: {num1:.2f}')
        print(f'I read in 2 number(s) Current number is: {num2:.2f} Total is: {a:.2f}' )
        print(f'I read in 3 number(s) Current number is: {num3:.2f} Total is: {b:.2f}')
        print(f'Average: {average}')
        break
if __name__ == '__main__':
    main()