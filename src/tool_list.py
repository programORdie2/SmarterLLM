from tools.dates import get_current_data
from tools.dates import date_to_timestamp
from tools.dates import timestamp_to_date
from tools.dates import date_math
from tools.search import search
from tools.math import calculate


tools = [
    {
        "name": "calculate",
        "function": calculate,
        "description": "Evaluate a mathematical expression",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The mathematical expression to evaluate",
                }
            },
            "required": ["expression"],
        },
    },
    
    {
        "name": "search",
        "function": search,
        "description": "Search for anything on the internet",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The query to search for. If searching for a date or age, make sure to tell it.",
                }
            },
            "required": ["query"],
        },
    },
    
    {
        "name": "get_date",
        "function": get_current_data,
        "description": "Get the current date and time, in the format YYYY-MM-DD HH:MM",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    
    {
        "name": "date_to_timestamp",
        "function": date_to_timestamp,
        "description": "Convert a date string in the format YYYY-MM-DD HH:MM to a Unix timestamp",
        "parameters": {
            "type": "object",
            "properties": {
                "date": {
                    "type": "string",
                    "description": "The date string in the format YYYY-MM-DD HH:MM",
                }
            },
            "required": ["date"],
        },
    },
    
    {
        "name": "timestamp_to_date",
        "function": timestamp_to_date,
        "description": "Convert a Unix timestamp to a date string in the format YYYY-MM-DD HH:MM",
        "parameters": {
            "type": "object",
            "properties": {
                "timestamp": {
                    "type": "integer",
                    "description": "The Unix timestamp",
                }
            },
            "required": ["timestamp"],
        },
    },
    
    {
        "name": "date_math",
        "function": date_math,
        "description": "Perform mathematical operations on two dates",
        "parameters": {
            "type": "object",
            "properties": {
                "date1": {
                    "type": "string",
                    "description": "The first date in the format YYYY-MM-DD HH:MM",
                },
                "date2": {
                    "type": "string",
                    "description": "The second date in the format YYYY-MM-DD HH:MM",
                },
                "operation": {
                    "type": "string",
                    "enum": ["add", "subtract"],
                    "description": "The operation to perform, either 'add' or 'subtract'",
                }
            },
            "required": ["date1", "date2", "operation"],
        }
    }
]