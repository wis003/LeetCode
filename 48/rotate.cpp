// Rotate Image

#include <vector>
#include <iostream>

using namespace std;

class Solution {
    public:
        void rotate(vector<vector<int>>& matrix) {
            int length = matrix.size();
            for(int row = 0; row < length; row++) {
                for(int column = 0; column < length; column++) {
                    if(column >= row && column < length - row - 1) { // positions to operate on
                        int i = 0;
                        int nextRow = row;
                        int nextColumn = column;
                        int currValue = matrix[nextRow][nextColumn];
                        while(i < 4) {
                            
                            // [x, y] --> [y, length - x - 1]
                            int temp = nextRow;
                            nextRow = nextColumn;
                            nextColumn = length - temp - 1;

                            // swap
                            int nextValue = matrix[nextRow][nextColumn];
                            matrix[nextRow][nextColumn] = currValue;
                            currValue = nextValue;
                            i++;
                        }
                    }
                }
            }
        }
};