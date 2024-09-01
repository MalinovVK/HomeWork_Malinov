def message():
    global message
    message = input("Введите сообщение которое хотите отправить: ")
    return message

def sender_email():
    sender = input("Введите свою почту: ")
    if (sender.endswith(".com") or sender.endswith("ru") or sender.endswith(".net") or sender.endswith("@")):
        return sender
    else:
        if not (sender.endswith(".com") or sender.endswith("ru") or sender.endswith(".net") or sender.endswith("@")):
            print("Некорректно введена почта отправителя")
            sender = str(input('Повторно введите почту: '))

def send_email(sender, *, recipient):
    a = 0
    while a == 0:
        if (recipient.endswith(".com") or recipient.endswith("ru") or recipient.endswith(".net") or recipient.endswith("@")) and recipient != sender:
            message()
            print('')
            print(f'Отправитель: {sender}')
            print(f'Получатель: {recipient}')
            print(f'Письмо: {message}')
            print(f'Письмо успешно отправлено')
            a = 1
        else:
            if not (recipient.endswith(".com") or recipient.endswith("ru") or recipient.endswith(".net") or recipient.endswith("@")):
                print("Некорректно введена почта получателя")
                recipient = str(input('Повторно введите почту: '))
            elif recipient == sender:
                print("Вы не можете самому себе отправить письмо")
                recipient = str(input('Повторно введите почту: '))

send_email(sender_email() ,recipient = str(input('Введите почту получателя: ')))