import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class 수포자 {
    public int[] solution(int[] answers) {
        List<Integer> answer = new ArrayList<>();

        int[] score = new int[3];
        int[] first = {1, 2, 3, 4, 5};
        int[] second = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] third = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == first[i%5]) score[0] ++;
            if (answers[i] == second[i%8]) score[1] ++;
            if (answers[i] == third[i%10]) score[2] ++;

        }
        // int maxScore = Math.max(score[0], Math.max(score[1], score[2]));
        int maxValue = Arrays.stream(score).max().getAsInt();

        for (int i = 0; i < 3; i++) {
            if (maxValue == score[i]) {
                answer.add(i+1);
            }

        }

        return answer.stream().mapToInt(i->i).toArray();
    }
}
