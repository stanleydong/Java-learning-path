# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)

# # re-declaring the variable works
f="abc"
print(f)

# # ERROR: variables of different types cannot be combined
print("Original f: " + str(123))

# Global vs. local variables in functions
def localVariable():
  f="Local value"
  print(f)

def globalVariable():
  global f
  f="Global value"
  print(f)


localVariable()
print(f)
globalVariable()
print(f)
