data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())

length = len(data)
length_0 = len(data[0])
print(length)
#print('data[0] = ', data[0])
#print('data[',length - 1,'] = ', data[length - 1])
#print(length_0)
cnt = 0
sum_data_length = 0
for i in data:
	length_temp = len(data[cnt])
	sum_data_length += length_temp
	cnt += 1 
print(sum_data_length/length)
