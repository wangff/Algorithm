# Math

## 343 Integer Break

Assume we break n into n/x number of x, then the product will be x^(n/x).

And we want to maximize it.

Taking its derivative gives us:

$$ y=x^{\dfrac{n}{x}} \\
(\ln y)'=(\ln x^ {\dfrac{n}{x}})'\\
\dfrac{y'}{y} = (\dfrac{n}{x})'ln x + \dfrac{n}{x}(ln x)'\\
\dfrac{y'}{y} = -nx^{-2}ln x + nx^{-2}\\
\dfrac{y'}{y} = n(1-ln x)x^{-2}\\
y' = n(1-ln x)x^{-2} * x^{\dfrac{n}{x}}\\
y' = n(1-ln x)x^{\dfrac{n}{x}-2}
$$

The derivative is positive when 0<x<e, and equal to 0 when x = e, then becomes negative when x >e,
which indicates that the product increases as x increases, then reaches its maximum when x=e, then starts dropping.

Thus, if n is sufficiently large and we are allowed to brea n into real numbers, the best idea is to break it into nearly all e's.

On the other hand, if we can only break n into integers, we should choose integers that are closer to e.

The only potential candidates are 2 and 3 since 2<e<3, but we will generally prefer 3 to 2. Why?

6=2+2+2=3+3, but 2*2*2<3*3

All the analysis above assumes n is significantly large. When n is small, it may contain flaws.


For instance, when n = 4, we have 2*2>3*1

## 357. Count Numbers with Unique Digits

Let f(n) = count of number with unique digits of length n.
$f(1) = 10$
$f(2) = 9*9$
$f(3) = f(2)*8$
$f(4) = f(3)*7$
$......$
$f(10) = f(9)*1$
$f(11) = 0 = f(12)=f(13)$

Any number with length > 10 couldn't be unique digits number.
The problem is asking for numbers from 0 to 10^n. 
Hence return f(1)+f(2)..+f(n)

## 258. Add digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

If an integer is like 100a+10b+c, then (100a+10b+c)%9=(a+99a+b+9b+c)%9=(a+b+c)%9

```
class Solution:
	def addDigits(self, num):
		if num<10: return num
		return num%9 if num%9>0 else 9

```

## 69. Sqrt(x) - Newton's method

Find a solution for the equation $ x^2-n=0$, giving the iterative formula:

$$x_{k+1} = \dfrac{1}{2}\left(x_{k}+\dfrac{n}{x_{k}}\right)\\
k\geq0\\
x_{0}\geq0
$$

The sequence $\left\{x_{k}\right\}$converges quadratically to $\sqrt{n} $ as $ k\rightarrow\infty$. It can be proven that if $ x_{0} = n $ is chosen as the initial guess, one can stop as soon as $\left| x_{k+1} - x_{k}\right| < 1$ to ensure that $\lfloor x_{k+1} \rfloor = \lfloor \sqrt{n}\rfloor$.

