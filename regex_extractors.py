import re

def extract_emails(text):
    """Extracts email addresses from the input text."""
    return re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)

def extract_urls(text):
    """Extracts full URLs with or without www or protocol."""
    return re.findall(
        r'\b(?:https?://|www\.)[^\s<>"]+',
        text
    )

def extract_phone_numbers(text):
    """Extracts phone numbers in various common formats."""
    return re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)

def extract_credit_cards(text):
    """Extracts credit card numbers in 1234-5678-9012-3456 or 1234 5678 9012 3456 format."""
    return re.findall(r'\b(?:\d{4}[-\s]?){3}\d{4}\b', text)

def extract_time(text):
    """Extracts time in 24-hour and 12-hour format."""
    return re.findall(
        r'\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9]\b|\b(?:1[0-2]|0?[1-9]):[0-5][0-9]\s?(?:AM|PM|am|pm)\b',
        text
    )

def extract_html_tags(text):
    """Extracts HTML tags like <p>, <div>, <img src='...'>, etc."""
    return re.findall(r'<[^>]+>', text)

def extract_hashtags(text):
    """Extracts hashtags like #Example or #ThisIsAHashtag."""
    return re.findall(r'#\w+', text)
    
def extract_currency(text):
    """
    Extracts currency amounts like $1,000.00, -€500, RWF 1000, etc.
    Supports symbols: $, €, £, ₦, ¥, RWF, USD, etc.
    """
    return re.findall(
        r'\b(?:-?\s?(?:\$|€|£|₦|¥|RWF|USD|EUR|GBP|KES|ZAR)\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\b-?\s?(?:\$|€|£|₦|¥|RWF|USD|EUR|GBP|KES|ZAR)\s?\d+(?:\.\d{2})?)',
        text
    )
