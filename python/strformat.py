def print_formatted(number):
	# your code goes here
	a = ""
	for _ in range(1,number+1):
		hex_,oct_,bin_ = hex(_).lstrip('0x'),oct(_).lstrip('0o'),bin(_).lstrip('0b')
		a += f"{_}\t{oct_}\t{hex_.upper()}\t{bin_}\n"
	print(f"{a[:-2]}")
if __name__ == '__main__':
	n = int(input())
	print_formatted(n)