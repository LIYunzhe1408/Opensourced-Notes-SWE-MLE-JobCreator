## Multiple choice questions:
1. Given 2 bbox,  left_top point and right_bottom point of bbox1 is (100, 120) and (160, 200), while the ones of bbox2 is (140, 160) and (180, 240). Solve the IOU
2. Average Run Time complexity of Quick Sort
3. A full binary tree has 8 leaf nodes at layer 6, what's the largest possible number of all nodes in this tree.
4. int x = 5&6, solve x = 
5. A model is used to detect cats. Given 100 cats and some dogs images, 14 dogs were mis-detected as cats, and 6 cats are detected as non-cat. Solve precision and recall.
6. reg [23:0] rand; rand = {$random} % 60. Solve the range of rand.
7. Input image is (256, 256, 3), after the convolution of `nn.Conv2d(3, 16, 3, stride=2), solve the size of the output.
8. BERT is a model with (encode / decoder / encoder + decoder)
9. $(3, 4, -12)^T$, solve L1-norm and L2-norm
10. The way to describe the rotation of a rigid body.
11. Illegal usage of dictionary. {[1,2,3]: 1}, {(1, 2, 3): 1}, {3:5}
12. Convert hex digit to octal digit of 255
13. Which activation function can reach -0.001. tanh, sigmoid, ReLu
14. The description of CLIP model.
15. Remove first element of a non-null Circular linked list, p is the last pointer, q is a temp pointer, h is the head pointer.
16. Solve the output
    ```python
        char *a = "ABCDEF"
        for (char *bp = a, *bp, b+=2)
        print("%s", bp)
    ```
17. Describe KMeans: The choice of initial center has a huge impact to final result; KMeans cannot detect the number of clusters, it randomly pick center points; When input data is not to many, the sequence of input will influence a lot; KMeans cannot detect the number of cluster, it will not randomly pick center points.
18. A stack, with sequence of in-stack a b c d e. After push, push, pop, push,  pop, push, push, pop, get the sequence of out-stack. What is it?
19. Which one is convex optimization. Given a function, solve max(xxxx) or min(xxxx)
20. Description of Fully Connected Layer.
21. In Attention mechanism, the shape of Q K V are all NLD, but padding elements are existing in Q and K. How to implement masked attention? Set 0 or -inf at the mask position, after softmax or before softmax.


## Coding Question
Write the attention mechanism with PyTorch or NumPy, QKV are 3 dimensional vectors. Try to implement the class Attention.
* Clarify the meaning and the shape of input and output
* Complete scaled dot-product attention
* If possible, implement multi-head attention