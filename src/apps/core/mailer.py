
from django.core.mail import send_mail


def send_email(mail_data):
    print('!!! mail data', mail_data)
    subject = "You've got a new match!!!"
    receiver = mail_data.get("mail_to")
    message = f"Hello {mail_data['full_name_to']}! You matched with {mail_data['match_full_name']}. "
    prefix = "His" if mail_data.get("match_gender", "m") == "m" else "Her"
    message += f"{prefix} email: {mail_data['match_email']}"
    send_mail(subject, message, 'sender@example.com', [receiver, ])
