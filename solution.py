def meet_star(s_ptr, p_ptr):
    p_ptr_copy = p_ptr + 1
    if p_ptr_copy == len(p):
        return len(s), len(p)
    while p[p_ptr_copy] == '?':
        p_ptr_copy += 1
    p_ptr = p_ptr_copy
    while True:
        while s[s_ptr] != p[p_ptr_copy]:
            s_ptr += 1
            if s_ptr == len(s):
                return len(s), -1
        while s[s_ptr] == p[p_ptr_copy] or p[p_ptr_copy] == '?':
            s_ptr += 1
            p_ptr_copy += 1
            if s_ptr >= len(s) or p_ptr_copy >= len(p):
                if s_ptr == len(s) and p_ptr_copy == len(p):
                    return len(s), len(p)
                else:
                    return len(s), -1
            if p[p_ptr_copy] == '*':
                return s_ptr, p_ptr_copy
        p_ptr_copy = p_ptr


def meet_question(s_ptr, p_ptr):
    s_ptr += 1
    p_ptr += 1
    return s_ptr, p_ptr


def meet_others(s_ptr, p_ptr):
    if s[s_ptr] == p[p_ptr]:
        s_ptr += 1
        p_ptr += 1
    else:
        return len(s), -1
    return s_ptr, p_ptr


def main():
    global s, p
    s = input('please input the data of S:\n')
    p = input('please input the data of P:\n')
    s_ptr = 0
    p_ptr = 0

    while s_ptr < len(s) or p_ptr < len(p):
        if p[p_ptr] == '*':
            s_ptr, p_ptr = meet_star(s_ptr, p_ptr)
        elif p[p_ptr] == '?':
            s_ptr, p_ptr = meet_question(s_ptr, p_ptr)
        else:
            s_ptr, p_ptr = meet_others(s_ptr, p_ptr)
    if s_ptr == len(s) and p_ptr == len(p):
        return True
    else:
        return False 


if __name__ == "__main__":
    while True:
        print(main())