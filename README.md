Repository Structure and Functionality (Solutions)
File	Function / Component	Description of Functionality
task_1_salary.py	total_salary(path)	Data Analysis: Reads developer salaries from a file and calculates the total and average salary, safely handling FileNotFoundError and division by zero.
task_2_cats.py	get_cats_info(path)	File Parsing: Converts structured data about cats (ID, name, age) from a text file into a list of dictionaries; includes robust error handling.
task_3_log_analyzer.py	main() / Handlers	Log Analysis CLI: Script accepts a path as an argument, displays logging level statistics, and supports filtering logs by level (using list comprehension).
task_4_assistant_bot.py	main() / Handlers	Console Assistant Bot: Implements a full CLI cycle with commands (add, change, phone, all). All handlers are protected by the universal @input_error decorator against ValueError, KeyError, and IndexError.
Execution Instructions for CLI Scripts
To run the interactive scripts (Tasks 3 and 4) from your terminal, use the following formats:

Task	Execution Format
Task 3 (Log Analyzer)	python task_3_log_analyzer.py /path/to/logfile.log [LEVEL]
**Task 4 (Assistant Bot)`	python task_4_assistant_bot.py