#include <algorithm>
#include "algorithmDeclaration.h"


int maxDepth(TreeNode* root) {
	return root ? 1 + std::max(maxDepth(root->left), maxDepth(root->left)) : 0;
}