## Python For Loop Exercises

### Q1. Print numbers from 1 to 10
```python
for i in range(1, 11):
    print(i)
```

### Q2. Print even numbers from 1 to 20
```python
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
```

### Q3. Multiplication table up to 10
```python
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

### Q4. Sum of numbers from 1 to n
```python
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum =", total)
```

### Q5. Print each character of a string
```python
text = input("Enter a string: ")
for char in text:
    print(char)
```

### Q6. Square of each element in a list
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num ** 2)
```

### Q7. Print numbers from 10 down to 1
```python
for i in range(10, 0, -1):
    print(i)
```

### Q8. Count vowels in a string
```python
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)
```

### Q9. Create list of even numbers from 1 to 50
```python
even_numbers = []
for i in range(1, 51):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)
```

### Q10. Factorial of a number
```python
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)
```

### Q11. Print pattern
```
*
**
***
****
```
```python
for i in range(1, 5):
    print("*" * i)
```

### Q12. Sum of digits of a number
```python
num = input("Enter a number: ")
total = 0
for digit in num:
    total += int(digit)
print("Sum of digits =", total)
```

### Q13. Find largest number in a list
```python
numbers = [4, 17, 23, 1, 56, 34]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number:", largest)
```

### Q14. Print first 10 odd numbers
```python
for i in range(1, 20, 2):
    print(i)
```

### Q15. Take 5 numbers and print their sum
```python
total = 0
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    total += num
print("Sum =", total)
```

### Q16. Multiplication tables of numbers from 1 to 5
```python
for i in range(1, 6):
    print(f"\nMultiplication Table of {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
```

### Q17. New list with only positive numbers
```python
numbers = [-3, 7, -1, 0, 4, 9]
positive = []
for num in numbers:
    if num > 0:
        positive.append(num)
print("Positive numbers:", positive)
```

