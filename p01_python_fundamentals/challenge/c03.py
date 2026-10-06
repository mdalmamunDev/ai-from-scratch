"""
Hard: Implement a Reusable DatasetAnalyzer Class

Build a reusable Python class called DatasetAnalyzer that works with a simple list of numbers.

Requirements:

1. Create a DatasetAnalyzer class.

2. The class should accept a list of numbers when creating an object.

Example:

numbers = [10, 25, 15, 40, 30, 20]

analyzer = DatasetAnalyzer(numbers)

3. Implement a method to calculate:
   - Total
   - Average
   - Minimum
   - Maximum
   - Range
   - Number of values

4. Implement a method to find:
   - Even numbers
   - Odd numbers
   - Positive numbers
   - Negative numbers

5. Implement a method to filter numbers:
   - Greater than a given value
   - Less than a given value
   - Between two values

6. Implement a method to return the top N largest numbers.

7. Implement a method to return the bottom N smallest numbers.

8. Implement a method to remove duplicate values.

9. Implement a method to display a complete statistics report.

10. The original list should not be modified directly.

11. Handle an empty dataset properly.

Example:

numbers = [10, 20, 20, 5, 30, -10, 15, 40, 5]

Expected report structure:

===== Dataset Report =====

Count: ...
Total: ...
Average: ...
Minimum: ...
Maximum: ...
Range: ...

Even Numbers: ...
Odd Numbers: ...
Positive Numbers: ...
Negative Numbers: ...

Unique Values: ...

Top 3: ...
Bottom 3: ...

Constraints:

- Use Python classes and objects.
- Use instance methods.
- Use lists.
- Use loops and conditions.
- Do not use pandas.
- Do not use external libraries.

Challenge:

Allow the class to accept a new dataset after the object has already been created.

Extra Challenge:

Add a method that returns all statistics as a dictionary instead of only printing them.
"""


class DatasetAnalyzer:
  dataset = []
  def __init__(self, dataset):
    if not isinstance(dataset, list):
        raise ValueError("The dataset cannot be empty!")
    self.dataset = dataset
  
  def get_basic_stats(self):
    total = sum(self.dataset)
    length = len(self.dataset)
    avg = total/length
    minimum = min(self.dataset)
    maximum = max(self.dataset)
    print(f'Total: {total}, Length: {length}, Average: {avg}, Minimum: {minimum}, Maximum {maximum}')
  
  def get_even_numbers(self):
    return [num for num in self.dataset if num % 2 == 0]
  def get_odd_numbers(self):
    return [num for num in self.dataset if num % 2 == 1]
  
  def get_positive_numbers(self):
    return [num for num in self.dataset if num >= 0]
  def get_negative_numbers(self):
    return [num for num in self.dataset if num < 0]
  
  def filter_greater_than(self, value):
    return [num for num in self.dataset if num > value]
  def filter_less_than(self, value):
    return [num for num in self.dataset if num < value]
  def filter_between(self, value1, value2):
    return [num for num in self.dataset if num > value1 and num < value2]
  
    
  def get_top(self, N):
        """Returns the top N largest numbers without modifying the original list."""
        # sorted() returns a new list, [::-1] reverses it to descending order
        return sorted(self.dataset, reverse=True)[:N]
        
  def get_bottom(self, N):
      """Returns the bottom N smallest numbers without modifying the original list."""
      return sorted(self.dataset)[:N]
      
  def remove_duplicates(self):
      """Returns unique values while preserving their original layout order."""
      unique_list = []
      for num in self.dataset:
          if num not in unique_list:
              unique_list.append(num)
      return unique_list


analyzer = DatasetAnalyzer([10, 25, 15, 40, 30, 20])
analyzer.get_basic_stats()

print("get_even_numbers: ", analyzer.get_even_numbers())
print("get_odd_numbers: ", analyzer.get_odd_numbers())

print("get_positive_numbers: ", analyzer.get_positive_numbers())
print("get_negative_numbers: ", analyzer.get_negative_numbers())

print("filter_greater_than: ", analyzer.filter_greater_than(10))
print("filter_less_than: ", analyzer.filter_less_than(15))
print("filter_between: ", analyzer.filter_between(10, 25))