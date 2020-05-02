import time
import random
from demos import quicksort, mergesort, bubblesort, selectionsort

def create_random_list(size, max_val):
	ran_list = []
	for num in range(size):
		ran_list.append(random.randint(1, max_val))
	return ran_list

def analyze_func(func_name, arr):
	start = time.time()
	func_name(arr)
	end = time.time()
	total = end - start
	print(f"{func_name.__name__.capitalize()}\t-> Elapsed time: {total:.5f}")

size = int(input("What size list do you want to create? "))
maximum = int(input("What is the max value of the range? "))
run_times = int(input("How many times do you want to run? "))

for num in range(run_times):
	print(f"Run: {num+1}")
	l = create_random_list(size, maximum)
	analyze_func(bubblesort, l.copy())
	analyze_func(selectionsort, l)
	analyze_func(quicksort, l)
	analyze_func(mergesort, l)
	print("Built In", end = ' ')
	analyze_func(sorted, l)
	print("-" * 40)






