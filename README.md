# GoIT Python Core - Home Work 05: Functional Programming and Decorators

## Project Overview 

This repository contains the solutions for the fifth block of homework assignments, focusing on **advanced Python concepts**: Closures, Generators, Memoization, Regular Expressions, CLI Architecture, and universal Exception Decorators.

---

## Repository Structure and Functionality 

| File | Function / Component | Description of Functionality |
| :--- | :--- | :--- |
| **`task_1_fibonacci.py`** | `caching_fibonacci()` | Implements a **closure** to create a memoized (cached) recursive function for calculating Fibonacci numbers. |
| **`task_2_generators.py`** | `generator_numbers()` / `sum_profit()` | Uses a **generator** and **regular expressions** (`re`) to efficiently extract and sum all float numbers from a given text string. |
| **`task_3_log_analyzer.py`** | `main()` / Handlers | **Log Analysis CLI:** Script accepts a path as an argument, displays logging level statistics, and supports **filtering logs by level**. |
| **`task_4_assistant_bot.py`** | `main()` / `@input_error` | **CLI Assistant Bot:** Implements a full CLI cycle with commands (`add`, `change`, `phone`, `all`). All handlers are protected by the universal **`@input_error` decorator** against `ValueError`, `KeyError`, and `IndexError`. |

---

## Execution Instructions
To run the command-line scripts (Tasks 3 and 4) from your terminal, use the following formats:

| Task | Execution Format |
| :--- | :--- |
| **Task 3 (Log Analyzer)** | `python task_3_log_analyzer.py /path/to/logfile.log [LEVEL]` |
| **Task 4 (Assistant Bot)`** | `python task_4_assistant_bot.py` |