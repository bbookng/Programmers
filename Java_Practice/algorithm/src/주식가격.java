import java.util.ArrayList;
import java.util.List;

public class 주식가격 {
    public int[] solution(int[] prices) {
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < prices.length; i++) {
            int time = 0;
            for (int j = i+1; j < prices.length; j++) {
                time ++;
                if (prices[i] > prices[j]) break;
            }
            answer.add(time);
        }
        return answer.stream().mapToInt(i->i).toArray();
    }

}
