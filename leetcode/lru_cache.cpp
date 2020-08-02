#include <list>
#include <iostream>
#include <unordered_map>
#include <algorithm>

class LRUCache {
	struct Value{
		int value;
		std::list<int>::iterator position;
	};
	public:
	LRUCache(int capacity) : capacity_{capacity}{

	}

	int get(int key) {
		if (map_.count(key) != 0)
		{
			auto& result = map_[key];
			lru_list_.splice(lru_list_.end(), lru_list_, result.position);
			result.position = std::prev(lru_list_.end()); // update postion
			return result.value;
		}else{
			return -1;
		}
		}

		void put(int key, int value) {
			if (map_.count(key) == 0)
			{
				if (map_.size() == capacity_)
				{
					auto& key_to_delete = lru_list_.front();
					map_.erase(key_to_delete);
					lru_list_.pop_front();
				}
				lru_list_.push_back(key);
				map_.insert(std::make_pair(key, Value{value, std::prev(lru_list_.end())}));
			}else
			{
				auto& result = map_[key];
				lru_list_.splice(lru_list_.end(), lru_list_, result.position);
				result.value = value;
				result.position = std::prev(lru_list_.end());
			}
		}
	private:
		std::list<int> lru_list_;
		std::unordered_map<int,Value> map_;
		const int capacity_;

};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
int main() {

	LRUCache cache = LRUCache( 2 /* capacity */ );

	cache.put(1, 1);
	cache.put(2, 2);
	std::cout << cache.get(1) <<std::endl;       // returns 1
	cache.put(3, 3);    // evicts key 2
	std::cout << cache.get(2)<<std::endl;       // returns -1 (not found)
	cache.put(4, 4);    // evicts key 1
	std::cout << cache.get(1)<<std::endl;       // returns -1 (not found)
	std::cout << cache.get(3)<<std::endl;       // returns 3
	std::cout << cache.get(4)<<std::endl;       // returns 4




	LRUCache cache2 = LRUCache( 2 /* capacity */ );
	cache2.put(2, 1);
	cache2.put(2, 2);
	std::cout << cache2.get(2) <<std::endl;       // returns 2
	cache2.put(1, 1);    // evicts key 2
	cache2.put(4, 1);    // evicts key 1
	std::cout << cache2.get(2)<<std::endl;       // returns -1 (not found)
	return 0;
}
