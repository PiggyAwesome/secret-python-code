
import os 

'''

Some secret code here:
  Example:
    os.system("rm -rf important")

'''

print("Only innocent code in here <3")

with open(os.path.realpath(__file__), "w") as this_one:
  this_one.write("print(\"Only innocent code in here <3\")")
