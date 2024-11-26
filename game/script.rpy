# 您可以在此編寫遊戲的腳本。


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
