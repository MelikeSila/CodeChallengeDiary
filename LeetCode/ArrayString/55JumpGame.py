class Solution {
    fun canJump(nums: IntArray): Boolean {
        
        val k = nums.size
        var max_jump_lenght = 0

        // if the array size 1 --> [0], [1>]
        if (k == 1){
            return true
        }

        //if the array size bigger than 1
        // we do not need to check the last integer
        for (i in 0..k-2){
            if (max_jump_lenght < nums[i]){
                max_jump_lenght = nums[i]
            }
            
            // there is no way to go further
            if (max_jump_lenght <= 0){
                return false
            }
            
            // is current max_jump_lenght enough to jump last step
            if (max_jump_lenght >= k-1){
                return true
            }

            max_jump_lenght -=1
            
        }
        return true
    }
}