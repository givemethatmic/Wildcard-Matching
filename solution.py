class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s = input('please input the data of S \n')
        p = input('please input the data of P \n')
        s_ptr = 0
        p_ptr = 0
        data_ptr = 0
        data = []
        pos = []
        for a in range(len(p)):
            if p[a] == '*':
                pos.append(a)
            else:
                pass
        if bool(pos) == False:
            while s_ptr < len(s):
                if s[s_ptr] == p[p_ptr] or p[p_ptr] == '?':
                    s_ptr += 1
                    p_ptr += 1
                else:
                    return False
            return True
        else:
            data.append(p[0:pos[0]])
            for a in range(len(pos) - 1):
                data.append(p[(pos[a] + 1):pos[a + 1]])
            data.append(p[(a + 1):len(p)])
            while s_ptr < len(s):
                if data[data_ptr] == "":
                    data_ptr += 1
                if s[s_ptr:(s_ptr + len(data[data_ptr]))] != data[data_ptr]:
                    s_ptr += 1               
                else:
                    s_ptr += len(data[data_ptr])
                    data_ptr += 1
                if data[data_ptr] == "":
                    return True