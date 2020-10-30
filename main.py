row = []
printlist = ""
num1 = 0
num2 = 0
for i in range(13):
  for c in range(13):
    row.append(i*c)
  for e in range(13):
    if len(str(row[e])) == 1:
      printlist += str(row[e]) + "  |"
    elif len(str(row[e])) == 2:
      printlist += str(row[e]) + " |"
    elif len(str(row[e])) == 3:
      printlist += str(row[e]) + "|"
  row = []
  print(printlist)
  printlist = ""
while True:
  num1 = input("Please enter a number to multiply: ")
  num2 = input("Please enter a number to multiply: ")
  try:
    print("The answer is: " + str(int(num1) * int(num2)))
  except:
    print("There was an error while calculating...")
    continue
