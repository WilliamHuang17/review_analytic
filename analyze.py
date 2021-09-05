data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())

length = len(data)
print(length)
print('data[0] = ', data[0])
print('data[',length - 1,'] = ', data[length - 1])
