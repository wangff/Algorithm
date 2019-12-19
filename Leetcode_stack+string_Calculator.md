# Leetcode summary stack+string

## Only Character, numbers, bracket
1. No precedence evaluation
2. 726 number of atoms:
    1. See the pattern of string, to see:
        1. how much we could process in one pass with no push in and pop out stack
        2. 字符数字
    2. （ we must push in to the stack:
        1. say what we should push in
            1. record the status of last stack level
            2. we be used again after processing all the things in ()
    3. ) we must push out to the stack:
        1. push out previous status
        2. update current status
3. 736 Parse Lisp Expression
    1. Input _expression_, must be one of the following three types of expression
        1. add -> evaluatedAdd
        2. mult -> evaluateMult
        3. let -> evaluateLet
    2. All the three types of expression can be thought of as composed by operands, each operand can be 
        1. Integer: An integer could be positive or negaive
        2. a variable: start with a lowercase letter, then zero or more lowercase letters or digits.
        3. another expression as step 1, and expression will be enclosed in paratheses
    3. An _add_ expression contains 2 operands
    4. An _mul_ expression contains 2 operands
    5. A _let_ expression contains _2m+1_ operands
        1. evaluated to be the value of the last operand
        2. The first m pairs of operands correspond to m assignments
            1. The first operand is a variable
            2. The second can be an integer, a variable or another expression.
            3. To simulate the assignment operations, maintain a _HashMap_.
            4. To simulate the concept of scope, the assigned values will be placed in a stack
    6. For the given expression
        1. getOperand: 
            1. the function will obtain the string representation of operand starting from the specified _offset_ into the expression e
        2. evaluateOperand: 
            1. this function will evaluate the operand string obtain above. 
            2. an operand of integer type -> parse the string as an integer.
            3. an operand of variable type -> look up the value in the hash map
            4. an operand of expression type -> recursively call the evaluate function to resolve its value.
    

## Calculator

### Steps - Non-negative, (),

\- 224 Basic Calculator : level 1 + ()

\- 227 Basic Calculator II : level 1 + level 2

\- 772 Basic Calculator III : level 1 + level 2 + ()

Line |Two precedence | One precedence
-----------|------------|------------
Precendence |l1: o1 = + ; l1 = 0 or -1 (-x is valid) <br> l2: o2 = * or /; l2 = 1 | l1: o1 = + ; l1 = 0 or -1 (if -x is valid) 
Traverse the string|Traverse the string | Traverse the string 
ch is digit | to get num. evaluate l2 (use num) | to get num. evaluate l1 (use num)
ch is variable| get the value, evaluate l2(use num)|get the value, evaluate l1(use num)
ch is (|push l1 o1 in stack<br>push l2 o2 in stack<br>reset l1 o1 and l2 o2|push l1 o1 in stack<br>reset l1 o1 
ch is )| evaluate l1 and store it to num <br> pop o2 l2<br>pop o1 l1<br>evaluate l2| evaluate l1 and store it to num <br> pop o1 l1<br>evaluate l1
if ch is o2|update o2|
if ch is o1|evalute l1<br>update o1<br>reset o2|update o1
At the end | evaluate o1(use l2)|
