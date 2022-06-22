import java.util.Arrays;

class Solution {
    public static int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length - k];
    }

    public static void main(String ars[]) {
        int[] test1 = {3, 2, 1, 5, 6, 4};
        int[] test2 = {3, 2, 3, 1, 2, 4, 5, 5, 6};
        System.out.println(findKthLargest(test1, 2));
        System.out.println(findKthLargest(test2, 4));
    }
}