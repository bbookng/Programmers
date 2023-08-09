package algorithm.src;

import java.util.LinkedList;
import java.util.Queue;

public class 게임_맵_최단거리 {
    static final int[] rowArr = new int[]{-1, 1, 0, 0},
            colArr = new int[]{0, 0, -1, 1};

    static class Node {
        final int row;
        final int col;
        final int move;

        public Node(int row, int col, int move) {
            this.row = row;
            this.col = col;
            this.move = move;
        }
    }

    public int solution(int[][] maps) {
        int rowLength = maps.length, colLength = maps[0].length;
        boolean[][] visited = new boolean[rowLength][colLength];

        for (int i = 0; i < maps.length; i++) {
            for (int j = 0; j < maps[i].length; j++) {
                if (maps[i][j] == 0) visited[i][j] = true;
            }
        }

        Queue<Node> queue = new LinkedList<>();
        visited[0][0] = true;
        // offer 큐 맨 뒤에 삽입.
        // add 와 차이점 ( add는 큐가 꽉 찬 경우 Exception 발생, offer는 false 반환)
        queue.offer(new Node(0, 0, 1));
        int min = Integer.MAX_VALUE;

        while (!queue.isEmpty()) {
            Node node = queue.poll();

            for (int i = 0; i < 4; i++) {
                int row = node.row + rowArr[i], col = node.col + colArr[i];
                if (rowLength <= row || row < 0 || colLength <= col || col < 0 || visited[row][col]) continue;

                visited[row][col] = true;
                queue.offer(new Node(row, col, node.move + 1));
                if (row == rowLength-1 && col == colLength -1) min = Math.min(min, node.move + 1);
            }
        }
        return min == Integer.MAX_VALUE ? -1 : min;
    }
}
