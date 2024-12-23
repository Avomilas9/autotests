#Задание 1. Условие:
#Написать функцию на Python, которой передаются в качестве параметров команда и текст. 
#Функция должна возвращать True, если команда успешно выполнена и текст найден 
#в её выводе и False в противном случае. 
#Передаваться должна только одна строка, разбиение вывода использовать не нужно.


import subprocess
if __name__=='__main__':
    def execute_and_check(command: str, text: str) -> bool:
        try:
        # Выполнение команды
            result = subprocess.run(command, shell=True, text=True, capture_output=True)
        # Проверка наличия текста в выводе
            return text in result.stdout
        except Exception:
        # Если появляется ошибка, возврат False
            return False
        
