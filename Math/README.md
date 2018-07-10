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




