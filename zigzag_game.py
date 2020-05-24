import time, sys

#Tracks the amount of indent spaces 
#and if the indentation increases or decreases
indent = 0 
indentIncrease = True #True for more indentation, False for less indentation

try:
  #The program will always execute, because is always True unless
  #you type Ctrl + C to stop it
  while True:  
    print(" " * indent, end="") #Print a spacing character the times indent equals to, it removes the new line at the end
    print("**********") #Prints 10 * right after the indentations
    time.sleep(0.1)#Pauses for 0.2 seconds after each printing

    #If True, add 1 to indent, adding 1 indent to line
    if indentIncrease:
      indent = indent + 1
      #If indent == 15, indentIncrease will be False to start decreases spaces
      if indent == 15:
        indentIncrease = False
    else:
      indent = indent - 1
      #If indent == 0, it goes back to adding spaces with indentIncrease as True
      if indent == 0:
        indentIncrease = True 

#When you press Ctrl + C, python sends a KeyboardInterrupt instruction
#This way it won't show an error, instead it will finish with no issues
except KeyboardInterrupt:
  sys.exit()


  