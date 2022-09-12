from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'отправлена письмо',
        'ВЫ УСПЕШНО ПРОШЛИ РЕГИСТРАЦИЮ'
        'Благодарим Вас за проявленный интерес ',
        'testweb23062000@gmail.com',
        [user_email],
        fail_silently=False,
    )