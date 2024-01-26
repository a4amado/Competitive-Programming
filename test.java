import java.util.*;

/**
 * test
 */
public class test {


    int num_of_paths(Integer[][] matrix, int row, int col, Map<String, Boolean> visit) {
        String place_key = Integer.toString(row) + Integer.toString(col);

        if (this.is_end_of_matrix(matrix, row, col)) return 1;
        if (this.is_out_of_range(matrix, row, col)) return 0;
        
        // is blocked
        if (matrix[row][col] == 1) return 0;
        if (visit.get(place_key) != null) return 0;


        visit.put(place_key, true);

        int count = 0;

        count = count + this.num_of_paths(matrix, row - 1, col, visit);
        count = count + this.num_of_paths(matrix, row + 1, col, visit);

        count = count + this.num_of_paths(matrix, row, col - 1, visit);
        count = count + this.num_of_paths(matrix, row, col + 1, visit);

        visit.remove(place_key);

        return count;

    };

 

    boolean is_out_of_range(Integer[][] matrix, int row, int col) {

        int  max_row = matrix.length  - 1;
        int  max_col = matrix[0].length  - 1;

        return row > max_row || col > max_col || row < 0 || col < 0;
    }
    boolean is_end_of_matrix(Integer[][] matrix, int row, int col) {

        int  max_row = matrix.length  - 1;
        int  max_col = matrix[0].length  - 1;

        return (row == max_row && col == max_col) ;
    }
 
    
    public static void main(String[] args) {
        test s = new test();
        Integer[][] m = {
                { 0, 0, 0, 0 },
                { 1, 1, 0, 0 },
                { 0, 0, 0, 1 },
                { 0, 1, 0, 0 },
        };
        Map<String, Boolean> visted = new HashMap<>();
        
        System.out.println(s.num_of_paths(m, 0, 0, visted));

    };
}


