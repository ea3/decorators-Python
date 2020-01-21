def func():
	return 1

print(func())

def hello():
	return "Hello!"

print(hello)


greet = hello

print(greet())

print(hello())

del(hello)

#print(hello())

print(greet())

def hello(name='Emilio'):
	print("The hello() has been executed")

	def greet():
		return "\t This is the greet() function inside hello"

	def welcome():
		return "\t This is welcome() inside Hello!"

	print("I am going to return a function")

	if name == "Emilio":
		return greet
	else:
		return welcome

	#print(greet())
	#print(welcome())
	#print("This is the end of the Hello() function")
my_new_func = hello("Emilio")
print(my_new_func())

def new_decorator(original_func):

	def wrap_func():

		print("Extra code, before the original function")

		original_func()

		print("Some extra code, after the original function")

	return wrap_func

def func_needs_decorator():
	print("I want to be decorated")

decorated_function = new_decorator(func_needs_decorator)
decorated_function()

@new_decorator
def func_needs_decorator():
	print("I want to be decorated")
func_needs_decorator()















