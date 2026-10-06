class DatasetError(Exception):
  """Base exception for dataset-related errors."""
  pass


class InvalidDatasetError(DatasetError):
  """Raised when the dataset is invalid."""
  pass


class EmptyDatasetError(DatasetError):
  """Raised when the dataset is empty."""
  pass


class InvalidValueError(DatasetError):
  """Raised when an invalid value is provided."""
  pass