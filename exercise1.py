class Solution:
    def convert(self, s, numRows: int):
        if numRows == 1:
            return s
        str_list=[]
        str_temp=''
        length_str=len(s)
        print(length_str)
        for i in range(0,numRows):
            #竖着的值的规律为间隔为numRows+numRows-2
            j=i
            while True:
                # print(s[j])
                # 判断往前数的值是否超出取值范围
                before_j=j-i * 2
                pre_j=j-numRows-numRows+2
                # print(before_j)
                if (before_j>0) and (before_j != j) and (before_j != pre_j):
                    if before_j <length_str:
                        str_temp+=s[before_j]
                if j < length_str:
                    str_temp+=s[j]
                else:
                    break
                j+=(numRows+numRows-2)
            str_list.append(str_temp)
            str_temp=''
        str_fin=''.join(str_list)
        print(str_list)
        return str_fin

if __name__=='__main__':
    solution = Solution()
    str="PAYPALISHIRING"
    solution.convert(str,4)