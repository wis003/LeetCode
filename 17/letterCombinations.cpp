// Letter Combinations of a Phone Number

#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
	std::unordered_map<char, std::vector<char>> numberToLetter;

	public:
		Solution() {
			std::vector<char> vec2{'a', 'b', 'c'};
			std::vector<char> vec3{'d', 'e', 'f'};
			std::vector<char> vec4{'g', 'h', 'i'};
			std::vector<char> vec5{'j', 'k', 'l'};
			std::vector<char> vec6{'m', 'n', 'o'};
			std::vector<char> vec7{'p', 'q', 'r', 's'};
			std::vector<char> vec8{'t', 'u', 'v'};
			std::vector<char> vec9{'w', 'x', 'y', 'z'};

			numberToLetter['2'] = vec2;
			numberToLetter['3'] = vec3;
			numberToLetter['4'] = vec4;
			numberToLetter['5'] = vec5;
			numberToLetter['6'] = vec6;
			numberToLetter['7'] = vec7;
			numberToLetter['8'] = vec8;
			numberToLetter['9'] = vec9;
		}

		std::vector<std::string> letterCombinations(std::string digits) {
			std::vector<std::string> output;
			for(int i = 0; i < digits.size(); i++) {
				output = recurse(output, digits[i]);
			}

			return output;
		}

		std::vector<std::string> recurse(std::vector<std::string> input, char digit) {
			std::vector<std::string> output;
			std::vector<char> mapping = numberToLetter[digit];
			if(input.size() == 0) {
				for(char letter : mapping) {
					output.push_back("" + letter);
				}
			}
			else {
				for(std::string combination : input) {
					for(char letter : mapping) {
						output.push_back(combination + letter);
					}
				}
			}
			return output;
		}
};


int main() {
	std::string test1 = "23";
	Solution object;
	std::vector<std::string> output = object.letterCombinations(test1);

	for(std::string combination : output) {
		std::cout << combination << std::endl;
	}
	return 0;
}