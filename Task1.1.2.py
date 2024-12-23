#Задание 2. (повышенной сложности)

#Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы, 
#в котором вывод разбивается на слова с удалением всех знаков пунктуации (их можно взять из списка string.punctuation модуля string). 
#В этом режиме должно проверяться наличие слова в выводе.


import subprocess
import string
if __name__=='__main__':
    def execute_and_find(command, text, word_mode=False):
        try:
            # Выполнение команды и её вывод
            result = subprocess.run(command, shell=True, text=True, capture_output=True)
       
            # Проверка - успешно ли выполнена команда
            if result.returncode != 0:
                return False
       
            output = result.stdout
       
            if word_mode:
                # Удаление всех знаков пунктуации из вывода
                translator = str.maketrans('', '', string.punctuation)
                clean_output = output.translate(translator)
                # Разбивка вывода на слова
                words = clean_output.split()
                # Проверка наличия слова
                return text in words
            else:
                # Проверка наличия текста в выводе
                return text in output
        except Exception as e:
            # Если появляется ошибка, возврат False
            return False