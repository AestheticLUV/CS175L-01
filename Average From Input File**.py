#CS-175LAB
#Jarek Torres
#Average From Input File with Exception Handling



#It should handle any IOError exception that are rasied when the file is opened and data is read from it
#It should handle any ValueError exceptions that are raised when the items that are read from the file are converted to a number
def main():
    count = 0
    #total = 0 
    average = 0
    try:
        file = open("numbers.txt", 'r')
        num1 = float(file.readline(4))
        num2 = float(file.readline(8))
        num3 = float(-99)
        
            
        
        for files in file:
            #total = num1 + num2 + num3
            a = num1+num2
            b = a+num3
            count = num1 + num2 + num3
            #count= +1 
            average = count/3
            print('\n') #used for spacing 
            print(f'I read in 1 number(s) Current number is: {num1:.2f} Total is: {num1:.2f}')
            print(f'I read in 2 number(s) Current number is: {num2:.2f} Total is: {a:.2f}')
            print(f'I read in 3 number(s) Current number is: {num3:.2f} Total is: {b:.2f}')
            print(f'Average: {average}')
            
       
    except IOError:
        print("File could not open try again!") #prints this when it has problems open the txt.file

    except ValueError:
        print("No number found in file try again!") #prints this when the txt has a non-number in it
    
    file.close()
        
if __name__ == '__main__':
    main()
