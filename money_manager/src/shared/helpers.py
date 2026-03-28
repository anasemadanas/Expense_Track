from datetime import datetime

def format_date(date_obj):
    return date_obj.strftime("%Y-%m-%d %H:%M:%S")

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")