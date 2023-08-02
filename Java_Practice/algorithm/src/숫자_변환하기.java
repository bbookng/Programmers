import java.util.*;

public class 숫자_변환하기 {
    public int solution(int x, int y, int n) {
        Queue<Pair> q = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        q.add(new Pair(x, 0));

        while (!q.isEmpty()) {
            Pair pair = q.poll();
            int i = pair.first;
            int j = pair.second;

            if (i > y || visited.contains(i)) {
                continue;
            }
            visited.add(i);
            
            if (i == y) return j;

            for (int k : new int[]{i*3, i*2, i+n}) {
                if (k <= y && !visited.contains(k)) {
                    q.add(new Pair(k, j + 1));
                }
            }
        }

        return -1;
    }

    class Pair {
        int first;
        int second;

        Pair(int first, int second) {
            this.first = first;
            this.second = second;
        }
    }
}
