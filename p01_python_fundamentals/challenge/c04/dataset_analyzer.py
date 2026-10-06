from exceptions import (
  InvalidDatasetError,
  EmptyDatasetError,
  InvalidValueError
)


class DatasetAnalyzer:

  def __init__(self, dataset):
    # Dataset must be a list
    if not isinstance(dataset, list):
      raise InvalidDatasetError(
        "Dataset must be a list."
      )

    # Dataset cannot be empty
    if len(dataset) == 0:
      raise EmptyDatasetError(
        "Dataset cannot be empty."
      )

    # Every item must be a number
    for value in dataset:
      if not isinstance(value, (int, float)):
        raise InvalidDatasetError(
          f"Invalid dataset value: {value}"
        )

    self.dataset = dataset.copy()

  def get_basic_stats(self):

    if not self.dataset:
      raise EmptyDatasetError(
        "Cannot calculate statistics for an empty dataset."
      )

    total = sum(self.dataset)
    length = len(self.dataset)
    average = total / length
    minimum = min(self.dataset)
    maximum = max(self.dataset)

    return {
      "total": total,
      "length": length,
      "average": average,
      "minimum": minimum,
      "maximum": maximum
    }

  def get_even_numbers(self):

    return [
      num for num in self.dataset
      if num % 2 == 0
    ]

  def get_odd_numbers(self):

    return [
      num for num in self.dataset
      if num % 2 != 0
    ]

  def get_positive_numbers(self):

    return [
      num for num in self.dataset
      if num >= 0
    ]

  def get_negative_numbers(self):

    return [
      num for num in self.dataset
      if num < 0
    ]

  def filter_greater_than(self, value):

    if not isinstance(value, (int, float)):
      raise InvalidValueError(
        "Value must be a number."
      )

    return [
      num for num in self.dataset
      if num > value
    ]

  def filter_less_than(self, value):

    if not isinstance(value, (int, float)):
      raise InvalidValueError(
        "Value must be a number."
      )

    return [
      num for num in self.dataset
      if num < value
    ]

  def filter_between(self, value1, value2):

    if not isinstance(value1, (int, float)):
      raise InvalidValueError(
        "First value must be a number."
      )

    if not isinstance(value2, (int, float)):
      raise InvalidValueError(
        "Second value must be a number."
      )

    if value1 > value2:
      raise InvalidValueError(
        "First value cannot be greater than second value."
      )

    return [
      num for num in self.dataset
      if value1 <= num <= value2
    ]

  def get_top(self, n):

    if not isinstance(n, int):
      raise InvalidValueError(
        "N must be an integer."
      )

    if n <= 0:
      raise InvalidValueError(
        "N must be greater than 0."
      )

    return sorted(
      self.dataset,
      reverse=True
    )[:n]

  def get_bottom(self, n):

    if not isinstance(n, int):
      raise InvalidValueError(
        "N must be an integer."
      )

    if n <= 0:
      raise InvalidValueError(
        "N must be greater than 0."
      )

    return sorted(self.dataset)[:n]

  def remove_duplicates(self):

    return list(set(self.dataset))