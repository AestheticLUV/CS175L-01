#CS-175L-01
#Jarek Torres
#Average and Grade.py




score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))
score4 = float(input("Enter score 4: "))
score5 = float(input("Enter score 5: "))
    
total = score1 + score2 + score3 + score4 + score5 

def cal_average(avg):   
    added = total / 5                                                           
    return added
def determine_grade(grade):
    if grade >= 90 and grade <= 100:
        return("A")
    elif grade >= 80 and grade <= 89:
        return("B")
    elif grade >= 70 and grade <= 79:
        return("C")
    elif grade >= 60 and grade <= 69:
        return("D")
    else:
        if grade < 60:
            return("F")

print()           
print("Score" "\t",              "\t" "Numeric Grade""\t", "Letter Grade")
print("-------------------------------------------------")
print("score 1:","\t",score1,"\t","           ",determine_grade(score1))
print("score 2:","\t",score2,"\t","           ",determine_grade(score2))
print("score 3:","\t",score3,"\t","           ",determine_grade(score3))
print("score 4:","\t",score4,"\t","           ",determine_grade(score4))
print("score 5:","\t",score5,"\t","           ",determine_grade(score5))   
print('Average score:' "\t",cal_average(total))


ask = input("Enter" + "yes" + "if you would like to do another calculation: ")
while ask == "yes" or ask == "YES":
        score1 = float(input("Enter score 1: "))
        score2 = float(input("Enter score 2: "))
        score3 = float(input("Enter score 3: "))
        score4 = float(input("Enter score 4: "))
        score5 = float(input("Enter score 5: "))
        print()           
        print("Score" "\t",              "\t" "Numeric Grade""\t", "Letter Grade")
        print("-------------------------------------------------")
        print("score 1:","\t",score1,"\t","           ",determine_grade(score1))
        print("score 2:","\t",score2,"\t","           ",determine_grade(score2))
        print("score 3:","\t",score3,"\t","           ",determine_grade(score3))
        print("score 4:","\t",score4,"\t","           ",determine_grade(score4))
        print("score 5:","\t",score5,"\t","           ",determine_grade(score5))   
        print('Average score:' "\t",cal_average(total))
        break