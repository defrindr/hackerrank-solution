inp = input()
arr = inp.split(" ")
arr2 =[[],[],[]]
j=0
for i in range(3):
	for o in range(3):
		arr2[i].append(int(arr[j]))
		j+=1
print(arr2)
