
class Solution {

    // A simple custom class to represent coordinates
    class Coord {
        int row;
        int col;

        public Coord(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }

    /**
     * Solves the Islands and Treasure problem using a multi-source BFS.
     * The grid is modified in-place to store the shortest distances.
     *
     * @param grid The grid representing the rooms, walls, and treasures.
     * - 0: A treasure room
     * - -1: A wall
     * - A large number (e.g., Integer.MAX_VALUE): An empty room
     */
    public void islandsAndTreasure(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return;
        }

        Queue<Coord> queue = new ArrayDeque<>();
        int numRows = grid.length;
        int numCols = grid[0].length;

        // Initialize the queue with all treasure locations (the BFS sources).
        for (int r = 0; r < numRows; r++) {
            for (int c = 0; c < numCols; c++) {
                if (grid[r][c] == 0) {
                    queue.add(new Coord(r, c));
                }
            }
        }

        // Define the four possible directions for movement (up, down, left, right).
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        // Perform the multi-source BFS.
        while (!queue.isEmpty()) {
            Coord current = queue.poll();
            int row = current.row;
            int col = current.col;

            // Explore the four neighbors of the current cell.
            for (int[] dir : directions) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];

                // Check for a valid neighbor that is an empty room.
                // A valid neighbor must be within bounds, not a wall, and not yet visited
                // (which is checked by seeing if its value is still Integer.MAX_VALUE).
                if (newRow >= 0 && newRow < numRows &&
                    newCol >= 0 && newCol < numCols &&
                    grid[newRow][newCol] == Integer.MAX_VALUE) {

                    // Update the distance and add the neighbor to the queue.
                    grid[newRow][newCol] = Math.min(grid[row][col] + 1, grid[newRow][newCol]);
                    queue.add(new Coord(newRow, newCol));
                }
            }
        }
    }
}