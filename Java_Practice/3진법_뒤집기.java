class Solution {
    public int solution(int n) {
        String std = Integer.toString(n, 3);
        String reversed = new StringBuilder(std).reverse().toString();
        return Integer.valueOf(reversed, 3);
    }
}