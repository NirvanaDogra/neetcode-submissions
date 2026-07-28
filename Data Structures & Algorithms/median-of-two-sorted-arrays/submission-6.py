class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        tlen = len1+len2 # 3
        mid = tlen//2 #1
        count1 = 0
        count2 = 0
        lst = []
        
        while count1<len1 and count2<len2:
            if nums1[count1] > nums2[count2]:
                # print("num2")
                lst.append(nums2[count2])
                count2+=1
            elif nums1[count1] < nums2[count2]:
                # print("num1")
                lst.append(nums1[count1])
                count1+=1
            else:
                # print("both")
                lst.append(nums1[count1])
                lst.append(nums1[count1])
                count1+=1
                count2+=1
            
        while count1<len1:
            lst.append(nums1[count1])
            count1+=1
            
        while count2<len2:
            lst.append(nums2[count2])
            count2+=1

        if tlen%2 != 0:
            print("this is mid", lst, mid)
            return lst[mid]

        elif tlen%2 == 0:
            print("otehr", lst[mid],lst[mid-1])
            return (lst[mid]+lst[mid-1])/2
            
        print(lst)
        return 0.0
        
