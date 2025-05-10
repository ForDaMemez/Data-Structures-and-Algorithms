num = [1,2,3,4,5,6,7,8]
Found = False
x = int(input("Enter what number you want"))
for i in range(len(num)):
  if num[i] == x:
    print("found at", num[i])
    Found = True
    break
  else:
    i = i + 1

if Found == False:
  print("Sorry, the number you are looking for is not in the list")