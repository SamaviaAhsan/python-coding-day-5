#print staric

for i in range (6):
    print("*"*i)

#check the balance of the account and perform deposit and withdrawal operations.

balance = 10000

while True:
  print(" Deposit")
  print("Withdraw")
  print(" Check Balance")
  print(" Exit")
  choice = (input("Enter your choice: "))
  if choice == "Deposit":
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Amount deposited successfully.")

  elif choice == "Withdraw":
        amount = int(input("Enter withdrawal amount: "))

        if amount > balance:
            print("Insufficient Balance")
        else:
            balance -= amount
            print("Amount withdrawn successfully.")

  elif choice == "Check Balance":
        print("Your balance is:", balance)

  elif choice == "Exit":
        print("Thank you!")

        break   
  else:
        print("Invalid choice")


#check the marks of students and print pass or fail based on the marks.

students = {
    "Ali": 75,
    "Sara": 45,
    "Ahmed": 60,
    "Ayesha": 35,
    "Bilal": 80
}

for name in students:
    if students[name] >= 60:
        print(name, "Pass")
    else:
        print(name, "Fail")


#check students marks


names = ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal"]

ages = (20, 21, 19, 22, 20)

subjects = {"Python", "Math", "English", "Physics", "Database"}

marks = {
    "Ali": 75,
    "Sara": 45,
    "Ahmed": 60,
    "Ayesha": 35,
    "Bilal": 80
}

for name in names:
    mark = marks[name]

    if mark >= 50:
        print(name, mark, "Pass")
    else:
        print(name, mark, "Fail")


#check prime numbers


count=0
for i in range(5):
    num=int(input("Enter a number: "))
    factor=0 

    for j in range(1,num+1):
        if num%j==0:
            factor+=1
    if factor == 2:
        print(num, "is  a prime number")
    else:
        print(num, "is not a prime number")
        count+=1        
print("Total prime numbers entered:", count)   
