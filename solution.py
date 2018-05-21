class Solution(object):

    def __init__(self):
        s = input('please input the data of S:\n')
        p = input('please input the data of P:\n')
        self.s = s
        self.p = p
        self.isMatch()

    def meeting_star(self, s_ptr, p_ptr):
        """
        :type s_ptr: int
        :type p_ptr: int
        :rtype: (int, int)
        """

        if p_ptr + 1 >= len(self.p)
            s_ptr = len(self.s)
            p_ptr = len(self.p)
            return s_ptr, p_ptr
        p_ptr += 1

        while self.p[p_ptr] != '*':
            if p_ptr >= len(self.p):
                break
            p_ptr += 1

        while self.s[s_ptr] != self.p[p_ptr]:
            s_ptr += 1
            if s_ptr == len(self.s):
                s_ptr = False
                return s_ptr, p_ptr

        s_ptr_copy = s_ptr - 1 
        p_ptr_copy = p_ptr - 1
        while True:
            if self.s[s_ptr_copy] != self.p[p_ptr_copy] and self.p[p_ptr_copy] != '?':
                break

        return s_ptr, p_ptr

    @staticmethod
    def meeting_question(s_ptr, p_ptr):
        """
        :type s_ptr: int
        :type p_ptr: int
        :rtype: (int, int)
        """
        s_ptr += 1
        p_ptr += 1
        return s_ptr, p_ptr

    def meeting_others(self, s_ptr, p_ptr):
        """
        :type s_ptr: int
        :type p_ptr: int
        :rtype: (int, int)
        """
        if self.s[s_ptr] == self.p[p_ptr]:
            s_ptr += 1
            p_ptr += 1
        else:
            s_ptr = False
        return s_ptr, p_ptr

    def isMatch(self):
        """
        :rtype: bool
        """
        s_ptr = 0
        p_ptr = 0
        while s_ptr < len(self.s) or p_ptr < len(self.p):
            if self.p[p_ptr] == "*":
                s_ptr, p_ptr = self.meeting_star(s_ptr, p_ptr)
            elif self.p[p_ptr] == "?":
                s_ptr, p_ptr = self.meeting_question(s_ptr, p_ptr)
            else:
                s_ptr, p_ptr = self.meeting_others(s_ptr, p_ptr)
            if s_ptr is False:
                return False     
        if s_ptr == len(self.s) and p_ptr == len(self.p):
            return True
        else:
            return False


if __name__ == '__main__':
    project = Solution()
    print(project.isMatch())
