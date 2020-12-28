#include <vector>
#include <iterator>
#include <algorithm>
#include <iostream>

using namespace std;
class Solution {
  public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
      std::vector<int> combined;
      combined.reserve(nums1.size()+ nums2.size());
      combined = nums1;
      combined.insert(combined.end(), nums2.begin(), nums2.end());
      size_t index_num2_begin=nums1.size();
      size_t j=0;
      for (auto i=index_num2_begin;i<combined.size();++i)
      {
        while(combined[i] > combined[j] && j < combined.size())
        {
          ++j;
        }
        std::rotate(combined.begin()+j, combined.begin()+i, combined.begin()+i+1);
        std::copy(combined.begin(), combined.end(), std::ostream_iterator<int>(std::cout, ","));
        std::cout << std::endl;
        ++j;
      }

      auto index = combined.size()/2;
      if (combined.size()%2==0)
      {
        return (combined[index] + combined[index-1])/2.0;
      }
      else{
        return combined[index];
      }
    }
};
int main()
{
  Solution s;
  std::vector<int> nums1={3};
  std::vector<int> nums2={-2,-1};
  auto result = s.findMedianSortedArrays(nums1, nums2);
  std::cout << result << std::endl;
  return 0;
}
