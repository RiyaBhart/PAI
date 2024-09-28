import re

def extractemails(text):
   
    emailpattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    
   
    emails = re.findall(emailpattern, text)
    
    return emails


text = """
Dear Team,

Please find the details below:

- For technical support, reach out to tech.support@mycompany.com.
- Sales inquiries can be sent to sales@ecommerce-world.com.
- Contact our HR team at hr-department@mycompany.co.uk for any recruitment-related queries.
- For feedback, email feedback123@feedbackservice.net.
- If you're a student, contact us at student.services@university.edu.
- Reach out to our CEO directly at ceo.johndoe@mycompany.com for urgent matters.
- In case of issues with billing, email billing@service-provider.org.
- For collaboration proposals, feel free to contact partner.connect@biz-partners.io.

Thank you for your cooperation.

Best regards,
The MyCompany Team

"""

emailaddresses = extractemails(text)
print("Extracted email addresses : ", emailaddresses)
