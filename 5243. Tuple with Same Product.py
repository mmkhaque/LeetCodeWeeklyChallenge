class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        total_product = 1
        
        '''
        for x in nums:
            total_product *= x
        
        #print(total_product)
        
        
        i, j = 0, len(nums) - 1
        
        nums.sort()
        
        left_numbers, right_numbers = [], []
        
        while i < j:
            left_numbers.append(nums[i])
            right_numbers.append(nums[j])
            i +=1
            j -=1
            
            if i ==2:
                break
        
        new_array = left_numbers.extend(right_numbers)
        
        print(new_array)
        
        permute_num = itertools.permutations(new_array)
        
        print(permute_num)
            
        
        
        '''
        permute_num = itertools.permutations(nums)
        
        l = len(nums)
        
        master_list = []
        
        seen_before_list = []
        
        def equals(arr):
            
            nonlocal master_list
            nonlocal seen_before_list
            
            i, j, k, l = 0, 1, 2, 3
            
            while l < len(nums):
                if [arr[i], arr[j], arr[k], arr[l]] not in seen_before_list:
                    if arr[i] * arr[j] == arr[k] * arr[l]:
                        if [arr[i], arr[j], arr[k], arr[l]] not in master_list:
                            master_list.append([arr[i], arr[j], arr[k], arr[l]])
                    else:
                        seen_before_list.append([arr[i], arr[j], arr[k], arr[l]])

                i +=1
                j +=1
                k +=1
                l +=1

        
        for n in permute_num:
            #print(n)
            equals(n)

        return len(master_list)
        
