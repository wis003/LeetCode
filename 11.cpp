// Container With Most Water

#include <iostream>
#include <vector>

int maxArea(std::vector<int>& height) {
    int max = 0;
    int bottom = 0;
    int top = height.size() - 1;

    while(bottom < top) {
        int wallHeight = std::min(height[bottom], height[top]);
        if(max < wallHeight * (top - bottom)) max = wallHeight * (top - bottom);
        while(height[bottom] <= wallHeight && bottom < top) bottom++;
        while(height[top] <= wallHeight && bottom < top) top--;
    }

    return max;
}

int main() {
    std::vector<int> test1 = {1,8,6,2,5,4,8,3,7};
    std::vector<int> test2 = {1,1};
    std::vector<int> test3 = {4,3,2,1,4};
    std::vector<int> test4 = {1,2,1};

    std::cout << maxArea(test1) << std::endl;
    std::cout << maxArea(test2) << std::endl;
    std::cout << maxArea(test3) << std::endl;
    std::cout << maxArea(test4) << std::endl;

    return 0;
}