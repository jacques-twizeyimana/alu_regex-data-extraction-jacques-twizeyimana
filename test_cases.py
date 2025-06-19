from regex_extractors import (
    extract_emails,
    extract_urls,
    extract_phone_numbers,
    extract_credit_cards,
    extract_time,
    extract_html_tags,
    extract_hashtags,
    extract_currency,
)

sample_text = """
Contact us via email: twizojacques@gmail.com, j.twizeyima@alustudent.com.
Visit our site: https://www.example.com or https://sub.example.org/page.
Call now: (123) 456-7890, 123-456-7890 or 123.456.7890.
Use this card: 1234-5678-9012-3456 or 1234 5678 9012 3456.
Event starts at 14:30 and ends at 2:30 PM.
Here is the HTML: <div class="box"><img src="image.jpg" alt="pic"><p>Text</p></div>
Trending hashtags: #RegexRocks #ThisIsAHashtag #2025
We received $19.99, then $1,234.56 as payment.
"""

print("Emails:", extract_emails(sample_text))
print("URLs:", extract_urls(sample_text))
print("Phone Numbers:", extract_phone_numbers(sample_text))
print("Credit Cards:", extract_credit_cards(sample_text))
print("Time Formats:", extract_time(sample_text))
print("HTML Tags:", extract_html_tags(sample_text))
print("Hashtags:", extract_hashtags(sample_text))
print("Currency Amounts:", extract_currency(sample_text))
