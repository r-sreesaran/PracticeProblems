package arrays;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class SudokoSolver {

    public static void main(String[] args) {
    }

    private static boolean hasDuplicate(List<List<Integer>> partialAssignment,
                                        int startRow, int endRow, int startCol,
                                        int endCol) {
        List<Boolean> isPresent = new ArrayList<>(
                Collections.nCopies(partialAssignment.size() + 1, false));
        for (int i = startRow; i < endRow; ++i) {
            for (int j = startCol; j < endCol; ++j) {
                if (partialAssignment.get(i).get(j) != 0
                        && isPresent.get(partialAssignment.get(i).get(j))) {
                    return true;
                }
                isPresent.set(partialAssignment.get(i).get(j), true);
            }
        }
        return false;
    }

}
