import sys

def collatz(start, limit=-1, cycles=1):
	print(cycles, "-> ", int(start))
	if limit == 0 or start == 1:
		print("Completed %d cycles, stopped at %d" % (cycles, start))
		return
	
	if start % 2 == 0:
		return collatz(start / 2, limit - 1, cycles + 1)
	else:
		return collatz((start * 3) + 1, limit - 1, cycles + 1)
	
	
if __name__ == '__main__':
	start = int(sys.argv[1])
	collatz(start, cycles=0)