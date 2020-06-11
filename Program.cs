using System;
using System.Collections.Generic;

namespace leetcode
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            var nums = new int[] {1,1,2};
            
           

            var len = RemoveDuplicates(nums);

            //  Console.WriteLine(len);

            // for (int i = 0; i < len; i++) {
            //     Console.WriteLine(nums[i]);
            // }
        }

         public static int RemoveDuplicates(int[] nums) {
              if (nums.Length == 0 || nums.Length == 1)
                return nums.Length;

            int uniqueElementsCount = 1;

            for (int i = 0; i < nums.Length; i++)
            {
                if (nums[i] != nums[uniqueElementsCount-1])
                {
                    nums[uniqueElementsCount++] = nums[i];
                }
            }

            
            for (int i = 0; i < nums.Length; i++) {
                Console.WriteLine(nums[i]);
            }
            return uniqueElementsCount;
         }
        //     var listNums = new List<int>(nums);
            
        //     if(nums.Length == 0)
        //         return 0;
                
        //     for(int i=1, swapInput = listNums[0]; i<listNums.Count; ++i)
        //     {   
        //         if(swapInput == listNums[i])
        //         {
        //             listNums.RemoveAt(i);   
        //             --i;
        //         }
        //         else
        //         {
        //             swapInput = listNums[i];
        //         }
        //     }
            
        //     for (int i = 0; i < listNums.Count; i++) {
        //         Console.WriteLine(listNums[i]);
        //     }
            
        //     nums = listNums.ToArray();

        //      for (int i = 0; i < nums.Length; i++) {
        //         Console.WriteLine(nums[i]);
        //     }
            
            
        //     return nums.Length;
        // }
    }
}
