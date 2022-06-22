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
			std::vector<std::string> working;
			for(int i = 0; i < digits.size(); i++) {
				working = output;
				output = recurse(working, digits[i]);
			}

			return output;
		}

		std::vector<std::string> recurse(std::vector<std::string> input, char digit) {
			std::vector<std::string> output;
			std::vector<char> mapping = numberToLetter[digit];
			if(input.size() == 0) {
				for(char letter : mapping) {
					output.push_back(std::string(1, letter));
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
	Solution object;

	std::string test1 = "2";
	std::string test2 = "23";
	std::string test3 = "237";
	

	std::vector<std::string> comb1 = object.letterCombinations(test1);
	std::vector<std::string> comb2 = object.letterCombinations(test2);
	std::vector<std::string> comb3 = object.letterCombinations(test3);

	std::string out1, out2, out3;

	for(std::string combination : comb1) {
		out1 = out1 + combination + " ";
	}

	for(std::string combination : comb2) {
		out2 = out2 + combination + " ";
	}

	for(std::string combination : comb3) {
		out3 = out3 + combination + " ";
	}

	std::cout << out1 << comb1.size() << std::endl;
	std::cout << out2 << comb2.size() << std::endl;
	std::cout << out3 << comb3.size() << std::endl;

	return 0;
}