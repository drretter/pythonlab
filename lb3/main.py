import random
import tkinter as tk
import winsound


# генерация одного блока ключа (вариант 2: 1 цифра и 3 буквы в случайном порядке)
def generate_block():
    letters = []
    for index in range(3):
        letters.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    digit = random.choice('0123456789')
    symbols = letters + [digit]
    random.shuffle(symbols)
    return ''.join(symbols)


# генерация полного ключа (вариант 2: формат XXXX-XXXX-XXXX-XXXX)
def generate_key():
    blocks = []
    for index in range(4):
        blocks.append(generate_block())
    return '-'.join(blocks)


# обновление поля с ключом при нажатии на кнопку генерации
def apply_key():
    new_key = generate_key()
    key_entry.delete(0, 'end')
    key_entry.insert(0, new_key)


# допзадание: фоновая 8-битная музыка
def play_music():
    winsound.PlaySound('music.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)


def stop_music():
    winsound.PlaySound(None, winsound.SND_PURGE)


def toggle_music():
    if window.is_music_active:
        stop_music()
        window.is_music_active = False
        button_music.configure(text='Включить музыку')
    else:
        play_music()
        window.is_music_active = True
        button_music.configure(text='Выключить музыку')


# допзадание: анимация бегущей строки
def run_animation():
    canvas_banner.move(banner_text, -2, 0)
    x, y = canvas_banner.coords(banner_text)
    if x < -320:
        canvas_banner.coords(banner_text, 580, 13)
    window.after(35, run_animation)


def close_window():
    stop_music()
    window.destroy()


window = tk.Tk()
window.title('Portal - Key Generator (Вариант 2)')
window.geometry('739x415')
window.resizable(False, False)
window.protocol('WM_DELETE_WINDOW', close_window)

# фон
bg_image = tk.PhotoImage(file='bg_pic.png')
label_background = tk.Label(window, image=bg_image)
label_background.place(x=0, y=0, relwidth=1, relheight=1)

# анимация
canvas_banner = tk.Canvas(window, width=540, height=26, bg='#101012', highlightthickness=0)
canvas_banner.place(relx=0.5, y=25, anchor='center')

banner_text = canvas_banner.create_text(
    570, 13,
    text='★ APERTURE SCIENCE KEYGEN ★ PORTAL ★ VARIANT 2 ★ PRESS GENERATE TO GET KEY ★',
    font=('Consolas', 10, 'bold'),
    fill='#00d4ff'
)

# портальные кольца в анимации
canvas_banner.create_oval(8, 5, 24, 21, outline='#ff7700', width=2)
canvas_banner.create_oval(516, 5, 532, 21, outline='#00a2ff', width=2)

# основное окно
frame_card = tk.Frame(window, bg='#18181c', bd=2, relief='ridge', padx=48, pady=16)
frame_card.place(relx=0.5, rely=0.5, anchor='center')

# заголовок и подзаголовок
label_title = tk.Label(
    frame_card,
    text='PORTAL KEYGEN',
    font=('Consolas', 15, 'bold'),
    fg='#ffffff',
    bg='#18181c'
)
label_title.pack(pady=(0, 2))

label_subtitle = tk.Label(
    frame_card,
    text='Вариант 2: XXXX-XXXX-XXXX-XXXX',
    font=('Arial', 9),
    fg='#aaaaaa',
    bg='#18181c'
)
label_subtitle.pack(pady=(0, 10))

# поле для ключа
key_entry = tk.Entry(
    frame_card,
    font=('Consolas', 15, 'bold'),
    width=24,
    justify='center',
    bg='#0c0c0e',
    fg='#00d4ff',
    bd=1,
    relief='solid'
)
key_entry.pack(pady=(0, 14), ipady=3)

# кнопки
frame_buttons = tk.Frame(frame_card, bg='#18181c')
frame_buttons.pack()

button_generate = tk.Button(
    frame_buttons,
    text='Сгенерировать ключ',
    font=('Arial', 9, 'bold'),
    bg='#ff7700',
    fg='#ffffff',
    padx=10,
    pady=4,
    command=apply_key
)
button_generate.pack(side='left', padx=6)

button_music = tk.Button(
    frame_buttons,
    text='Выключить музыку',
    font=('Arial', 9, 'bold'),
    bg='#0088cc',
    fg='#ffffff',
    padx=10,
    pady=4,
    command=toggle_music
)
button_music.pack(side='left', padx=6)

# запуск музыки и анимация, первый кейген
window.is_music_active = True
play_music()
apply_key()
run_animation()

# запуск
window.mainloop()