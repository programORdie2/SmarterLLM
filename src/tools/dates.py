from datetime import datetime as DateTime

def get_current_data() -> str:
    return DateTime.now().strftime("%Y-%m-%d %H:%M")

def timestamp_to_date(timestamp: int) -> str:
    return DateTime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M")

def date_to_timestamp(date: str) -> int:
    return DateTime.strptime(date, "%Y-%m-%d %H:%M").timestamp()

def date_math(date1: str, date2: str, operation: str) -> str:
    date1 = date_to_timestamp(date1)
    date2 = date_to_timestamp(date2)
    if operation == "add" or operation == "sum" or operation == "+":
        return timestamp_to_date(date1 + date2)
    elif operation == "subtract" or operation == "sub" or operation == "-":
        return timestamp_to_date(date1 - date2)
    else:
        return None