# Day 18 Challenge: Use enumerate to loop with index
languages = ["Python", "SQL", "Power BI", "Excel"]

for index, lang in enumerate(languages, start=1):
    print(f"{index}. {lang}")
