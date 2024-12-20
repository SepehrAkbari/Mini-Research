# Measuring the Efficiency of Binary Search Trees

## Research Question

This project investigates the efficiency of re-balancing algorithms in Binary Search Trees (BSTs), specifically comparing the time complexity of the insertion operations in a **Splay Tree** and an **Adelson-Velskii and Landis Tree (AVL Tree)**.

### Research Objective

The main objective of this research is to analyze how the re-balancing efficiency of a **Splay Tree** compares to that of an **AVL Tree** in terms of time complexity, focusing on their performance during value insertions. This comparison is conducted through a series of computational experiments, measuring the execution time of insertion operations.

## Files Included

- **splaytree.c**: Implements the Splay Tree data structure. The program takes user input, inserts values into the tree, and outputs the in-order traversal of the Splay Tree.
  
- **avltree.c**: Implements the AVL Tree, a self-balancing BST. Similar to the Splay Tree program, it takes user input, inserts values, and provides the in-order traversal.

- **testing.java**: Automates the execution of both the **splaytree.c** and **avltree.c** programs. It measures the execution time of the insertion operations in nanoseconds and outputs a comparative performance analysis.

## Usage Instructions

1. **Compile the C Programs:**
   - Ensure that you have a C compiler installed (e.g., GCC).
   - Compile the Splay Tree program:  
     `gcc splaytree.c -o splaytree`
   - Compile the AVL Tree program:  
     `gcc avltree.c -o avltree`
   
2. **Run the Testing Script:**
   - Make sure all compiled programs are in the same directory.
   - Compile and run the Java testing script:  
     `javac testing.java`  
     `java testing`
   
3. **Input:**
   - The programs prompt the user to input a series of numbers for insertion into the trees.
   
4. **Output:**
   - The testing script will output the in-order traversal of each tree and display the time taken for insertion in nanoseconds, comparing the efficiency of the Splay Tree and AVL Tree.

## Project Overview

This project aims to measure and compare the time complexity of the re-balancing operations that occur when values are inserted into both types of trees. The testing framework will facilitate the collection of data on how each algorithm performs in terms of execution time and efficiency.

## Conclusion

By the end of the project, we will provide a comprehensive analysis of the differences in re-balancing efficiency between Splay Trees and AVL Trees, contributing valuable insights into the performance of these data structures.