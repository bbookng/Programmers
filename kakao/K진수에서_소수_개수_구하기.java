public class K진수에서_소수_개수_구하기 {
    public static boolean check(int number) {
        if (number < 2) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
    public static int solution(int n, int k) {
        int answer = 0;
        String number = "";

        while (n > 0) {
            number = (n % k) + number;
            n /= k;
        }

        String[] numbers;
        if (number.equals("0")) {
            numbers = new String[]{number}; // number가 "0"일 경우에도 배열 생성
        } else {
            numbers = number.split("0");
        }

        for (String num : numbers) {
            if (!num.isEmpty()) {
                int parsedNum = Integer.parseInt(num);
                if (parsedNum > 1 && check(parsedNum)) {
                    answer++;
                }
            }
        }

        return answer;

    }
    public static void main(String[] agrs) throws Exception {
        solution(437647, 3);
    }

//    public boolean isprime(long n){
//        if(n <= 1) return false;
//        else if(n == 2) return true;
//        for(int i = 2; i <= Math.sqrt(n); i++)
//            if(n % i == 0)
//                return false;
//        return true;
//    }
//    public String to_Knum(int n, int k) {
//        String res = "";
//        while(n > 0) {
//            res = n % k + res;
//            n /= k;
//        }
//        return res;
//    }
//    public int solution(int n, int k) {
//        int answer = 0, i, j;
//        String s = to_Knum(n,k);
//        for(i = 0; i < s.length(); i = j) {
//            for(j = i + 1; j < s.length() && s.charAt(j) != '0'; j++);
//            if(isprime(Long.parseLong(s.substring(i,j))))
//                answer++;
//        }
//        return answer;
//    }
}
