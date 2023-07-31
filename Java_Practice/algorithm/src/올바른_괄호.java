import java.util.*;

public class 올바른_괄호 {
    boolean solution(String s) {

        Queue<String> q = new LinkedList<>();
        for (char i : s.toCharArray()) {
            if (q.isEmpty() && i == ')') {
                return false;
            } else if (!q.isEmpty() && q.peek().equals("(") && i == ')' ) {
                q.poll();
            } else {
                q.add(String.valueOf(i));
            }
        }
        return !q.isEmpty() ? false : true;
    }
}
