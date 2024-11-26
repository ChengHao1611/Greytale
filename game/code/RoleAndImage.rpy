##function
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

##Role
define Narration = Character("",callback = general)  #旁白
define Chara = Character('Chara', color="#D3D3D3") #Chara角色
define Flowey = Character("[Flowey]", color="#e4e4e4")

##Image
image Chara despair = "images/characters/Chara/Chara_despair.png"
image Chara look_up = "images/characters/Chara/Chara_look_up.png"
image Chara surprised = "images/characters/Chara/Chara_surprised.png"
image Chara sad = "images/characters/Chara/Chara_sad.png"
image Chara sad_smile = "images/characters/Chara/chara_sad_smile.png"

image Flowey worried = "images/characters/Flowey/flowey_worried.png"
image Flowey look_away = "images/characters/Flowey/flowey_look_away.png"
image Flowey happy_goat = "images/characters/Flowey/flowey_happy_goat.png"
image Flowey sad = "images/characters/Flowey/flowey_sad.png"

image bg_Ruins = "images/background/chapter_1/chapter_1-1/ruins.png"
image bg_Ruins_no_flowey = "images/background/chapter_1/chapter_1-1/ruins_no_flowey.png"
