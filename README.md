bracebalance
============

A function to test the balance of braces in a string.

Braces being '{' and '}', balanced meaning every opening brace has a corresponding closing brace and vice versa.

If a string is unbalanced, output will be the 0-based index of the first unbalanced brace. Otherwise the output is -1.

## Usage

Import the function into your code:

`from first import balanced`

Run code with string and use output:

```
string = '{}{foo{}'
res = balanced(string)
if res == -1:
  print('balanced')
else:
  print('unbalanced on index ' + res)
```
