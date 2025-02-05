w_i = [0.01,0.04,0.11,0.24,0.27,0.16,0.12,0.05]

weight_range_list = []

for i in range(8):
	weight_range_list.append((15000*(i+1))+7500)

print(weight_range_list)

dist_list = []
i = 0

for weight_range in weight_range_list:
	dist_list.append(weight_range*w_i[i])
	i+=1

print(dist_list)
print(sum(dist_list))