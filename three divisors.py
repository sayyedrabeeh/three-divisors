'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def isThree(self, n) -> bool:
        c=0
        for i in range(1,n+1):
            if n % i == 0 :
                c=c+1
        return c==3
s=Solution()
print(s.isThree(10))