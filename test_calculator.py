from calculator import add, substract, multiply, divide

def test_add():
	assert add(2, 3) == 5

def test_divide():
	assert divide(6, 2) == 3

def test_multiply():
	assert multiply(3, 2) == 6

def test_substract():
	assert substract(6, 3) == 3

def test_divide_uneven():
	a, b = 5, 2
	result = divide(a, b)
	assert result == 2.5

def test_circleArea():
	assert circleArea(-4) == "Error"
	
