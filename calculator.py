def add(a, b):
	return a + b

def substract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

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
