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

int main() {
    Solution object;
    vector<vector<int>> matrix {{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}};
    object.rotate(matrix);
    for(auto i : matrix) {
        for(auto j : i) {
            cout << j << " ";
        }
    }
    return 0;
}