import pyautogui as pg, time as t, threading as th, random as rd, numpy as np, pytesseract as tess, pygame as pgm, tkinter as tk, os, keyboard as kb
from colorama import init as i, Fore as f

i(autoreset=True)


scr_status, cpt_dtc, at_thread, cpt_thread = True, False, None, None
last_wpray = 0

# Membaca text untuk notifikasi captcha (tambahkan jika memungkinkan)
cpt_text = ["https://owobot.com/captcha", "If you have trouble solving the captcha", "Please complete captcha", "please complete", "captcha", "result in a ban!", "Please complete your captcha","to verify that", "you are human!", "are you a real human?"]

# Membersihkan terminal
def cl_term():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menampilkan notifikasi captcha
def sh_ntf():
    global scr_status, cpt_dtc
    try:
        win = tk.Tk()
        tk.Label(win, text="Close this, solve captcha, and press 'Down Arrow' to continue!").pack()
        pgm.init()
        pgm.mixer.init()
        pgm.mixer.music.load("C:/***/***/***.mp3") #Ubah dan sesuaikan lokasi lagu atau suara notifikasi
        pgm.mixer.music.play()
        scr_status, cpt_dtc = True, True
        win.mainloop()
    except Exception as ex:
        print(f"{f.RED}Error in sh_ntf: {ex}")

# Fungsi autotyping
def at_func():
    global last_wpray, scr_status, cpt_dtc
    try:
        while not scr_status and not cpt_dtc:

            # Perintah dasar
            for cmd in ["wh", "wb", "owo"]:
                if scr_status or cpt_dtc: return
                pg.typewrite(cmd), pg.press('enter')
                t.sleep(2)

            # Peluang "wbuy 1"
            if rd.random() <= 0.8:
                if scr_status or cpt_dtc: return
                pg.typewrite("wbuy 1"), pg.press('enter')
                t.sleep(3.5)

            # Pilihan perintah fun
            if rd.random() <= 0.05:
                cmd_fun = rd.choice(["wrun", "wpiku", "wpup", "wkiss @owo \n", "wwave @owo \n", "wpunch @owo \n", "wcuddle @owo \n", "wpat @owo \n", "wlb all", "wwc all"])
                if scr_status or cpt_dtc: return
                pg.typewrite(cmd_fun), pg.press('enter')
                t.sleep(3.5)

            # Perintah gambling
            if rd.random() <= 0.4:
                cmd_gamble = rd.choice(["ws 1", "wcf 1", "wcf t 1"])
                if scr_status or cpt_dtc: return
                pg.typewrite(cmd_gamble), pg.press('enter')
                t.sleep(2)

            # Perintah tambahan
            if rd.random() <= 0.08:
                cmd_add = rd.choice(["wping", "ww", "wcl", "winv", "wz", "wdaily", "wq"])
                if scr_status or cpt_dtc: return
                pg.typewrite(cmd_add), pg.press('enter')
                t.sleep(2)
            
            # "wpray" setiap 5 menit
            if t.time() - last_wpray >= 300:
                if scr_status or cpt_dtc: return
                pg.typewrite("wpray"), pg.press('enter')
                last_wpray = t.time()

            # Delay random
            for _ in range(rd.randint(8, 13)):
                if scr_status or cpt_dtc: return
                t.sleep(1)

    except Exception as ex:
        print(f"{f.RED}Error in at_func: {ex}")

# Fungsi pengecekan captcha
def chk_cpt():
    global scr_status, cpt_dtc
    try:
        while True:
            if not scr_status and not cpt_dtc:

                # Ambil screenshot dan ubah ke teks
                sc_text = tess.image_to_string(np.array(pg.screenshot()), lang='eng', config='--psm 11')
                
                # Cek jika teks captcha terdeteksi
                if any(ct in sc_text for ct in cpt_text):
                    print(f"\n{f.YELLOW}{'='*23}\n🎯 Captcha Detected! 🚫\nSolve the Captcha & Restart the bot!\n{'='*23}")
                    sh_ntf()
                    scr_status = True
                    
            t.sleep(1)
    except Exception as ex:
        print(f"{f.RED}Error in chk_cpt: {ex}")

# Fungsi toggle script
def tg_scr():
    global scr_status, cpt_dtc, at_thread
    try:
        scr_status = not scr_status
        if scr_status:
            print(f"\n{f.RED}{'-'*23}\n✋ Script Stopped! 🛑\n{'-'*23}")
        else:
            print(f"\n{f.GREEN}{'-'*23}\n🚀 Script Started! 🟢\n{'-'*23}")
            cpt_dtc = False
            at_thread = th.Thread(target=at_func)
            at_thread.start()
    except Exception as ex:
        print(f"{f.RED}Error in tg_scr: {ex}")

# Memulai script
cl_term()
print(f"{f.CYAN}Press Down Arrow to start/stop the script!")
kb.add_hotkey('down', tg_scr)
cpt_thread = th.Thread(target=chk_cpt, daemon=True)
cpt_thread.start()

while True:
    t.sleep(1)
