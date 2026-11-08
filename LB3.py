import tkinter as tk
import random


def exit():             #функция выхода из генератора ключей
    window.destroy()

def calculate_average(block):                   #функция для подсчета среднего значения блока
    total_weight = sum(WEIGHTS[char] for char in block)
    return total_weight / len(block)

def generate_block(length):                              #функция генерации блока
    while True:
        block = ''.join(random.choices(CHARS, k=length)) #блок собирается из случайно выбранных символов по заданной длине
        avg = calculate_average(block)                   #высчитывание среднего значения
        if MIN_VAL <= avg <= MAX_VAL:                    #если среднее значение подходит, то блок добавляется в ключ
            return block

def generate_key():                           #функция сборки ключа
    block1 = generate_block(5)
    block2 = generate_block(4)
    block3 = generate_block(4)
    full_key = f'{block1}-{block2}-{block3}'
    key_entry.delete(0, 'end')      #очищается текущий текст в окне
    key_entry.insert(0, full_key)       #в окно записывается новый ключ


CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
WEIGHTS = {char: i + 1 for i, char in enumerate(CHARS)} #каждому символу выставляется его числовое значение
MIN_VAL = 10
MAX_VAL = 30

window = tk.Tk()           #создание окна генератора
window.title('KEYGEN')
window.geometry('750x360')
window.resizable(False, False)

try:
    bg_img = tk.PhotoImage(file='bg.png')
    label_bg = tk.Label(window, image=bg_img)
    label_bg.place(x=0, y=0, relwidth=1, relheight=1)
except Exception:                                       #если не нашелся файл для фона, то фон делается белым
    window.config(bg='white')


key_entry = tk.Entry(window,                       #создание окна для ключей
                     font=('Consolas', 18),
                     justify='center')
key_entry.pack(pady=(100,0))
key_entry.insert(0,'XXXXX-XXXX-XXXX')


generate_btn = tk.Button(window,                    #создание кнопки генерации ключа
                         text='СГЕНЕРИРОВАТЬ КЛЮЧ',
                         font=('Consolas', 18),
                         command=generate_key)
generate_btn.pack(pady=10)


exit_btn = tk.Button(window,                         #создание кнопки выхода
                     text='EXIT',
                     font=('Consolas', 14),
                     command=exit)
exit_btn.pack()


window.mainloop()