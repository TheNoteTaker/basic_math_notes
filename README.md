# Math Notes

# General Notes

## Checking If a Number Is Divisible

- **2**: Check if the last number is divisible by 2.
- **3**: Add each individual number and check if it's divisible by 3.
    - This can be repeated
- **4**: Check if the last two digits are divisible by 4.
- **5**: Check if the last number is divisible by 5.
- **7**: Take off and multiply the last number by 2. Subtract it from the
  remaining digits. If it's 0 or a number divisible by 7, it is. Repeat if the
  number is too large, until there's an easy to tell number.
    1. 203
    2. Take off 3 and multiply by 2 = 6
    3. Subtract 6 from 20 = 14
    4. 20 is not divisible by 7, so it's not divisible by 7.
- **8**: If the last three digits are divisible by 8, then it is.
    - If the first digit of the 3-digit number is even, then the entire number
      is divisible by 8 if the last two digits are divisible by 8.
    - If the first digit of the number is odd, then subtract the number 4 from
      the last two digits and check to see if this new number is divisible by 8.
      If it is, then the entire number is too.
- **If a number is divisible by the factors numbers that make it up,
  then it is also divisible by that number**
    - **6**: If it's divisible by both 2 and 3, it is.
    - **9**: If it's divisible by 3, it is. You can also add the numbers and see
      if it's divisible by 3.

# Fractions

**Reciprocal:** A number that, when multiplied by another number, equals 1.

- The reciprocal of 3/4 is 4/3

## Dividing Fractions

1. **Keep** - Keep the first fraction the same
2. **Change** - Change the division symbol to multiplication
3. **Flip** - Flip the second fraction to get the reciprocal

# Ratios and Rates

- **Ratio:** compares two quantities by division, or describes the relationship
  between two quantities
- **Rate:** A ratio that compares quantities that are measured in different
  units
- **Unit Rate:** compares a quantity to one unit of measure

# Proportions

![](assets/proportions.png)

- The units must be the same. Convert if needed.

## Cross Products

To check if a proportion is true, use cross multiplication.

- If they're equal, it's true.

### Example 1

![](assets/proportions_multiplication.png)

# Variables and Real Numbers

## Variables and Expressions

- **Constant:** A number or symbol that represents a quantity that cannot change
- **Variable:** A letter or symbol used to represent a quantity that can change
- **Expression:** A mathematical phrase that contains operations, numbers,
  and/or variables.

## Integers

- **Counting/Natural Numbers:** Positive numbers only
- **Whole Numbers**: All the natural numbers + zero
- **Integers:** All negative and positive numbers
- **Absolute Value:** A nubmer's distance from zero, regardless of its sign
    - Displayed by using pipes one eacn side:
        - **|-3|** and **|3|** are both the same: **3**

## Rational and Real Numbers

- **Real Numbers:** Contain all integers (negative and positive). Consists of
  two sets:
    1. **Rational Numbers**
        - Numbers that can be written as the ratio of two integers, where the
          denominator is not zero.
            - Integers
            - Whole numbers
            - Natural numbers
            - A terminating or repeating decimal is a rational number.
    2. **Irrational Numbers**
        - Numbers that cannot be written as the ratio of two integers
        - Irrational numbers do not repeat and are non-terminating decimals.
        - Numbers that do not have a perfect square are also irrational.

### Adding Real Numbers

When adding real numbers, first change all the signs to be the same.

#### Same sign

1. Add their absolute values
2. Assign same sign to sum

#### Different signs

1. Find the difference of the absolute values
2. The sum gets the same sign as the number
   with the larger absolute value

**The identity property of 0:** Adding 0 to other numbers doesn't change their
value.

### Subtracting Real Numbers

**Additive Inverses:** Two numbers whose sum is **0**.

When subtracting a negative number, use its additive inverse instead.

### Multiplying and Dividing Real Numbers

- **Additive Identity:** 0
- **Multiplicative Identity:** 1
    - You can multiply any number by this without changing it.
- **Multiplicative Inverse (Reciprocal):** Two numbers that when multiplied
  equal the multiplicative identity.

#### Division

Keep, Change, Flip

#### For multiplication:

1. Multiply the top numbers
2. Multiply the bottom numbers
3. Simplify

# Solving Equations and Inequalities

## Special Cases and Applications

### Solving Applications

First get all the constants (The things that we know that are not going to
change), then create the variable (The thing that you're trying to find out.)

### Special Cases

The variable disappears on both sides, and you don't get a solution. Instead,
you get either a **True** or **False** statement.

- If it's **True**, then there's infinite solutions.
- If it's **False**, then there are no solutions.

1. `x + 5 = 5 + x`
2. `5 = 5`
    - This is true since 5 does equal 5.

#### Example

The perimeter of Tina’s rectangular garden is 60 feet. If the length of the
garden is twice the width, what are the dimensions of the garden?

- `2X = Y`

1. `4X + 2Y = 60`
2. `X + X + X + X + 2Y = 60`
3. `X + X + X + X + X + X = 60`
4. `6X = 60`
5. `X = 10`
6. `Y = 20`

## Solving One-Step Inequalities

**Inequality**

a mathematical statement that shows the relationship between two expressions
where one expression can be greater than or less than the other expression

![](assets/inequalities.png)

- Inequalities can be solved similar to equations in that you can do the same
  thing to both sides.
- To check if an inequality is correct, substitute the solution value into the
  inequality to check if it holds up.
    - Check the endpoint of a **Greater/Less than (>/<)** by substituting the end
      point, and changing it to an **equals (=)** sign. Then check the point after
      and keep the sign the same.
- When multiplying by a negative number, remember to flip both sides.

### Recap

* When you multiply or divide both sides by a negative number, flip the
  inequality sign

* To check answers, check the endpoint in the related equation, and check the
  inequality by checking one or more solutions of the inequality.

## Solving Multi-Step Inequalities

1. Simplify
    - Distributive property (Eliminate parentheses)
    - Combine like-terms
2. Move variable terms to one side (usually left side)
3. Isolate variable term on one side by moving the numbers to the other side
4. Isolate variable by multiplying or dividing
    - Remember to flip the sign if multiplying or dividing by negatives.

## Compound Inequalities

two inequality statements linked together either by **"and"** or **"or"**.

You can split a compound inequality into two and solve both, or solve as is:

`7 < 3X + 4 < 10`

- **Split into two:** `7 < 3X + 4` and `3X +4 < 10`

### Compound And

- **Solution:** values that make **both** individual inequalities true
- Many **and** statements can be written as a 3-part statement:
  `X > 0 and x < 5` -> `0 < x < 5`
- Solve three-part statements by applying the properties of inequality to all
  three parts

### Compound Or

- **Solution:** values that make either of the individual inequalities true
- **Or** statements cannot be written as a single statement

# Exponents and Polynomials

## Exponential Notation

Exponential notation has a **Base** and an **Exponent**.

- The base is the number or variable, and the exponent is the exponent.

Any number _(other than zero)_ raised to the power of **0** is one.

### Negative Exponents

Any number with a negative exponent is the reciprocal of the number with a
positive exponent.

![](assets/negative_exponential_notation.png)

- With positive exponents, you multiply by the base.
- With negative exponents, you divide by the base (as long as it isn't zero).
    - Take the reciprocal and then attach the positive exponent to it.

## Simplify by Using the Product, Quotient, and Power Rules

### Multiplication - The Product Rule for Exponents

![](assets/exponential_notation_mulitplication.png)

- When multiplying variables in exponential notation, as long as they have the
  same base, you can add the exponents.

### Division - The Quotient Rule for Exponents

![](assets/exponential_notation_division.png)

- When dividing variables in exponential notation, as long as they have the
  same base, you can subtract the exponents.

### The Power Rule For Exponents

![](assets/exponential_notation_power.png)

- To simplify a power of a power, you multiply the exponents, keeping the same
  base

## Products and Quotients Raised to Powers

![](assets/exponent_multiplication.png)

### A Product Raised to a Power

**(ab)<sup>x</sup> = a<sup>x</sup> * b<sup>x</sup>**

- **(3x)<sup>3</sup> = 3<sup>3</sup> * x<sup>3</sup> = 27x<sup>3</sup>**
- When multiplying, the quotient applies to all values in the parenthesis.

### A Quotient Raised to a Power

**(<sup>x</sup>/<sub>y</sub>)<sup>3</sup> = (<sup>x</sup>/<sub>y</sub>)
(<sup>x</sup>/<sub>y</sub>)(<sup>x</sup>/<sub>y</sub>) = <sup>x<sup>3</sup></sup>
/<sub>y<sup>3</sup></sub>**

- When dividing, you apply it both the numerator and the denominator

## Scientific Notation

**Scientific Notation** is a way to write very big or very small numbers so that
they're easy to read.

Scientific notation consists of two parts:

- **_a_ * 10<sup>n</sup>**
    - `a` must be greater than or equal to 1, but less than 10
      - `1 <= a < 10`
    - No fractions or decimals

**The exponent counts how many times the decimal moves left or right, not the
amount of zero's.**

- **For Positive Exponents:** If you have a number such as **5.55<sup>10</sup>**,
  then there will be `exponent - 2` zero's after it: **55,500,000,000**
- **For Negative Exponents:** If you have a number such as 
  **5.55<sup>-10</sup>**, then there will be `exponent - 1` zero's before it: 
  **.000000000555**


### Examples

  - **5.28 * 10<sup>2</sup> = 528**
  - **3 * 10<sup>-3</sup> = .003**

### Solving Without Rewriting

1. **(4.5 x 10<sup>5</sup>) * (5.28 * 10<sup>-7</sup>)**
2. **(4.5 * 5.28)(10<sup>5</sup> * 10<sup>-7</sup>)**
3. **23.76**

If the number is higher than 10, move the decimal over and increase/decrease the
exponent to account for it.

## Introduction to Single Variable Polynomials

**15x<sup>3</sup>**

- **15** is the co-efficient
- **x** is the variable
- **<sup>3</sup>** is the exponent
- The entire thing is the **term**

Different Types:

- **15x:** Monomial - One term
- **15x + 12h:** Binomial - Two terms
- **15x + 12h + 10x:** Polynomial - A monomial or sum of monomials

Polynomial terms cannot have:

- Negative exponents
- Fraction exponents
- Variables in the denominator

## Adding Polynomials

1. Combine like-terms (terms that have the same variables with the same 
  exponents)
   - Add the co-efficients and keep the variables the same

### Example

A rectangular picture frame has a length of  inches and a width of  inches. 
Find the perimeter of the picture frame in inches.

1. Add the lengths and widths: 
   `(3a + 5) + (a + 2) + (3a + 5) + (a + 2)`
2. Regroup using the commutative and associative properties:
   `(3a + 3a + a + a) + (5 + 5 + 2 + 2)`
3. Combine like terms to simplify: `8a + 14`

## Multiplying Polynomials

![](assets/properties.png)

It helps to **FOIL** when multiplying polynomials.

- **F** irst
- **O** uter
- **I** Inner
- **L** Last

**(a + b)(c + d) = ac + ad + bc + bd**

![](assets/polynomial_multiplication.png)


## Multiplying Special Cases

There are three special cases:

1. Square of a Sum
2. Square of a Difference
3. Product of a Sum and a Difference

![](assets/three_special_cases.png)

1. **(a + b)<sup>2</sup> = (a + b)(a + b) = <u>a<sup>2</sup> + 2ab + 
   b<sup>2</sup></u>**
2. **(a - b)<sup>2</sup> = (a - b)(a - b) = <u>a<sup>2</sup> - 2ab + 
   b<sup>2</sup></u>**
3. **(a+b)(a - b) = a<sup>2</sup> - ab + ab - b<sup>2</sup> = 
   <u>a<sup>2</sup> - b<sup>2</sup></u>**

These special cases are useful, because the final answers above will always be 
a formula you can quickly apply to get the answers.

- The sign is not taken into account as part of either **a** or **b**.

## Dividing Monomials

1. Divide the coefficients
2. Divide the variables

![](assets/dividing_monomials.png)

- The monomials are rewritten from negative exponents to fractions (the 
  reciprocal)

## Simplifying and Evaluating Polynomials with More than One Term