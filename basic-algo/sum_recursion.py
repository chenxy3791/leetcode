"""
尾递归
在上一篇文章中，我们讨论了由于递归调用而在系统调用栈上产生的隐式额外空间。
然而，你应该学习识别一种称为尾递归的特殊递归情况，它不受此空间开销的影响。

尾递归函数是递归函数的一种，其中递归调用是递归函数中的最后一条指令。
并且在函数中应该只有一次递归调用。

我们已经在反转字符串的解决方案中看到了尾递归的例子。这里的另一个例子说明了
非尾递归和尾递归之间的区别。请注意，非尾递归示例中，在最后一次递归调用之后
有一个额外的计算。

尾递归的好处是，它可以避免递归调用期间栈空间开销的累积，因为系统可以为每个
递归调用重用栈中的固定空间。

例如，对于递归调用序列 f(x1) -> f(x2) -> f(x3)，如果函数 f(x) 以尾递归的
形式实现。那么其执行步骤的顺序和栈空间的分配如下所示：
[There is one illustration figure here]

请注意，在尾递归的情况下，一旦从递归调用返回，我们也会立即返回，因此我们可以
跳过整个递归调用返回链，直接返回到原始调用方。这意味着我们根本不需要所有递归
调用的调用栈，这为我们节省了空间。

例如，在步骤（1）中，栈中的一个空间将被分配给 f(x1)，以便调用 f(x2)。然后，
在步骤（2）中，函数 f(x2) 能够递归地调用 f(x3)，但是，系统不需要在栈上分配
新的空间，而是可以简单地重用先前分配给第二次递归调用的空间。最后，在函数 f(x3) 
中，我们达到了基本情况，该函数可以简单地将结果返回给原始调用方，而不会返回到
之前的函数调用中。

尾递归函数可以作为非尾递归函数来执行，也就是说，带有调用栈并不会对结果造成影响。
通常，编译器会识别尾递归模式，并优化其执行。
然而，并不是所有的编程语言都支持这种优化，比如 C，C++ 支持尾递归函数的优化。
另一方面，Java 和 Python 不支持尾递归优化。
"""
def sum_non_tail_recursion(ls):
    """
    :type ls: List[int]
    :rtype: int, the sum of the input list.
    """
    if len(ls) == 0:
        return 0
    
    # not a tail recursion because it does some computation after the recursive call returned.
    return ls[0] + sum_non_tail_recursion(ls[1:])


def sum_tail_recursion(ls):
    """
    :type ls: List[int]
    :rtype: int, the sum of the input list.
    """
    def helper(ls, acc):
        if len(ls) == 0:
            return acc
        # this is a tail recursion because the final instruction is a recursive call.
        return helper(ls[1:], ls[0] + acc)
    
    return helper(ls, 0)