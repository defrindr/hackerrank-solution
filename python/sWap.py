def swap_case(s):
	new_str = []
	for i in s:
		new_str.append(i.lower()  if i.isupper() else i.upper())
	return ''.join (_ for _ in new_str)

if __name__ == '__main__':
	s = input()
	result = swap_case(s)
	print(result)