
def match():
	s_ptr = 0
	p_ptr = 0
	s_ptr_end = len(s) - 1
	p_ptr_end = len(p) - 1
	p_copy = []
	if len(s) == len(p) == 0:
		return True
	for a in p:
		if a != '*':
			p_copy.append(a)
	if len(p_copy) > len(s):
		return False
	while p[p_ptr] != '*':
		if s[s_ptr] == p[p_ptr] or p[p_ptr] == '?':
			s_ptr += 1
			p_ptr += 1
		else:
			return False
		if p_ptr == len(p):
			if s_ptr == len(s):
				return True
			else:
				return False
	while p[p_ptr_end] != '*':
		if s[s_ptr_end] == p[p_ptr_end] or p[p_ptr_end] == '?':
			s_ptr_end -= 1
			p_ptr_end -= 1
		else:
			return False
	if p_ptr == p_ptr_end:
		return True
	while True:
		while p[p_ptr] == '*':
			p_ptr += 1
			if p_ptr == p_ptr_end:
				return True
		p_ptr_copy = p_ptr
		while s[s_ptr] != p[p_ptr_copy] and p[p_ptr_copy] != '?':
			s_ptr += 1
			if s_ptr > s_ptr_end:
				return False
		s_ptr_copy = s_ptr
		while s[s_ptr_copy] == p[p_ptr_copy] or p[p_ptr_copy] == '?':
			s_ptr_copy += 1
			p_ptr_copy += 1
			if p[p_ptr_copy] == '*':
				p_ptr = p_ptr_copy
				s_ptr = s_ptr_copy - 1
				break
			if s_ptr_copy > s_ptr_end:
				return False
		s_ptr += 1
		while p[p_ptr] == '*':
			p_ptr += 1
			if p_ptr >= p_ptr_end:
				return True
		if s_ptr_copy > s_ptr_end:
			return False

if __name__ == '__main__':
	while True:
		s = input('please input the data of S:\n')
		p = input('please input the data of P:\n')
		a = match()
		print(a)  


