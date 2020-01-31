import time
start_time = time.time()
for num in range(1, 78000, 2):
	print(num)
print("---- %s seconds ---" % (time.time() - start_time))
