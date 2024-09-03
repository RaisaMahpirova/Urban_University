def correct_sender(sender):
    is_correct = True
    if "@" not in sender:
        is_correct = False
        return is_correct
    elif ".com" not in sender and ".ru" not in sender and ".net" not in sender:
        is_correct = False
        return is_correct

    return is_correct


def correct_recipient(recipient):
    is_correct = True
    if "@" not in recipient:
        is_correct = False
        return is_correct
    if ".com" not in recipient and ".ru" not in recipient and ".net" not in recipient:
        is_correct = False
        return is_correct
    return is_correct


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if not correct_sender(sender) or not correct_recipient(recipient):
        print("Невозможно отправить письмо с адреса ", sender, "на адрес ", recipient)
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса ", sender, "на адрес ", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender, "на адрес ", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
