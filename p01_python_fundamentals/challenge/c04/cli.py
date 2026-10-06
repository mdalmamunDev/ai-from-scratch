from dataset_analyzer import DatasetAnalyzer
from exceptions import DatasetError


class DatasetCLI:

  def __init__(self):
    self.analyzer = None

  def show_menu(self):
    print("\n===== Dataset Analyzer =====")
    print("1. Enter dataset")
    print("2. Show statistics")
    print("3. Show even numbers")
    print("4. Show odd numbers")
    print("5. Show positive numbers")
    print("6. Show negative numbers")
    print("7. Filter numbers")
    print("8. Show top N")
    print("9. Show bottom N")
    print("10. Remove duplicates")
    print("11. Exit")

  def run(self):
    
    while True:
      self.show_menu()
      choice = input("\nChoose an option: ").strip()

      try:
        if choice == "1":
          self.enter_dataset()

        elif choice == "2":
          self.show_statistics()

        elif choice == "3":
          self.show_even_numbers()

        elif choice == "4":
          self.show_odd_numbers()

        elif choice == "5":
          self.show_positive_numbers()

        elif choice == "6":
          self.show_negative_numbers()

        elif choice == "7":
          self.filter_numbers()

        elif choice == "8":
          self.show_top()

        elif choice == "9":
          self.show_bottom()

        elif choice == "10":
          self.remove_duplicates()

        elif choice == "11":
          print("\nGoodbye!")
          break

        else:
          print("\nInvalid option. Please choose 1-11.")

      except DatasetError as error:
        print(f"\nError: {error}")

      except ValueError as error:
        print(f"\nInvalid input: {error}")

  def enter_dataset(self):

    raw_input = input(
      "\nEnter numbers separated by spaces: "
    ).strip()

    if not raw_input:
      raise ValueError("Please enter at least one number.")

    try:
      numbers = [
        float(value)
        for value in raw_input.split()
      ]
    except ValueError:
      raise ValueError(
        "Dataset can only contain numbers."
      )

    self.analyzer = DatasetAnalyzer(numbers)

    print("\nDataset loaded successfully.")

  def check_analyzer(self):

    if self.analyzer is None:
      raise DatasetError(
        "No dataset available. Please enter a dataset first."
      )

  def show_statistics(self):

    self.check_analyzer()

    stats = self.analyzer.get_basic_stats()

    print("\n===== Statistics =====")
    print(f"Count: {stats['length']}")
    print(f"Total: {stats['total']}")
    print(f"Average: {stats['average']:.2f}")
    print(f"Minimum: {stats['minimum']}")
    print(f"Maximum: {stats['maximum']}")

  def show_even_numbers(self):

    self.check_analyzer()

    print(
      "\nEven numbers:",
      self.analyzer.get_even_numbers()
    )

  def show_odd_numbers(self):

    self.check_analyzer()

    print(
      "\nOdd numbers:",
      self.analyzer.get_odd_numbers()
    )

  def show_positive_numbers(self):

    self.check_analyzer()

    print(
      "\nPositive numbers:",
      self.analyzer.get_positive_numbers()
    )

  def show_negative_numbers(self):

    self.check_analyzer()

    print(
      "\nNegative numbers:",
      self.analyzer.get_negative_numbers()
    )

  def filter_numbers(self):

    self.check_analyzer()

    print("\n===== Filter =====")
    print("1. Greater than")
    print("2. Less than")
    print("3. Between")

    choice = input("Choose filter: ").strip()

    if choice == "1":

      value = float(
        input("Enter value: ")
      )

      result = self.analyzer.filter_greater_than(value)

    elif choice == "2":

      value = float(
        input("Enter value: ")
      )

      result = self.analyzer.filter_less_than(value)

    elif choice == "3":

      value1 = float(
        input("Enter minimum value: ")
      )

      value2 = float(
        input("Enter maximum value: ")
      )

      result = self.analyzer.filter_between(
        value1,
        value2
      )

    else:
      raise ValueError("Invalid filter option.")

    print("\nResult:", result)

  def show_top(self):

    self.check_analyzer()

    n = int(
      input("How many top numbers? ")
    )

    result = self.analyzer.get_top(n)

    print("\nTop numbers:", result)

  def show_bottom(self):

    self.check_analyzer()

    n = int(
      input("How many bottom numbers? ")
    )

    result = self.analyzer.get_bottom(n)

    print("\nBottom numbers:", result)

  def remove_duplicates(self):

    self.check_analyzer()

    result = self.analyzer.remove_duplicates()

    print("\nUnique values:", result)