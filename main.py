#TODO:IMPORT TKINTER
from tkinter import *
from tkinter import messagebox

#TODO:import the data with the list of instagram account
from game_data import data
from check_list import data_check
#TODO: import the random model
import random



#TODO: a function to request for new data
QUESTION_RETURN = []
def request():
    new_data = random.choice(data)
    QUESTION_RETURN.append(new_data)
    data.remove(new_data)
    return new_data

#TODO: keep track of the score result
SCORE = 0
def user_progress():
    return SCORE+1
#TODO: shiwch the b for a and request new_date for b
def chiwch(b):
    a = b
    b=request()
    return a,b
#TODO: check the user input and how has the more followers
def check(a,b, input_user):
    global SCORE
    if input_user == "a" and a['follower_count'] > b['follower_count']:
        SCORE = user_progress()
        return True
    elif input_user == "b" and b['follower_count'] > a['follower_count']:
        SCORE = user_progress()
        return True
    else:
        """game over"""
        messagebox.showinfo("game result", "GAME OVER")
        return False

#TODO: The start function
def start_game(a,b):
    canver.itemconfig(result, text=f"Result:{SCORE}")
    canver.itemconfig(texts, text=f"a {a['description']} from {a['country']} \nand \na {b['description']} from {b['country']}")
    canver.itemconfig(l_ig, image=name_image[data_check.index(a)])
    canver.itemconfig(r_ig, image=name_image[data_check.index(b)])
    canver.itemconfig(namea, text=f"{a['name']}")
    canver.itemconfig(nameb, text=f"{b['name']}")
    canver.itemconfig(nameas, text=f"{a['name']}")
    canver.itemconfig(namebs, text=f"{b['name']}")

def chc(play):
    global a,b
    if play == True:
        a, b = chiwch(b)
        start_game(a, b)
    else:
        exit()




#TODO: GUI FOR THE GAME

#todo:GUI FUNCTION
def left_butten_function():
    user_input = "a"
    play = check(a, b, user_input)
    chc(play)

def right_butten_function():
    user_input = "b"
    play = check(a, b, user_input)
    chc(play)

def play_page():
    global l_ig,r_ig, texts,a,b, namea,nameb, nameas,namebs, result
    canver.delete(tht)
    canver.create_image(275,142, image=vs)
    canver.create_image(267,235, image=bord)
    texts = canver.create_text(260,232, text="ooo", justify=CENTER, font=("Adobe Arabic Regular",6), fill="#ffffff")
    l_ig =canver.create_image(80,110, image=tx1)
    r_ig =canver.create_image(457, 110, image=tx1)
    l_b = Button(canver,image=left_butten, font=("Adobe Arabic Regular",6), border=0, bg="#25094f", command=left_butten_function)
    l_b.place(y=220,x=30)
    r_b = Button(canver,image=right_butten, border=0, bg="#25094f",command=right_butten_function)
    r_b.place(y=220, x=410)
    namea = canver.create_text(75,273, text="ooo", justify=CENTER, font=("Adobe Arabic Regular",8), fill="#ffffff")
    nameb = canver.create_text(457,273, text="ooo", justify=CENTER, font=("Adobe Arabic Regular",8), fill="#ffffff")
    nameas = canver.create_text(64, 71, text="ooo", justify=LEFT,font=("Adobe Arabic Regular", 3), )
    namebs = canver.create_text(440, 71, text="ooo", justify=LEFT, font=("Adobe Arabic Regular", 3),)
    result = canver.create_text(275,20, text=f"Result:{SCORE}", justify=CENTER, font=("Adobe Arabic Regular",18), fill="#ffffff")

    a = request()
    b = request()
    start_game(a, b)






home = Tk()
home.title("HIGHER LOWER")
home.geometry("535x289")
canver = Canvas(width=537, height=289)
canver.place(x=-2,y=0)
#todo: load all the image needed
backgroun =PhotoImage(file="image/background.png")
left_butten = PhotoImage(file="image/left_butten.png")
right_butten = PhotoImage(file="image/right_butten.png")
vs = PhotoImage(file="image/vs.png")
bord = PhotoImage(file="image/bord.png")
tx1 =  PhotoImage(file="image/text.png")

#TODO: ig profiles
Instagram = PhotoImage(file=f'IG_image/Instagram.png')
Cristiano_Ronaldo = PhotoImage(file=f'IG_image/Cristiano Ronaldo.png')
Ariana_Grande = PhotoImage(file=f'IG_image/Ariana Grande.png')
Dwayne_Johnson = PhotoImage(file=f'IG_image/Dwayne Johnson.png')
Selena_Gomez = PhotoImage(file=f'IG_image/Selena Gomez.png')
Kylie_Jenner = PhotoImage(file=f'IG_image/Kylie Jenner.png')
Kim_Kardashian = PhotoImage(file=f'IG_image/Kim Kardashian.png')
Lionel_Messi = PhotoImage(file=f'IG_image/Lionel Messi.png')
Beyoncé = PhotoImage(file=f'IG_image/Beyoncé.png')
Neymar = PhotoImage(file=f'IG_image/Neymar.png')
National_Geographic = PhotoImage(file=f'IG_image/National Geographic.png')
Justin_Bieber = PhotoImage(file=f'IG_image/Justin Bieber.png')
Taylor_Swift = PhotoImage(file=f'IG_image/Taylor Swift.png')
Kendall_Jenner = PhotoImage(file=f'IG_image/Kendall Jenner.png')
Jennifer_Lopez = PhotoImage(file=f'IG_image/Jennifer Lopez.png')
Nicki_Minaj = PhotoImage(file=f'IG_image/Nicki Minaj.png')
Nike = PhotoImage(file=f'IG_image/Nike.png')
Khloé_Kardashian = PhotoImage(file=f'IG_image/Khloé Kardashian.png')
Miley_Cyrus = PhotoImage(file=f'IG_image/Miley Cyrus.png')
Katy_Perry = PhotoImage(file=f'IG_image/Katy Perry.png')
Kourtney_Kardashian = PhotoImage(file=f'IG_image/Kourtney Kardashian.png')
Kevin_Hart = PhotoImage(file=f'IG_image/Kevin Hart.png')
Ellen_DeGeneres = PhotoImage(file=f'IG_image/Ellen DeGeneres.png')
Real_Madrid_CF = PhotoImage(file=f'IG_image/Real Madrid CF.png')
FC_Barcelona = PhotoImage(file=f'IG_image/FC Barcelona.png')
Rihanna = PhotoImage(file=f'IG_image/Rihanna.png')
Demi_Lovato = PhotoImage(file=f'IG_image/Demi Lovato.png')
Victorias_Secret = PhotoImage(file=f"IG_image/Victoria's Secret.png")
Zendaya = PhotoImage(file=f'IG_image/Zendaya.png')
Shakira = PhotoImage(file=f'IG_image/Shakira.png')
Drake = PhotoImage(file=f'IG_image/Drake.png')
Chris_Brown = PhotoImage(file=f'IG_image/Chris Brown.png')
LeBron_James = PhotoImage(file=f'IG_image/LeBron James.png')
Vin_Diesel = PhotoImage(file=f'IG_image/Vin Diesel.png')
Cardi_B = PhotoImage(file=f'IG_image/Cardi B.png')
David_Beckham = PhotoImage(file=f'IG_image/David Beckham.png')
Billie_Eilish = PhotoImage(file=f'IG_image/Billie Eilish.png')
Justin_Timberlake = PhotoImage(file=f'IG_image/Justin Timberlake.png')
UEFA_Champions_League = PhotoImage(file=f'IG_image/UEFA Champions League.png')
NASA = PhotoImage(file=f'IG_image/NASA.png')
Emma_Watson = PhotoImage(file=f'IG_image/Emma Watson.png')
Shawn_Mendes = PhotoImage(file=f'IG_image/Shawn Mendes.png')
Virat_Kohli = PhotoImage(file=f'IG_image/Virat Kohli.png')
Gigi_Hadid = PhotoImage(file=f'IG_image/Gigi Hadid.png')
Priyanka_Chopra_Jonas = PhotoImage(file=f'IG_image/Priyanka Chopra Jonas.png')
GAG = PhotoImage(file=f'IG_image/9GAG.png')
Ronaldinho = PhotoImage(file=f'IG_image/Ronaldinho.png')
Maluma = PhotoImage(file=f'IG_image/Maluma.png')
Camila_Cabello = PhotoImage(file=f'IG_image/Camila Cabello.png')
NBA = PhotoImage(file=f'IG_image/NBA.png')
name_image = [Instagram, Cristiano_Ronaldo, Ariana_Grande, Dwayne_Johnson, Selena_Gomez, Kylie_Jenner,
              Kim_Kardashian, Lionel_Messi, Beyoncé, Neymar, National_Geographic, Justin_Bieber, Taylor_Swift,
              Kendall_Jenner, Jennifer_Lopez, Nicki_Minaj, Nike, Khloé_Kardashian, Miley_Cyrus, Katy_Perry,
              Kourtney_Kardashian, Kevin_Hart, Ellen_DeGeneres, Real_Madrid_CF, FC_Barcelona, Rihanna,
              Demi_Lovato, Victorias_Secret, Zendaya, Shakira, Drake, Chris_Brown, LeBron_James, Vin_Diesel,
              Cardi_B, David_Beckham, Billie_Eilish, Justin_Timberlake, UEFA_Champions_League, NASA, Emma_Watson,
              Shawn_Mendes, Virat_Kohli, Gigi_Hadid, Priyanka_Chopra_Jonas, GAG, Ronaldinho, Maluma, Camila_Cabello,
              NBA]

canver.create_image(268,145, image=backgroun)
tht = canver.create_text(275,142, text="HIGHER \n            LOWER GAME",justify=LEFT, font=("Copperplate Gothic Bold", 30), fill="#ffffff")
canver.after(4000, play_page)
home.mainloop()
