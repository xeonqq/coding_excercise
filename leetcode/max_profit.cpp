#include<algorithm>
#include<cassert>
#include<vector>
#include <limits>
using namespace std;
class Solution {
	public:
		int maxProfit(vector<int>& prices) {
			if (prices.empty())
			{
				return 0;
			}
			int max_profit = 0;
			int prev_bought_price = prices[0];

			for(size_t i=1;i< prices.size();i++) {
				auto sell_price = prices[i];
				auto profit = sell_price - prev_bought_price;
				if (profit > max_profit){
					max_profit = profit;
				}
				if (prices[i] < prev_bought_price)
				{
					prev_bought_price = prices[i];
				}
			}
			return max_profit;
		}
};

int main()
{
	Solution s;
	std::vector<int> prices = {7,1,5,3,6,4};
	std::vector<int> prices2 = {7,6,4,3,1};
	std::vector<int> prices3 = {1, 2};
	std::vector<int> prices4 = {7,1,5,3,0,4,6};
	assert((s.maxProfit(prices) == 5));
	assert((s.maxProfit(prices2) == 0));
	assert((s.maxProfit(prices3) == 1));
	assert((s.maxProfit(prices4) == 6));
	return 0;
}
