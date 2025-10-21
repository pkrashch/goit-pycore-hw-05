import sys
from pathlib import Path
from typing import Callable

def parse_log_line(line: str) -> dict:
    parts = line.split() 
    # parts[0]=date, parts[1]=time, parts[2]=level, *rest=message
    date, time, level, *message_parts = parts
    #join message parts back to string
    message = " ".join(message_parts)
    #creation of dictionary
    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message
    }

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as fh:
            for line in fh:
                cleaned_line = line.strip()
                if not cleaned_line: #for empty lines
                    continue
                logs.append(parse_log_line(cleaned_line))
    except (FileNotFoundError, IOError):
        return []
    
def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: dict) -> None:
    #table's header
    print(f"{'Рівень логування':<20}|{'Кількість':<10}")
    print("-" * 20 + "|" + "-" * 10)
    #display of formatted results
    for level, count in counts.items():
        print(f"{level:<20}|{count:<10}")

def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = [log for log in logs if  log["level"] == level]
    return filtered_logs

def main():
    # validation of number of arguments (expected 2 or 3)
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Error: Incorrect amount of arguments.")
        sys.exit(1)

    file_path = sys.argv[1] 
    target_path = Path(file_path)
    # check if file exists and whether it is file.
    if not target_path.exists() or not target_path.is_file():
        print(f"Error: Path '{file_path}' is either invalid or is not a file.")
        sys.exit(1)
    #load logs
    logs = load_logs(file_path)
    # general statistics
    log_counts = count_logs_by_level(logs)
    print("\nLogging level | Amount")
    print("-----------------|----------")
    display_log_counts(log_counts) #show the table

    # work with non-mandatory argument
    if len(sys.argv) == 3:
        filter_level = sys.argv[2].upper() 
        filtered_logs = filter_logs_by_level(logs, filter_level)
        print(f"\nDetailed logs for level '{filter_level}':")
        #showing filtered entries
        for log in filtered_logs:
            # Format: 2024-01-22 09:00:45 - Database connection failed.
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()