// Container With Most Water

#include <iostream>
#include <vector>

int maxArea(std::vector<int>& height) {
    int max = 0;
    for(int i = 0; i < height.size(); i++) {
        for(int j = i + 1; j < height.size(); j++) {
            int wallHeight = (height[i] < height[j]) ? height[i] : height[j];
            if(max < wallHeight * (j - i)) max = wallHeight * (j - i);
        }
    }
    return max;
}

int main() {
    std::vector<int> test1 = {1,8,6,2,5,4,8,3,7};
    std::cout << maxArea(test1) << std::endl;
    return 0;
}