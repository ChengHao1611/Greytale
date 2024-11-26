##chapter_1-1-1-1開始

default persistent.Circle_click_count = 0
default persistent.Tombstone_click_count = 0
default persistent.Flowerpile_click_count = 0
default persistent.Pillar_click_count = 0
default persistent.Light_click_count = 0
default persistent.Grass1_click_count = 0
default persistent.Grass2_click_count = 0
default persistent.Grass3_click_count = 0
default persistent.Grass4_click_count = 0

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
        Narration "* 似乎是用粉筆畫出來的，又被人為抹去大半。"
    elif persistent.Circle_click_count == 2:
        Chara "* 她碰了碰白色污痕。"
        Chara "* （沒有想像中那麼容易擦掉。）"
    else:
        "* 從殘餘的粉筆痕跡看來，或許它曾經是一個圓形法陣。" 

    jump chapter_1_1_1_1


label Tombstone_pressed:

    $ renpy.block_rollback()
    $ persistent.Tombstone_click_count += 1
    scene bg_Ruins

    show white:
        alpha 0.2 
    pause 0.2

    $ quick_menu = True  
    if persistent.Tombstone_click_count == 1:
        Narration "* 尚新的墓碑，象徵一個生命的殞落。"
    elif persistent.Tombstone_click_count == 2:
        Narration "* 墓碑上刻著名字的地方被刻意刮除。"
    else:
        show Chara sad: 
            zoom 0.25  xalign 0.5 ypos 80
        show white:
            alpha 0.2 
        Chara "* （埋葬死者是人類的習俗。）" 
    
    jump chapter_1_1_1_1


label Flowerpile_pressed:

    $ renpy.block_rollback()
    $ persistent.Flowerpile_click_count += 1

    scene bg_Ruins
    show white:
        alpha 0.2 
    pause 0.2

    $ quick_menu = True  
    if persistent.Flowerpile_click_count == 1:
        Narration "* 普通的花。 "
    elif persistent.Flowerpile_click_count == 2:
        Narration "* 散發一股淡淡的香氣，不靜下心來很難察覺。"
    elif persistent.Flowerpile_click_count == 3:
        show Chara sad: 
            zoom 0.25  xalign 0.5 ypos 80
        Chara "* （……他們喜歡的花。）"
    elif persistent.Flowerpile_click_count == 4:
        show Chara sad: 
            zoom 0.25  xalign 0.5 ypos 80
        Chara "* （用它們編織花環很漂亮。）"
    else:
        show Chara despair: 
            zoom 0.25  xalign 0.5 ypos 80
        Chara "* ......" 

    jump chapter_1_1_1_1


label Pillar_pressed:

    $ renpy.block_rollback()
    $ persistent.Pillar_click_count += 1

    scene bg_Ruins
    show white:
        alpha 0.2 
    pause 0.2

    $ quick_menu = True
    if persistent.Pillar_click_count == 1:
        Narration"* 破損的石柱，成為一些爬藤植物的生長場所。"
    else:
        Narration "* 柱子上刻有花紋，看上去是某種符文。" 

    jump chapter_1_1_1_1


label Light_pressed:
    $ renpy.block_rollback()
    $ persistent.Light_click_count += 1

    scene bg_Ruins
    show white:
        alpha 0.2 
    pause 0.2

    $ quick_menu = True  
    if persistent.Light_click_count == 1:
        Narration "* 太陽高掛在遙遠的蒼穹上，即使身處地底，仍能清楚感受它的熱度。"
    else:
        Narration "* 垂直通道使原路返回的可能性趨近於零。" 

    jump chapter_1_1_1_1


#######fuck grass

label Grass1_pressed:
    $ renpy.block_rollback()
    $ persistent.Grass1_click_count += 1

    scene bg_Ruins
    show white:
        alpha 0.2 
    pause 0.2

    $ quick_menu = True  
    if persistent.Grass1_click_count == 1:
        Narration "* 淺灰色小草，沾了些許晶瑩剔透的水珠。"
    else:
        show Chara sad: 
            zoom 0.25  xalign 0.5 ypos 80
        Chara "* （看起來很有精神）"

    jump chapter_1_1_1_1


label Grass2_pressed:

    $ renpy.block_rollback()
    $ persistent.Grass2_click_count += 1

    scene bg_Ruins
    show white:
            alpha 0.2 
    pause 0.2

    $ quick_menu = True  
    if persistent.Grass2_click_count == 1:
        Narration "* 淺灰色小草，沾了些許晶瑩剔透的水珠。"
    else:
        show Chara sad: 
            zoom 0.25  xalign 0.5 ypos 80
        Chara "* （看起來很有精神）"

    jump chapter_1_1_1_1


label Grass3_pressed:
    $ renpy.block_rollback()
    $ persistent.Grass3_click_count += 1

    scene bg_Ruins
    show white:
            alpha 0.2 
    pause 0.2

    $ quick_menu = True  
    if persistent.Grass3_click_count == 1:
        Narration "* 淺灰色小草，沾了些許晶瑩剔透的水珠。"
    else:
        show Chara sad: 
            zoom 0.25  xalign 0.5 ypos 80
        Chara "* （看起來很有精神）"

    jump chapter_1_1_1_1

label Grass4_pressed:
    $ renpy.block_rollback()
    $ persistent.Grass4_click_count += 1

    scene bg_Ruins
    show white:
            alpha 0.2 
    pause 0.2
    $ quick_menu = True  
    if persistent.Grass4_click_count == 1:
        Narration "* 淺灰色小草，沾了些許晶瑩剔透的水珠。"
    else:
        show Chara sad: 
            zoom 0.25  xalign 0.5 ypos 80
        Chara "* （看起來很有精神）"

    jump chapter_1_1_1_1

label eye_pressed:
    $ renpy.block_rollback()

    scene bg_Ruins
    show white:
            alpha 0.2 
    pause 0.2

    $ quick_menu = True 
    Narration "* 還沒做好哈哈哈哈"
    Narration "* 哈哈哈哈哈哈哈哈"
    Narration "* 哇哇哇哈哈哈哈哈"

    jump chapter_1_1_1_1