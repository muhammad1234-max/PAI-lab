import re

# Sample text containing dates in different formats
text = """
The event will happen on 12/09/2023. Another important date is 2023-09-12.
We also celebrate on Sep 12, 2023, and another date format is 09-12-2023.
Remember, important deadlines are on 12th Sept, 2023.
"""
#regex for all formats of dates
date_pattern = r'(\d{2}/\d{2}/\d{4})|(\d{4}-\d{2}-\d{2})|([A-Za-z]{3,9} \d{1,2}, \d{4})'

# Find all matches of dates in the text
dates = re.findall(date_pattern, text)

#fiters out the empty strings in the tuple
extracted_dates = [date for match in dates for date in match if date]

for date in extracted_dates:
    print(date)
