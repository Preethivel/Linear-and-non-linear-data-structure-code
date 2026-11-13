def isPerfectSquare(self, num: int) -> bool:
        l=1
        r=num
        while l<=r:
            m=(l+r)//2
            s=m*m
            if s==num:
                return True
            elif s<num:
                l=m+1
            else:
                r=m-1
        return False
