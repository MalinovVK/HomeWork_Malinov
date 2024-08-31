def message():
    global message
    message = input("Введите сообщение которое хотите отправить: ")
    return message

def send_email(sender = "university.help@gmail.ru", *, recipient):
    a = 0
    while a == 0:
        if (recipient.endswith(".com") or recipient.endswith("ru") or recipient.endswith(".net") or recipient.endswith("@")) and recipient != sender:
            message()
            print(f'Отправитель: {sender}')
            print(f'Получатель: {recipient}')
            print(f'Письмо: {message}')
            print(f'Письмо успешно отправлено')
            a = 1
        else:
            if not (recipient.endswith(".com") or recipient.endswith("ru") or recipient.endswith(".net") or recipient.endswith("@")):
                print("Некорректно введена почта")
                recipient = str(input('Повторно введите почту: '))
            elif recipient == sender:
                print("Вы не можете самому себе отправить письмо")
                recipient = str(input('Повторно введите почту: '))

send_email(recipient = str(input('Введите почту получателя: ')).lower())