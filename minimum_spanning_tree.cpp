#include <boost/config.hpp>
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <boost/graph/adjacency_list.hpp>
#include <boost/tuple/tuple.hpp>
#include <boost/graph/kruskal_min_spanning_tree.hpp>

using namespace boost;
typedef property<edge_weight_t, int> EdgeProperty;
typedef adjacency_list<vecS, vecS, undirectedS,
	no_property, EdgeProperty> Graph;

enum Node {
	A, B, C, D
};
Graph CreateGraph()
{
	Graph g(4);
	add_edge(A, B, 2,g);
	add_edge(A, C, 1, g);
	add_edge(C, B, 3, g);
	add_edge(C, D, 4,g);
	add_edge(D, B,5,g);
	return g;
}
std::ostream& operator<<(std::ostream& stream, const Graph& g)
{
  	graph_traits < Graph >::vertex_iterator vi, end;
  	graph_traits < Graph >::adjacency_iterator ai, a_end;
  	graph_traits < Graph >::out_edge_iterator ei, e_end;
  	for (tie(vi, end) = vertices(g); vi != end; ++vi) {
		std::cout << "Node: "<< *vi << " has neighbors: ";
		tie(ai, a_end) = adjacent_vertices(*vi, g);
		for (; ai != a_end; ++ai) {
			std::cout << *ai;
			if (boost::next(ai) != a_end)
				std::cout << ", ";
		}
			std::cout << " has edges: ";
		for(tie(ei, e_end) = out_edges(*vi, g);ei != e_end; ++ei)
		{
			std::cout <<  *ei << " ";
		}
		std::cout << '\n';
	}
	return stream;
}

class WeightLess
{
	public:
		using Edge = graph_traits < Graph >::edge_descriptor;
		WeightLess(const property_map<Graph, edge_weight_t>::const_type& weight_map):weight_map{weight_map}
		{
		}
		bool operator()(const Edge& e1, const Edge& e2){
			return get(weight_map, e1 ) < get(weight_map, e2);
		}
		const property_map<Graph, edge_weight_t>::const_type& weight_map;
};

Graph MinimumSpanningTree(const Graph&  g)
{

	using Edge = graph_traits < Graph >::edge_descriptor;
	property_map<Graph, edge_weight_t>::const_type weight_map = get(edge_weight, g);

	//property_map<Graph, edge_weight_t>::type weight_map = get(edge_weight, g);

	Graph minimum_spanning_tree;
	WeightLess wl(weight_map);

	graph_traits < Graph >::vertex_iterator vi, end;
	graph_traits < Graph >::adjacency_iterator ai, a_end;
	graph_traits < Graph >::out_edge_iterator ei, e_end;
	std::set<Edge, WeightLess>  edges_to_visit(wl);
	std::set<Node>  visited_nodes;
	std::set<Edge>  visited_egdes;
	tie(vi, end) = vertices(g);
	std::cout << "first node: " << *vi << std::endl;
	visited_nodes.insert(static_cast<Node>(*vi));
	for(tie(ei, e_end) =out_edges(*vi, g); ei != e_end; ++ei)
	{
		edges_to_visit.insert(*ei);
	}

	while (visited_nodes.size()!=num_vertices(g))
	{
		std::cout << "to visit: ";
		for (const auto& edge: edges_to_visit)
		{
			std::cout << edge << " ";
		}
		std::cout << std::endl;

		const auto e_with_min_cost_iter = edges_to_visit.begin();
		const auto e_with_min_cost = *e_with_min_cost_iter;
		std::cout << "e_with_min_cost: "<<e_with_min_cost<<std::endl;
		visited_egdes.insert(e_with_min_cost);
		const auto neighor_node = target(e_with_min_cost, g);
		edges_to_visit.erase(e_with_min_cost_iter);
		if (visited_nodes.count(static_cast<Node>(neighor_node))==0)
		{
			visited_nodes.insert(static_cast<Node>(neighor_node));
			add_edge(source(e_with_min_cost,g),neighor_node, minimum_spanning_tree);
			std::cout << "Add edge: "<< source(e_with_min_cost,g)<< " "<<neighor_node << std::endl;
		}
		else{
			continue; //have already seen this node
		}

		std::cout << "for: " << neighor_node << " add edge: ";
		for(tie(ei, e_end) =out_edges(neighor_node, g); ei != e_end; ++ei)
		{
			if (visited_egdes.count(*ei) == 0) // not going back
			{
				edges_to_visit.insert(*ei);
				std::cout  << *ei << " ";
			}
			else
			{
				std::cout  <<"except: "<< *ei << " ";
			}
		}
		std::cout << "\n\n";
	}

	return minimum_spanning_tree;
}
int main()
{
	auto g = CreateGraph();
	auto min_g = MinimumSpanningTree(g);
	std::cout << g<< std::endl;
	std::cout << min_g<< std::endl;
	return 0;
}
