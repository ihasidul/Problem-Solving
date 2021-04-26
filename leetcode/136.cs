using System;

namespace Problem
{
    class Program
    {
        static int SingleNumber(int[] nums)
        {
            int a = 0;
            foreach(int n in nums)
            {
                a ^= n;
                
            }
            return a;
        }
        static void Main(string[] args)
        {
            int[] nums = { 1, 2, 1, 2,4,4, 9 };
            int x = SingleNumber(nums );
            Console.WriteLine(x);
        }
    }
}