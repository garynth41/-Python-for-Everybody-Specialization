#Exercise 3: Write a program to prompt for a score between 0.0 
#and 1.0. If the score is out of range, print an error message. 
#If the score is between 0.0 and 1.0, print a grade using the 
#following table:
#Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
#< 0.6    F

#Enter score: 0.95 
#A 
#Enter score: perfect
#Bad score
#Enter score: 10.0
#Bad score
#Enter score: 0.75
#C
#Enter score: 0.5
#F
#Run the program repeatedly as shown above to 
#test the various different values for input.

score=input("Please type a score between 0.0 and 1.0:")
try:
  float(score)
  if float(score) >= 0.9 and float(score) <= 1.0:
    print("A")
  elif float(score) >= 0.8 and float(score) <= 0.9:
    print("B")
  elif float(score) >= 0.7 and float(score) <= 0.8:
    print("C")
  elif float(score) >= 0.6 and float(score) <= 0.7:
    print("D")
  elif float(score) > 0 and float(score) <= 0.6:
    print("F")
  else:
    print("Bad score.  Please run the program again.")  
except: 
    print("Bad score.  Please run the program again.")
  