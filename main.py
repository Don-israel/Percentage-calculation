# take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
btech = int(input("btech :"))
history = int(input("history:"))
# Let's calculate the percentage of marks
sum = math+english+science+btech+history
print("sum of math,english,science,btech and history")

perc = (sum/600)*100

print(end="Percentage Mark = ")
print(perc)
