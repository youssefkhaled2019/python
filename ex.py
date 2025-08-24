number = 10
if isinstance(number, int):
    print("The variable is an integer.")
else:
    print("The variable is not an integer.")

float_number = 3.14
if isinstance(float_number, int):
    print("The variable is an integer.")
else:
    print("The variable is not an integer.")
# -------------------------------------------------------    
number = 10
if type(number) == int:
    print("The variable is an integer.")
else:
    print("The variable is not an integer.")
# -------------------------------------------------------    
float_as_int = 100.0
if float_as_int.is_integer():
    print("The float value represents an integer.")
else:
    print("The float value does not represent an integer.")