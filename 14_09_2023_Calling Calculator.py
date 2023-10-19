# importing calculator
import Calculator

# trying all the operations
add_result = Calculator.addition(5, 6)
sub_result = Calculator.subtraction(7, 8)
mul_result = Calculator.multiplication(4, 5)
try:
    div_result = Calculator.division(10, 0)
except ValueError as e:
     div_result = str(e)
try:
    mod_result = Calculator.modulo(10, 3)
except ValueError as e:
     mod_result = str(e)

# displaying the result
print("Add Result of 5 and 6: ", add_result)
print("Sub Result of 7 and 8: ", sub_result)
print("Mul Result of 4 and 5: ", mul_result)
print("Div Result of 10 and 0: ", div_result)
print("Mod Result of 10 and 3: ", mod_result)