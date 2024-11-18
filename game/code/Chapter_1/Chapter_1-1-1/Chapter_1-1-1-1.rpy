##chapter_1-1-1-1開始

image Chara sad = "images/characters/Chara/Chara_sad.png"
image bg_Ruins = "images/background/chapter_1/chapter_1-1/ruins.png"

default persistent.Circle_click_count = 0
default persistent.Tombstone_click_count = 0
default persistent.Flowerpile_click_count = 0

label chapter_1_1_1_1:
    play music "elementary-wave.wav" volume 0.3
    $ quick_menu = False
    call screen Fallenplacebg()

label Wall_pressed:
    $ renpy.block_rollback()
    scene bg_Ruins

    show white:
        alpha 0.2 
    pause 0.2
    $ quick_menu = True    
    Narration "* 與上方洞穴是同一種岩質，有水蝕的痕跡。"    

    jump chapter_1_1_1_1


label Circle_pressed:

    $ renpy.block_rollback()
    $ persistent.Circle_click_count += 1
    scene bg_Ruins

    show white:
        alpha 0.2 
    pause 0.2
    $ quick_menu = True  

    if persistent.Circle_click_count == 1:
        $ quick_menu = True
        Narration "* 似乎是用粉筆畫出來的，又被人為抹去大半。"
    elif persistent.Circle_click_count == 2:
        $ quick_menu = True
        Chara "* 她碰了碰白色污痕。"
        Chara "* （沒有想像中那麼容易擦掉。）"
    else:
        $ quick_menu = True
        "* 從殘餘的粉筆痕跡看來，或許它曾經是一個圓形法陣。" 

    jump chapter_1_1_1_1


label Tombstone_pressed:

    $ renpy.block_rollback()
    $ persistent.Tombstone_click_count +=1
    scene bg_Ruins

    show white:
        alpha 0.2 
    pause 0.2
    $ quick_menu = True  

    if persistent.Tombstone_click_count == 1:
        $ quick_menu = True
        Narration "* 尚新的墓碑，象徵一個生命的殞落。"
    elif persistent.Tombstone_click_count == 2:
        $ quick_menu = True
        Narration "* 墓碑上刻著名字的地方被刻意刮除。"
    else:
        $ quick_menu = True
        show Chara sad: 
            zoom 0.25  xalign 0.5 ypos 80
        show white:
            alpha 0.2 
        Chara "* 埋葬死者是人類的習俗。" 
    
    jump chapter_1_1_1_1


label Flowerpile_pressed:

    $ renpy.block_rollback()
    $ persistent.Flowerpile_click_count +=1

    scene bg_Ruins
    show white:
        alpha 0.2 
    pause 0.2

    $ quick_menu = True  
    if persistent.Flowerpile_click_count == 1:
        $ quick_menu = True
        Narration "* 普通的花。 "
    elif persistent.Flowerpile_click_count ==2:
        $ quick_menu = True
        Narration "* 散發一股淡淡的香氣，不靜下心來很難察覺。"
    elif persistent.Flowerpile_click_count ==3:
        $ quick_menu = True
        show Chara sad: 
            zoom 0.25  xalign 0.5 ypos 80
        Chara "* （……他們喜歡的花。）"
    elif persistent.Flowerpile_click_count ==4:
        $ quick_menu = True
        show Chara sad: 
            zoom 0.25  xalign 0.5 ypos 80
        Chara "* （用它們編織花環很漂亮。）"
    else:
        $ quick_menu = True
        show Chara despair: 
            zoom 0.25  xalign 0.5 ypos 80
        Chara "* ......" 

    jump chapter_1_1_1_1