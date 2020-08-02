#include <cassert>
#include <array>
class Solution {
public:
    int uniquePaths(int m, int n) {
	    int map[n][m];
	    for (int i = 1; i < m; ++i)
	    {
	    	map[0][i] = 1;
	    }
	    for (int j = 1; j < n; ++j)
	    {
	    	map[j][0] = 1;
	    }

	    for (int row = 1; row < n; ++row)
		    for (int col = 1; col < m; ++col){
			map[row][col] = map[row][col-1] + map[row-1][col];

		    }
	    return map[n-1][m-1];
    }
};

int main()
{
	Solution s;
	assert((s.uniquePaths(7,3) == 28));
	return 0;
}
