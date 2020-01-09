/* 字符串简介

字符串实际上是一个 unicode 字符数组。你可以执行几乎所有我们在数组中使用的操作，自己试试看吧。
然而，二者之间还是存在一些区别。在这篇文章中，我们将介绍一些在处理字符串时应该注意的问题。这些特性在不同的语言之间可能有很大不同。

比较函数
字符串有它自己的比较函数（我们将在下面的代码中向你展示比较函数的用法）。

然而，存在这样一个问题：我们可以用 “==” 来比较两个字符串吗？

这取决于下面这个问题的答案：我们使用的语言是否支持运算符重载？

如果答案是 yes （例如 C++）。我们可以使用 “==” 来比较两个字符串。
如果答案是 no （例如 Java），我们可能无法使用 “==” 来比较两个字符串。当我们使用  “==” 时，它实际上会比较这两个对象是否是同一个对象。

是否可变
不可变意味着一旦字符串被初始化，你就无法改变它的内容。

在某些语言（如 C ++）中，字符串是可变的。 也就是说，你可以像在数组中那样修改字符串。
在其他一些语言（如  Java）中，字符串是不可变的。 此特性将带来一些问题。 我们将在下一篇文章中阐明问题和解决方案。
你可以通过测试修改操作来确定你喜欢的语言中的字符串是否可变。以下程序段有一个示例。

额外操作
与数组相比，我们可以对字符串执行一些额外的操作
你应该了解这些内置操作的时间复杂度。
例如，如果字符串的长度是 N，那么查找操作和子字符串操作的时间复杂度是 O(N)。
此外，在字符串不可变的语言中，你应该额外小心连接操作（我们将在下一篇文章中解释这一点）。
在计算解决方案的时间复杂度时，不要忘记考虑内置操作的时间复杂度。
 */

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s1 = "Hello World";
    cout << "s1 is \"Hello World\"" << endl;
    string s2 = s1;
    cout << "s2 is initialized by s1" << endl;
    string s3(s1);
    cout << "s3 is initialized by s1" << endl;
    // compare by '=='
    cout << "Compared by '==':" << endl;
    cout << "s1 and \"Hello World\": " << (s1 == "Hello World") << endl;
    cout << "s1 and s2: " << (s1 == s2) << endl;
    cout << "s1 and s3: " << (s1 == s3) << endl;
    // compare by 'compare'
    cout << "Compared by 'compare':" << endl;
    cout << "s1 and \"Hello World\": " << !s1.compare("Hello World") << endl;
    cout << "s1 and s2: " << !s1.compare(s2) << endl;
    cout << "s1 and s3: " << !s1.compare(s3) << endl;

    // Test whether string can be modified in C++
    s1[5] = ',';
    cout << s1 << endl; // It seems that string can be modified in C++.

    // Some extra special  operation to string
    // 1. concatenate
    s1 += "!";
    cout << s1 << endl;
    // 2. find
    cout << "The position of first 'o' is: " << s1.find('o') << endl;
    cout << "The position of last 'o' is: " << s1.rfind('o') << endl;
    // 3. get substr
    cout << s1.substr(6, 5) << endl;    

}