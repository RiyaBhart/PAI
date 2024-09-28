import re
def extractdate(text):
    datepatt = r'\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b|\b\w+ \d{1,2}, \d{4}\b'
    extractdate=re.findall(datepatt,text)
    return extractdate

text = """Dear All,

We would like to remind you of the following important dates for the upcoming events:

The project submission deadline is 15/10/2023. Please make sure all your documents are uploaded by that date.
The next team meeting is scheduled for October 18, 2023. This will be a virtual meeting, and the invite will be sent soon.
The annual company retreat will take place from November 1st, 2023 to November 3rd, 2023. Please mark your calendars accordingly.
On 01-12-2023, we will be hosting the year-end wrap-up meeting.
The next quarter starts on January 2, 2024, and all team members are expected to submit their reports by 31st December 2023.
Let us know if you need any further information.

Best regards,
The Team"""

print("Extracted Dates : ",extractdate(text))
