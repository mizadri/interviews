class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # one pointer always points to where you have to write, the other one to the number of elements you have read
        out_ptr = 0
        read_ptr = 0
        deleted = 0

        while(read_ptr < len(nums)):
            #print(out_ptr,read_ptr,deleted)
            nums[out_ptr] = nums[read_ptr]
            read_ptr += 1
            #print(nums)
            while(read_ptr < len(nums) and nums[out_ptr] == nums[read_ptr]):
                read_ptr += 1
                deleted += 1

            out_ptr += 1

        return len(nums)-deleted
