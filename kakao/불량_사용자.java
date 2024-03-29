import java.util.*;

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
    public int solution1(String[] user_id, String[] banned_id) {
        visited = new boolean[user_id.length];
        set = new HashSet<>();

        for (int i = 0; i < banned_id.length; i++) {
            banned_id[i] = banned_id[i].replace('*', '.');
        }

        backtracking(0, "", banned_id, user_id);
        return set.size();

    }

    // 책 풀이
    private void count(int index, Set<String> banned, String[][] bans, Set<Set<String>> banSet) {
        if (index == bans.length) {
            banSet.add(new HashSet<>(banned));
            return;
        }

        for (String id : bans[index]) {
            if (banned.contains(id)) continue;
            banned.add(id);
            count(index + 1, banned, bans, banSet);
            banned.remove(id);
        }
    }

    public int solution2(String[] user_id, String[] banned_id) {
        String[][] bans = Arrays.stream(banned_id)
                .map(banned -> banned.replace('*', '.'))
                .map(banned -> Arrays.stream(user_id)
                        .filter(id -> id.matches(banned))
                        .toArray(String[]::new))
                .toArray(String[][]::new);

        Set<Set<String>> banSet = new HashSet<>();
        count(0, new HashSet<>(), bans, banSet);
        return banSet.size();
    }
}
