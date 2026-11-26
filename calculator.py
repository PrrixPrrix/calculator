# SCCM4910 lab project - a four operation calculator
def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

def circleArea(r):
	if r >= 0:
		return 3.14*r*r
	else:
		return "Error"

def main():
	while True:
		a = float(input("First Number: "))
		op = input("Operator ( + - * /): ")
		b = float(input("Second Number: "))
		if op == "+":
			print("Result: ", add(a, b))
		elif op == "-":
			print("Result: ", subtract(a, b))
		elif op == "*":
			print("Result: ", multiply(a, b))
		elif op == "/":
			print("Result: ", divide(a, b))
		else:
			print("Unknown Operator: ", op)
		print(" ")
if __name__ == "__main__":
	main()
