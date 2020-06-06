PersonsList = [1,2,3,4,5,6,7]
counter = 1
index = 0
while len(PersonsList)>1:
  if index >= len(PersonsList):
    index = len(PersonsList)-index
  if counter == 3:
    counter = 1
    PersonsList.pop(index)
  else:
    index += 1
    counter += 1
print(PersonsList[0])