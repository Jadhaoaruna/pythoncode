var1=int(input("enter the number"))
print("var1:",var1)
var2=int(input("enter the number"))
print("var2:",var2)

#addition of two number
addition=var1+var2
print("addition:",var1+var2)

#square of first number
print("square of var1",var1*var1)

#first number raised to number second number

print("var1 raised to var2",var1**var2)

#2) Accept String from user and output upper case of the input string 
str1=str(input("enter the string: "))
print("string upper: ",str1.upper())

#3) Define a variable named "raise_salary_percentage" and get the salary raise 
#percentage from the user, Now apply the raise to an employee
#with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
#print the incremented salary to the console

raise_salary_percentage = float(input("enter the salary raised percentage: "))

name ="aruna"
existing_salary=900 
raised_salary=(existing_salary*raise_salary_percentage)/100
print("raised_salary:",raised_salary)
new_salary=existing_salary+raised_salary
print("new_salary",new_salary)

#Get the height from the user in cms and display the user height back to console
#in foot/feet and inches
height = float(input("enter the height in cm"))
print("conert cm into feet+inches",round(height/30.42),"feet",height%30.42,"inch")


#Get the no of the dollars from the user apply the conversion of 
#1 dollar = 82 rupees and print the amount to the console in rupees
dollers= int(input("enter no of dollers"))
print(dollers,"dollers=",dollers*82,"rupees")

#6) Take the source, destination, fare in INR, discount_rate percentage from the user and display the 
#string ex: "fare from mumbai to pune is 300 INR with has a discount of 5%"

source = str(input("enter the source"))
destination = str(input("enter the destination"))
fare= float(input("enter the fare in INR"))
discount= float(input("enter the discount"))
print("fare from",source,"to",destination,"is",fare-((fare*discount)/100),"INR with has a discount of",discount,"%")
