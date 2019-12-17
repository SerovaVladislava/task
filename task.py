 # Импорт библиотеки
import sqlite3
 
conn = sqlite3.connect("patient.db")
cursor = conn.cursor()
    # Создание таблицы
cursor.execute(
    'CREATE TABLE IF NOT EXISTS pat (fio TEXT, sex TEXT, birth INTEGER,region TEXT)')
conn.commit()
     # Вводим данные
fio = input('Введите ФИО: ')
sex = input('Пол: ')
birth = input('Дата рождения: ')
region = input('Область: ')
    # Вставляем данные в таблицу
cursor.execute('''INSERT INTO pat(fio, sex, birth, region) VALUES (?, ?, ?, ?)''', (fio, sex, birth, region))
conn.commit()
    # Сохраняем изменения
conn.commit()
cursor.close()
conn.close()