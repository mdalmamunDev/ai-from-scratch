# from dataset_analyzer import DatasetAnalyzer
# from exceptions import DatasetError

# try:

#     analyzer = DatasetAnalyzer(
#         [10, 25, 15, 40, 30, 20, -5]
#     )

#     print(analyzer.get_basic_stats())

#     print("Even:", analyzer.get_even_numbers())

#     print("Odd:", analyzer.get_odd_numbers())

#     print("Positive:", analyzer.get_positive_numbers())

#     print("Negative:", analyzer.get_negative_numbers())

#     print("Greater than 20:",
#           analyzer.filter_greater_than(20))

#     print("Less than 20:",
#           analyzer.filter_less_than(20))

#     print("Between 10 and 30:",
#           analyzer.filter_between(10, 30))

#     print("Top 3:",
#           analyzer.get_top(3))

#     print("Bottom 3:",
#           analyzer.get_bottom(3))

# except DatasetError as error:

#     print(f"Error: {error}")


from cli import DatasetCLI
cli = DatasetCLI()
cli.run()