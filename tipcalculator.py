print("Welcome to the tip calculator !")
bill = float(input("What was the total bill to be paid ? $ "))
tip = int((input("what is the total tip to be paid in percentage ? 10 15 or 20 ")))
people = int((input("What are the number of peoples in which you like to split your bill ?")))
tip_per_percent = tip /100
total_tip_amount = bill * tip_per_percent
total_bill = bill +total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)
print(f"bill to be paid by each person :$ {final_amount}")