credit_score = int(input("What's your credit score? "))

if credit_score < 300 or credit_score > 850:
	print("Invalid score.")
	print("Seek credit improvement.")
elif credit_score >= 750:
	print("Excellent - Loan Approved. Interest rate: Low")
elif 700 <= credit_score < 750:
	print("Good - Loan Approved with Review. Interest rate: Low")
elif 600 <= credit_score < 700:
	print("Fair - Loan Conditional. Seek credit improvement.")
else:
	print("Poor - Loan Denied. Seek credit improvement.")
