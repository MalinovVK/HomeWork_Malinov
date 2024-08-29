calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return calls
def string_info(stroka):
    count_calls()
    tuple = (len(stroka), stroka.lower(), stroka.upper())
    return tuple
def is_contains(str, list):
    count_calls()
    for i in range(len(list)):
        if str.lower() == list[i].lower():
            a = True
            break
        else:
            a = False
    return a

print(string_info('Capybara'))
print(string_info('Armageddod'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('Cycle', ['recycling', 'cycling', 'urBAN']))
print(calls)