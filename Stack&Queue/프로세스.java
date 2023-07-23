import java.util.*;

public class Solution {

    public class Pair<K, V> {
        // Key와 Value를 저장하는 변수
        private final K key;
        private final V value;

        // 생성자 : Pair 객체 생성
        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }

        // Getter 역할을 하는 듯
        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }
    }
    public int solution(int[] priorities, int location) {
        int answer = 0;

        // 연결 리스트를 쓰는 이유는 그냥 배열은 크기가 고정되어 있지만 연결 리스트는 삽입과 삭제가 가능하다.
        Queue<Pair<Integer, Integer>> q = new LinkedList<>();

        for (int i = 0; i < priorities.length; i++) {
            q.add(new Pair<>(i, priorities[i]));
        }

        while (!q.isEmpty()) {
            // poll 메서드가 python 의 pop(0) 과 같음. deque의 popleft() 와 같음.
            // remove 는 큐가 비어있을 시 예외가 발생하지만 poll 은 null을 반환함.
            Pair<Integer, Integer> now = q.poll();
            if (q.stream().anyMatch(i -> now.getValue() < i.getValue())) {
                q.add(now);
            } else {
                answer++;
                if (now.getKey() == location) {
                    return answer;
                }
            }
        }
        return answer;
    }
}