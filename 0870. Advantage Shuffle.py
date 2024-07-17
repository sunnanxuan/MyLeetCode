class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic=collections.defaultdict(list)
        for i,c in enumerate(nums2):
            dic[c].append(i)
        nums2.sort(reverse=True)
        nums1.sort(reverse=True)
        res=[0]*len(nums1)
        stack=[]
        while nums2 and nums1:
            n1=nums1.pop()
            n2=nums2.pop()
            while nums1 and n1<=n2:
                stack.append(n1)
                n1=nums1.pop()

            if n1>n2:
                p=dic[n2].pop()
                if not dic[n2]:dic.pop(n2)
                res[p]=n1
            elif n1<=n2 and not nums1:
                stack.append(n1)
        if stack:
            for k in dic:
                for i in dic[k]:
                    res[i]=stack.pop()
        return res

