# DATA 4000: Python with AI

Python exercises for DATA 4000 in the School of Business. The exercises build progressively from variables and input/output to functions and conditional logic.

## Concepts Covered

- Variables: `str`, `int`, and `float`
- Input and output
- String methods such as `strip`, `lower`, `title`, and `split`
- Arithmetic operations and modulo
- Functions with parameters, defaults, and return values
- Conditionals: `if`/`elif`/`else`, logical operators, and ternary expressions
- `match`/`case` statements

The exercises do not require loops, lists, dictionaries, file I/O, exceptions, or other advanced topics.

## Student Instructions

- Use Python 3.x in VS Code.
- Create a new Python file for each exercise, such as `exercise1_profit_calculator.py`.
- Test each program thoroughly with the sample inputs and additional inputs.
- Use AI tools such as Grok or ChatGPT for brainstorming, debugging, or explanations, while ensuring the final code reflects your own understanding and implementation.
- Push your solutions to a public GitHub repository and submit the repository link to Blackboard by the deadline.
- Collaborate ethically: discuss ideas, but submit individual code.
- Aim to complete each exercise in 20-60 minutes.

---

## Exercise Overview

### Exercise 1: Profit Margin Calculator
* **File:** `exercise1_profit_calculator.py`
* **Description:** Calculates profit and profit margin percentage based on user-inputted revenue and cost.
* **Assumptions:** Revenue must be greater than zero to calculate margin; valid floating-point numbers are entered.

### Exercise 2: Credit Score Evaluator
* **File:** `exercise2_credit_score.py`
* **Description:** Evaluates a credit score (300–850 range) using chained conditionals to determine loan approval tier and interest rate status.
* **Assumptions:** Credit scores outside 300–850 are flagged as invalid.

### Exercise 3: Customer Greeting Formatter
* **File:** `exercise3_greeting_formatter.py`
* **Description:** Cleans and titles user input names, extracting the first name to construct a personalized greeting.
* **Assumptions:** Empty inputs default to a generic "Valued Customer" greeting.

### Exercise 4: Tax Bracket Determiner
* **File:** `exercise4_tax_bracket.py`
* **Description:** Categorizes income into low, medium, or high tax brackets using functions and returns formatted estimated tax owed.
* **Assumptions:** Negative income is treated as invalid.

### Exercise 5: Product Category Matcher
* **File:** `exercise5_product_category_matcher`
* **Description:** Uses Python's `match-case` statements with pattern matching to categorize retail products by profit margin.
* **Assumptions:** Input strings are stripped and lowercased to ensure case-insensitive matching.

---

## Sample Run Outputs

```text
What's the revenue? 5000.0
What's the cost? 3500.0
Profit: $1,500.00 | Margin: 30.00%