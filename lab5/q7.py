import re

pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

sample = '''Hello, you can contact us at support@example.com for any queries.
For sales, reach out to sales-department@shop-now.com. 
Alternatively, you can email john.doe@university.edu or jane_doe123@mail.org.
Don't forget to also check with hr@company123.io.'''

result = list(re.findall(pattern,sample))

print("all emails found in the text:",result)
