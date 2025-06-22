# ThyLang
ThyLang is a interpreted and case sensitive programming language inspired by Shakespearean/old English. This language allows you to code in a way that feels poetic, ancient, and deep. 

# Important Notice/Warning
ThyLang is currently in beta and has not been thoroughly tested! You may encounter bugs, unexpected behavior, or incomplete features while using this language. 
This project was built primarily for fun and creativity rather than functionality. 
This documentation assumes you already have an understanding or programming concepts likle loops, data types, variables, etc. This is a documentation, not a programming tutorial.
Please keep this in mind when experimenting with ThyLang!

# Documentation

## Table of Contents
- [Getting Started](#getting-started)
- [Data Types](#data-types)
- [Variables](#variables)
- [Operators](#operators)
- [Control Flow](#control-flow)
- [Functions](#functions)
- [Built-in Functions](#built-in-functions)
- [Lists](#lists)
- [Comments](#comments)
- [Error Messages](#error-messages)
- [Examples](#examples)
- [Contributing](#contributing)



## Getting Started

To run ThyLang, execute `Main.py` and you'll see the following interactive prompt in your terminal:

```
ThyLang >>> 
```

Type your ThyLang code and press Enter to execute the code. You can type `cease` to exit the interpreter.

## Data Types

ThyLang supports several fundamental data types such as:

### Numbers
- **Integers**: `42`, `-17`, `0`
- **Floats**: `3.14`, `-2.5`, `0.0`

### Strings
- Enclosed in double quotes: `"Hello, fair maiden!"`
- Supported escape characters:
  - `\n` - newline
  - `\t` - tab
  - `\\` - backslash

### Lists
- Ordered collections: `[1, 2, 3]`
- Lists can contain mixed types: `[42, "hello", 3.14]`
- ThyLang also supports nested lists like: `[[1, 2], [3, 4]]`

### Booleans
- `sooth` - true (1)
- `falsehood` - false (0)

## Variables

### Variable Assignment
Use the `hath` keyword to assign values to variables:

```thylang
hath x = 42
hath name = "Sir Lancelot"
hath scores = [10, 20, 30]
```

### Variable Access
Simply use the variable name:

```thylang
hath x = 10
hath y = x + 5
printeth(y)  # Outputs: 15
```

## Operators

### Arithmetic Operators
- `+` - Addition
- `-` - Subtraction
- `*` - Multiplication
- `/` - Division
- `//` - Floor division
- `^` - Exponentiation

### Comparison Operators
- `==` - Equal to
- `!=` - Not equal to
- `>` - Greater than
- `<` - Less than
- `>=` - Greater than or equal to
- `<=` - Less than or equal to

### Logical Operators
- `and` - Logical AND
- `or` - Logical OR
- `not` - Logical NOT

### Unary Operators
- `+` - Positive (unary plus)
- `-` - Negative (unary minus)

## Control Flow

### Conditional Statements (If-Else)
The syntax for a if-else statement in ThyLang is as follows:
```thylang
shouldst condition so expression
```

For else-if and else:

```thylang
shouldst x > 10 so "Large number" mayhaps x > 5 so "Medium number" naughtwise "Small number"
```
Keep in mind that as of now, ThyLang does not support multi line statements and is case sensitive (shouldst ≠ Shouldst).

### While Loops
The syntax for a while loop in ThyLang is as follows:
```thylang
whilst condition do (expression)
```
Your expressions can be separated by using commas ","

Example:
```thylang
hath i = 0 (you have to declare all variables, including your iterator before the loop)
whilst i < 5 do ( hath i = i + 1, printeth(i))
```

### For Loops

```thylang
each iterator amongst start_value to end_value do (expression)
```

Example:
```thylang
each i amongst 1 to 5 do (printeth(i))
```

Note: For loops automatically handle ascending and descending ranges, for loops also support mutiple expression each separated by commas.

## Functions
WARNING - As of now, functions can not accept more than one expression, but can accept more than one parameters separated by commas!

### Function Definition

```thylang
craft function_name(parameter1, parameter2) : expression
```


Example:
```thylang
craft add_numbers(a, b) : a + b
craft multiply_lists(list, num): list * num
craft greet(name): printeth("Hello, " + name)
```

### Function Calls

```thylang
function_name(argument1, argument2)
```

Example:
```thylang
hath result = add_numbers(5, 3)
multiply_lists([1, 2, 3], 8)
greet("Arthur")
```

## Built-in Functions

ThyLang provides several built-in functions which are listed as follows:

### Input/Output Functions
- `printeth(value)` - Print a value to the terminal
- `recieve_sentence()` - Get string input from user
- `recieve_number()` - Get numeric input from user

### Type Checking Functions
These functions like any other in ThyLang return 1 if true and 0 if false
- `beith_whole(value)` - Check if value is a number 
- `beith_tongue(value)` - Check if value is a string
- `beith_listeth(value)` - Check if value is a list

### List Manipulation Functions
- `includeth(list, value)` - Append value to list
- `banish(list, index)` - Remove and return element at index
- `length(value)` - Get length of string or list

### Examples of Built-in Functions

```thylang
printeth("Enter thy name:")
hath name = recieve_sentence()
printeth("Greetings, " + name + "!")

hath numbers = [1, 2, 3]
includeth(numbers, 4)  # numbers becomes [1, 2, 3, 4]
hath removed = banish(numbers, 0)  # removes first element
printeth(length(numbers))  # prints length
```

## Lists

### Creating Lists
```thylang
hath empty_list = []
hath numbers = [1, 2, 3, 4, 5]
hath mixed = [42, "hello", 3.14, sooth]
```

### List Operations
NOTE - As of now, ThyLang does not support list index accessing, so you can not do something like multiplying the 0th element (or any other element) of a list by any number. You can use the banish function to pop an index from a list which is 0 indexed.

Lists in ThyLang support arithmetic operations that apply to all elements of the list:

```thylang
hath numbers = [1, 2, 3]
hath doubled = numbers * 2    # [2, 4, 6]
hath increased = numbers + 1  # [2, 3, 4]
```

### List Functions
```thylang
hath fruits = ["apple", "banana"]
includeth(fruits, "cherry")  # Add element
hath first = banish(fruits, 0)  # Remove first element
hath count = length(fruits)  # Get list length
```

## Comments

Use `#` to create comments. Everything after `#` on a line is ignored:

```thylang
# This is a comment
hath x = 42  # This is also a comment
```

## Error Messages

ThyLang provides error messages in classical English style, while these messages might be cryptic to understand for some users, please remember that this language is built more from a fun perspective rather than a functionality one:

- **Undefined Variable**: "Verily, no variable of 'name' is inscribed in these sacred scripts."
- **Division by Zero**: "Thou dared divide by naught."
- **Invalid Operation**: "Hark! Thou hast attempted an operation most grievous and forbidden!"
- **Illegal Character**: "Expected '=', but thy script delivereth none."

## Examples

### Basic Calculator
```thylang
printeth("Enter first number:")
hath a = recieve_number()
printeth("Enter second number:")
hath b = recieve_number()

printeth("Sum: " + (a + b))
printeth("Product: " + (a * b))
```

### Factorial Function
```thylang
craft factorial(n) :  shouldst n <= 1 so 1 naughtwise n * factorial(n - 1)
    
hath result = factorial(5)

printeth("5! = " + result)
```

### List Processing
```thylang
hath numbers = [1, 2, 3, 4, 5]
hath sum = 0
hath i = 0

each i amongst 0 to length(numbers) - 1 do (hath sum = sum + banish(numbers, 0))

printeth("Sum: " + sum)
```

### Guessing Game
```thylang
hath secret = 42
hath guess = 0

whilst guess != secret do (printeth("Guess the number:"),  hath guess = recieve_number(), shouldst guess > secret so printeth("Too high!") mayhaps guess < secret so printeth("Too low!") naughtwise printeth("Thou hast guessed correctly!"))
```

### String Manipulation
```thylang
hath greeting = "Hello"
hath name = "World"
hath message = greeting + ", " + name + "!"

printeth(message)
printeth("Message length: " + length(message))

shouldst beith_tongue(message) so printeth("'Tis a string indeed!")
```

## Contributing
I appreciate anyone who takes the time to contribute to ThyLang! Whether you're fixing bugs, adding new features, improving documentation, or just experimenting with the language, your involvement means a lot.

If you encounter any bugs or have ideas for improvements, please feel free to:

Submit bug reports
Create pull requests with fixes or enhancements
Suggest new features or language constructs
Improve the documentation
Share your ThyLang projects!

Remember, ThyLang is a project built for fun and creative expression, so don't hesitate to get creative with your contributions.
I hope you love the documentation as well as ThyLang!


