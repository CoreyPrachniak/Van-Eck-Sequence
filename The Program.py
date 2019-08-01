print("Please input a tuple, (M, p). The output is the probability that for a random index, n < M, the nth member of the Van Eck sequence is zero or within p percent of n.")

tuple = input()
M, p = map(int, tuple[1: len(tuple) - 1].split(", "))

#STEP 1: Fill an array called dontknow with the first M entries of the Van Eck sequence.

dontknow = [0]*M
seen = []

for i in range(1, M):
	if dontknow[i - 1] not in seen:
		dontknow[i] = 0
		seen.append(dontknow[i - 1])
	else:
		for j in range(1, i):
			if dontknow[i - 1] == dontknow[(i - 1) - j]:
				dontknow[i] = j
				break

#STEP 2: Do a favorable divided by total calculation.

counter = 0

for i in range(M):
	if dontknow[i] == 0 or (100 - p)*i < 100*dontknow[i] < (100 + p)*i:
		counter += 1

print("The desired probability is " + str(counter/M) + ".")
