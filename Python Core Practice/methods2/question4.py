""""Q4. Build a Loan class that:
•	Has a common interest rate for all loans.
•	Each object stores borrower name and principal.
•	Calculates total payable amount.
•	Provides a function to update the interest rate.
•	Provides a static function to check loan eligibility (e.g., salary > certain threshold).
Demonstrate:
1.	Creating multiple loan accounts.
2.	Updating interest rates.
3.	Checking eligibility and total repayment for borrowers.
"""
class Loan:
    interest_rate=8
    min_salary=30000
    def __init__(self,name,principal,tenure):
        self.name=name
        self.principal=principal
        self.tenure=tenure
    def final_amount(self):
        fp=(self.principal*(Loan.interest_rate/100)*self.tenure)
        return self.principal+fp
    @classmethod
    def update_interest_rate(cls,new_rate):
        cls.interest_rate=new_rate
    @staticmethod
    def loan_eligibility(salary):
        if salary>=Loan.min_salary:
            return True
        return False
loan1=Loan("swadeep",2000000,3)
loan2=Loan("deekshith",3000000,4)
print(loan1.final_amount()) #printing the final amount to be paid after including the interest
print(loan2.final_amount()) #printing the final amount to be paid after including the interest
Loan.update_interest_rate(12)
print(loan1.final_amount()) #printing the final amount to be paid after updating the interest rate
print(loan2.final_amount()) #printing the final amount to be paid after updating the interest rate
if Loan.loan_eligibility(32000):
    print("Eligible for Loan")
else:
    print("Not Eligible")