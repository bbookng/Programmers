public class Solution15 {
    // Count 객체 생성
    private static class Count {
        public final int zero;
        public final int one;

        public Count(int zero, int one) {
            this.zero = zero;
            this.one = one;
        }

        // Count 생성
        public Count add(Count other) {
            return new Count(zero + other.zero, one + other.one);
        }

    }

    private Count count(int offsetX, int offsetY, int size, int[][] arr) {
        // 높이
        int h = size / 2;

        // offset부터 offset + size 까지
        for (int x = offsetX; x < offsetX + size; x++) {
            for (int y = offsetY; y < offsetY + size; y++) {

                // 배열의 좌표와 arr의 좌표가 같지 않다면. ( 쿼드가 압축되지 않는다면 )
                if (arr[x][y] != arr[offsetX][offsetY]) {
                    // 4분면으로 재귀시켜 버리기
                    // 현재의 count 객체에 + 재귀로 들어간 count 숫자 더해주기
                    return count(offsetX, offsetY, h, arr)
                            .add(count(offsetX + h, offsetY, h, arr))
                            .add(count(offsetX, offsetY + h, h, arr))
                            .add(count(offsetX + h, offsetY + h, h, arr));
                }
            }
        }

        // 1과 0 한 칸 일 때 return 값
        if (arr[offsetX][offsetY] == 1) {
            return new Count(0, 1);
        }
        return new Count(1, 0);
    }
    public int[] solution(int[][] arr) {
        Count count = count(0, 0, arr.length, arr);
        return new int[]{count.zero, count.one};
    }
}
