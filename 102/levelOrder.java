import java.util.ArrayList;
import java.util.List;

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {

    public static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> out = new ArrayList<List<Integer>>();
        int h = height(root);
        for(int i = 1; i <= h; i++) {
            List<Integer> nodes = new ArrayList<Integer>();
            getGivenLevel(nodes, root, i);
            out.add(nodes);
        }
        return out;
    }
 
    public static int height(TreeNode root) {
        if(root == null) {
           return 0;
        }
        else {
            int lheight = height(root.left);
            int rheight = height(root.right);

            if(lheight > rheight) {
                return lheight + 1;
            }
            else {
                return rheight + 1;
            }
        }
    }
 
    public static void getGivenLevel(List<Integer> nodes, TreeNode root, int level) {
        if(root == null) {
            return;
        }
        if(level == 1) {
            nodes.add(root.val);
        }
        else if(level > 1) {
            getGivenLevel(nodes, root.left, level - 1);
            getGivenLevel(nodes, root.right, level - 1);
        }
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);


        List<List<Integer>> test1 = new ArrayList<List<Integer>>();
        test1 = levelOrder(root);
        for(List<Integer> i : test1) {
            for(Integer j : i) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }
}