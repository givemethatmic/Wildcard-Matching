s = input('please input the data of S:\n')
p = input('please input the data of P:\n')
ptr_repository = []
c = -1
s_ptr = 0
p_ptr = 0

for a in range(len(p)):
    if p[a] == '*':
        c += 1
        ptr_repository.append([])
        for b in range(len(s)):
            if s[b] == p[a + 1]:
                ptr_repository[c].append(b)
            
if ptr_repository == []:
    while s_ptr < len(s) and p_ptr < len(p):
        if s[s_ptr] == p[p_ptr] or p[p_ptr] == '?':
            s_ptr += 1
            p_ptr += 1
        else:
            break
    if s_ptr == p_ptr == len(s):
        print('Ture')
    else:
        print('False')
else:
    print(ptr_repository)