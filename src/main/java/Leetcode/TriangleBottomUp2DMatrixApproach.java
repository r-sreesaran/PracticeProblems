package Leetcode;

import java.util.LinkedList;
import java.util.List;

public class TriangleBottomUp2DMatrixApproach {
    public int minimumTotal(List<List<Integer>> triangle) {
        int[][] minSum = new int[triangle.size()][triangle.size()];

        for (int r = triangle.size() - 1; r >= 0; r--) {
            for (int c = r; c >= 0; c--) {
                if (r == triangle.size() - 1) {
                    minSum[r][c] = triangle.get(r).get(c);
                    continue;
                }

                minSum[r][c] =
                        Math.min(minSum[r + 1][c], minSum[r + 1][c + 1]) + triangle.get(r).get(c);
            }
        }

        return minSum[0][0];
    }

    public  int miniSum(List<List<Integer>> triangle) {
        int totalsum =0;
        for (List<Integer> rows : triangle) {
            int minsum=10000;
            for (int number: rows) {
                if (number<minsum) {
                    minsum = number;
                }
            }
            totalsum+=minsum;
        }
return totalsum;
    }

    public static void main(String args[]) {
        TriangleBottomUp2DMatrixApproach test = new TriangleBottomUp2DMatrixApproach();
        List<List<Integer>> triangle = new LinkedList<>();
        List<Integer> rows1 = new LinkedList<>();
        rows1.add(-1);
        triangle.add(rows1);

        List<Integer> rows2 = new LinkedList<>();
        rows2.add(2);
        rows2.add(3);
        triangle.add(rows2);

        List<Integer> rows3 = new LinkedList<>();
        rows3.add(1);
        rows3.add(-1);
        rows3.add(-3);
        triangle.add(rows3);


        System.out.println(test.minimumTotal(triangle));

    }
}
