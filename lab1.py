import re
import random
import datetime


responses = {
    r"привет": "Добрый день!",
    r"как тебя зовут\??": "Меня зовут Бот!",
    r"сколько времени": lambda: datetime.datetime.now().strftime("%H:%M:%S"), 
    r"какое сегодня число": lambda: datetime.datetime.now().strftime("%d.%m.%Y"),
    r"какая сейчас погода": "У меня не доступа к погоде, но надеюсь, что у Вас солнечно!",
    r"(\d+)\s*([+\-\/*])\s*(\d+)": "calculate",  
    r"выход": "exit",
    r"что ты умеешь\??|какие у тебя функции\??|что ты можешь\??": "Я могу отвечать на приветствия, сообщать текущее время и дату, говорить о погоде (как могу), вычислять простые арифметические выражения и прощаться."
}

def calculate(match):
    try:
        num1 = int(match.group(1))
        operator = match.group(2)
        num2 = int(match.group(3))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "нельзя так делать :("
            result = num1 / num2
        else:
            return "Неизвестная операция."

        return str(result)
    except ValueError:
        return "Некорректный ввод чисел."

def chatbot_response(text):
    text = text.lower()  
    for pattern, response in responses.items():
        match = re.search(pattern, text)
        if match:
            if callable(response):  
                return response()  
            elif response == "calculate":
                return calculate(match)  
            elif response == "exit":
                return "До свидания!"
            else:
                return response
    return random.choice(["Я не понял вопрос.", "Попробуйте перефразировать."])

if __name__ == "__main__":
    print("Введите 'выход' для завершения диалога.")
    while True:
        user_input = input("Вы: ")
        response = chatbot_response(user_input)
        print("Бот:", response)
        if user_input.lower() == "выход": 
            break
