public class Solution {
    public void ReverseString(char[] s) {
        RecurciveReverse(s,0,s.Length -1);
        
    }
    public void RecurciveReverse(char[] s, int left, int right)
    {
        if(left >= right) return;
         char tmp = s[left];
         s[left++] = s[right];
         s[right--] = tmp;
         RecurciveReverse(s, left, right);
        
        
    }
}