import java.util.*;

public class 다리를_지나는_트럭 {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int totalWeight = 0;
        int answer = 0;
        int[] bridge = new int[bridge_length];

        for (int t : truck_weights) {
            while (true) {
                // 다리 위의 트럭을 한 칸씩 앞으로 이동
                for (int i = 0; i < bridge_length - 1; i++) {
                    bridge[i] = bridge[i + 1];
                }
                bridge[bridge_length - 1] = 0;

                // 다음 트럭이 다리에 올라올 수 있는지 확인
                if (totalWeight + t <= weight) {
                    totalWeight -= bridge[0];
                    totalWeight += t;
                    bridge[bridge_length - 1] = t;
                    answer++;
                    break;
                } else {
                    totalWeight -= bridge[0];
                    answer++;
                }
            }
        }

        // 마지막 트럭이 다리를 건너는 시간 추가
        return answer + bridge_length;
    }
}
