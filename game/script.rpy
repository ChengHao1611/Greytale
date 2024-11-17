# 您可以在此編寫遊戲的腳本。
init python:
    
    def general(event, interact=True, **kwargs):
        #播放音效
        ##"show_done"顯示每個對話片段後調用。
        if event == "show_done":
            for i in range(1):
                renpy.sound.play("sound/general.wav", loop="True", channel="sound")
                #renpy.pause(0.2)  # 等待 0.2 秒
            #renpy.sound.play("sound/general.wav", loop="True", channel="sound")
        #"slow_done" 在緩慢的文字顯示完畢後調用
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sound")

#定義角色
define Narration = Character("",callback = general)  #旁白
define Chara = Character('Chara', color="#D3D3D3") #Chara角色

# image命令可用於定義一個圖像。
#前綴BG代表BackGround
# eg. image eileen happy = "eileen_happy.png"
image bg_Ruins_no_flowey = "images/background/chapter_1/chapter_1-1/ruins_no_flowey.png"
#image bg_white = "images/background/white.png"


image Chara despair = "images/characters/Chara/Chara_despair.png"
image Chara look_up = "images/characters/Chara/Chara_look_up.png"
image Chara surprised = "images/characters/Chara/Chara_surprised.png"

#default enterGame = 0  #猜測回到標題畫面default會再跑一次

# label main_menu:
#     #screen main_menu
#     "enterGame = [enterGame]"
#     if enterGame == 0:
#         "恭喜你成功了"
#         "嘿嘿"
#     $ enterGame += 1
#     "enterGame = [enterGame]"
#     call screen main_menu()
#     return


# 遊戲從這裡開始。
label start:
    #這裡的停止音樂是在options.rpy Line:58
    stop music
    hide screen main_menu

    scene black
    Narration "* 睜開眼睛後第一個看到的，{p=0.2}* 是黑白色的花。"
    #使quick_menu不受到"BG_Ruins_no_flowey"的Dissolve影響
    hide screen quick_menu
    $ quick_menu = False
    play music "Undertale - Intro Sound.mp3" volume 1.0

    scene white with Dissolve(5.0)
    stop music

    scene bg_Ruins_no_flowey:
        zoom 1.3 xpos -250 ypos -200
    with Dissolve(2.0)
    pause 1.0

    show white:
        alpha 0.2
    with dissolve   

    show Chara despair: 
        zoom 0.25  xalign 0.5 ypos 80
    with moveinbottom
    $ quick_menu = True 
    Chara "* 「......」"
    Narration "* 她坐起身，輕輕拍掉身上的泥土。"
    Chara "*  （還好沒受傷。）"

    show Chara look_up: 
        zoom 0.25  xalign 0.5 ypos 80
    Narration "* 她抬起頭，環顧四周。"
    hide Chara
    call chapter_1_1_1_1 #跳到chapter_1_1_1_

    return
