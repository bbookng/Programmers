import java.util.Arrays;
import java.util.HashSet;

public class 불량_사용자 {

    // 방문 처리
    static boolean[] visited;

    // 정답 담을 Set
    static HashSet<String> set;

    // 조합 생성
    public static void backtracking(int depth, String res, String[] ban_id, String[] user_id) {

        if (depth == ban_id.length) {
            String[] arr = res.split(" ");
            Arrays.sort(arr);

            String str = "";
            for (String s:arr) str += s;
            set.add(str);

            return;
        }

        for (int i = 0; i < user_id.length; i++) {
            if (visited[i] ||!user_id[i].matches(ban_id[depth])) continue;
            visited[i] = true;
            backtracking(depth+1, user_id[i] + " " + res, ban_id, user_id);
            visited[i] = false;
        }
    }
    public int solution(String[] user_id, String[] banned_id) {
        visited = new boolean[user_id.length];
        set = new HashSet<>();

        for (int i = 0; i < banned_id.length; i++) {
            banned_id[i] = banned_id[i].replace('*', '.');
        }

        backtracking(0, "", banned_id, user_id);
        return set.size();

    }
}
