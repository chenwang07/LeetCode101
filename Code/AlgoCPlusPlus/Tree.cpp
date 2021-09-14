#include<memory>


template<typename T>
struct BinaryTreeNode {
	T data;
	std::unique_ptr<BinaryTreeNode<T>> left, right;
};






void TreeTraversal(const std::unique_ptr <BinaryTreeNode<int>>& root) {

}