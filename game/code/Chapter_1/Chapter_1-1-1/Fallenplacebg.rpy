screen Fallenplacebg():
    zorder 1
    
    add "images/background/chapter_1/chapter_1-1/ruins_no_flowey.png"

    imagebutton:
        idle "images/background/chapter_1/chapter_1-1/UI/wall_idle.png"
        hover "images/background/chapter_1/chapter_1-1/UI/wall_hovered.png"
        activate_sound "sound/confirm.wav"
        hover_sound "sound/select.wav"
        action Jump("Wall_pressed") 

    imagebutton:
        xpos 0.0
        ypos 0.2625
        idle "images/background/chapter_1/chapter_1-1/UI/circle_idle.png"
        hover "images/background/chapter_1/chapter_1-1/UI/circle_hovered.png"
        activate_sound "sound/confirm.wav"
        hover_sound "sound/select.wav"
        action Jump("Circle_pressed") 

    imagebutton:
        xpos 0.843
        ypos 0.275
        idle "images/background/Chapter_1/Chapter_1-1/UI/tombstone_idle.png" 
        hover "images/background/Chapter_1/Chapter_1-1/UI/tombstone_hovered.png"
        activate_sound "sound/confirm.wav"
        hover_sound "sound/select.wav"
        action Jump("Tombstone_pressed")  
    
    imagebutton:
        xpos 0.1285
        ypos 0.281
        idle "images/background/Chapter_1/Chapter_1-1/UI/flowerpile_idle.png"
        hover "images/background/Chapter_1/Chapter_1-1/UI/flowerpile_hovered.png"
        activate_sound "sound/confirm.wav"
        hover_sound "sound/select.wav"
        action Jump("Flowerpile_pressed") 

    imagebutton:
        xpos 0.233
        ypos 0.00
        idle "images/background/Chapter_1/Chapter_1-1/UI/pillar_idle.png" 
        hover "images/background/Chapter_1/Chapter_1-1/UI/pillar_hovered.png"
        activate_sound "sound/confirm.wav"
        hover_sound "sound/select.wav"
        action Jump("Pillar_pressed")  

    imagebutton:
        xpos 0.35
        ypos 0.00
        idle "images/background/Chapter_1/Chapter_1-1/UI/light_idle.png"
        hover "images/background/Chapter_1/Chapter_1-1/UI/light_hovered.png"
        activate_sound "sound/confirm.wav"
        hover_sound "sound/select.wav"
        action Jump("Light_pressed")

    #####I hate grass############ 

    imagebutton:
        xpos 0.318
        ypos 0.805
        idle "images/background/Chapter_1/Chapter_1-1/UI/grass1_idle.png"
        hover "images/background/Chapter_1/Chapter_1-1/UI/grass1_hovered.png"
        activate_sound "sound/confirm.wav"
        hover_sound "sound/select.wav"
        action Jump("Grass1_pressed") 

    imagebutton:
        xpos 0.673
        ypos 0.76
        idle "images/background/Chapter_1/Chapter_1-1/UI/grass2_idle.png"
        hover "images/background/Chapter_1/Chapter_1-1/UI/grass2_hovered.png"
        activate_sound "sound/confirm.wav"
        hover_sound "sound/select.wav"
        action Jump("Grass2_pressed") 

    imagebutton:
        xpos 0.727
        ypos 0.407
        idle "images/background/Chapter_1/Chapter_1-1/UI/grass3_idle.png"
        hover "images/background/Chapter_1/Chapter_1-1/UI/grass3_hovered.png"
        activate_sound "sound/confirm.wav"
        hover_sound "sound/select.wav"
        action Jump("Grass3_pressed") 

    imagebutton:
        xpos 0.173
        ypos 0.405
        idle "images/background/Chapter_1/Chapter_1-1/UI/grass4_idle.png"
        hover "images/background/Chapter_1/Chapter_1-1/UI/grass4_hovered.png"
        activate_sound "sound/confirm.wav"
        hover_sound "sound/select.wav"
        action Jump("Grass4_pressed") 

    if persistent.Flowey_click_count <8:
        imagebutton:
            xpos 0.6335
            ypos 0.4285
            idle "images/characters/Flowey/flowey_idle.png"
            hover "images/characters/Flowey/flowey_hovered.png" 
            activate_sound "sound/confirm.wav"
            hover_sound "sound/select.wav"
            action Jump("Flowey_pressed") 