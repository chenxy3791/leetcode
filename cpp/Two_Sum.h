#include <vector>
#include <map>


class Solution_Hash {
public:
  vector<int> twoSum(vector<int>&numbers, int target) {
    map<int, int> mapping;
    vector<int> result;
    for (unsigned int i = 0; i < numbers.size(); i++)
    {
      mapping[numbers[i]] = i;
    }
    for (unsigned int i = 0; i < numbers.size(); i++)
    {
      int searched = target - numbers[i];

      // c.end(): Returns an iterator for the position after the last element
      // Refer to <<The C++ Standard Library>>#Table6.1
      // map.find(key): Returns the position of the first element with key key or end()
      // Refer to <<The C++ Standard Library>>#Table6.28
      if (mapping.find(searched) != mapping.end() && i != mapping[searched])
      {
        result.push_back(i + 1);
        result.push_back(mapping[searched] + 1);
        break;
      }
    }
    return result;
  }
};