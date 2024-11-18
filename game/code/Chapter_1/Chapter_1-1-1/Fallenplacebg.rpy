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