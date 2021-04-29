//https://leetcode.com/problems/reverse-string/
public class Solution {
    public void ReverseString(char[] s) {
        helper(s,0,s.Length -1);
    }
     public void helper(char[] s, int left, int right)
        {
            if(left >= right) return;
            char temp = s[left];
            s[left++] = s[right];
            s[right--] = temp;
            helper(s, left, right);
        }
}
