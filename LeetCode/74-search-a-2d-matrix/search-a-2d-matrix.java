class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        int low = 0;
        int high = matrix.length - 1;
        int mid = (low + high) / 2;

        while (high >= low) {
            if (matrix[mid][matrix[mid].length - 1] < target) {
                
                low = mid  + 1;
                mid = (low + high) / 2;
            } else if (matrix[mid][0] > target) {
                high = mid - 1;
                mid = (low + high) / 2;
            } else {
                break;
            }

        }

        low = 0;
        high = matrix[mid].length - 1;
        int col_mid = (low + high) / 2;


        while (high >= low) {
            if (matrix[mid][col_mid] > target) {
                high = col_mid - 1;
                col_mid = (low + high) / 2;
            } else if (matrix[mid][col_mid] < target) {
                low = col_mid + 1;
                col_mid = (low + high) / 2;
            } else {
                return true;
            }

        }

        return false;
    }
}