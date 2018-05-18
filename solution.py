class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_ptr = 0
        p_ptr = 0
        p_ptr_copy = 0
        while True:
            if s[s_ptr] != p[p_ptr]:
                if p[p_ptr] == '?':
                    s_ptr += 1
                    p_ptr += 1
                elif p[p_ptr] == '*':
                    p_ptr_copy = p_ptr + 1
                    while True:
                        if s_ptr == len(s) or p_ptr == len(p) or p_ptr_copy == len(p):
                            break
                        if p[p_ptr_copy] != s[s_ptr]:
                            if p[p_ptr_copy] == '?':
                                p_ptr_copy += 1
                                s_ptr += 1
                            elif p[p_ptr_copy] == '*':
                                p_ptr = p_ptr_copy
                                p_ptr_copy += 1
                            else:
                                s_ptr += 1                        
                        else:
                            while True:
                                p_ptr_copy += 1
                                s_ptr += 1
                                if s_ptr == len(s) or p_ptr == len(p) or p_ptr_copy == len(p):
                                    break
                                if p[p_ptr_copy] != s[s_ptr]:
                                    if p[p_ptr_copy] == '?':
                                        pass
                                    elif p[p_ptr_copy] == '*':
                                        p_ptr = p_ptr_copy
                                        p_ptr_copy += 1
                                        break
                                    else:
                                        p_ptr_copy = p_ptr + 1
                                        break                                
                else:
                    return False
            else:
                s_ptr += 1
                p_ptr += 1
            if s_ptr == len(s) and p_ptr == len(p):
                return True
            elif s_ptr == len(s) and p_ptr != len(p):
                return False
            elif p_ptr == len(p) and s_ptr != len(s):
                return False

if __name__ == '__main__':
    start = Solution()
    while True:
        data_s = input('please input the data of S: \n')
        data_p = input('please input the data of P: \n')
        so_ = start.isMatch(data_s, data_p)
        print(so_)