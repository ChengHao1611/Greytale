# 您可以在此編寫遊戲的腳本。
default persistent.Flowey_click_count = 0


label Flowey_pressed:
    $ renpy.block_rollback()
    scene bg_Ruins
    show white:
            alpha 0.2
    pause 0.5

    $ quick_menu = True    
    $ persistent.Flowey_click_count += 1

    if persistent.Flowey_click_count == 1:
        $ Flowey = "?????"
        Narration "* 一朵與眾不同的花，睜大眼睛，用一種十分錯愕的表情「看」向這邊。"
        Flowey "* {size=+20}「C-Chara？」{/size} "

        show Chara surprised: 
            zoom 0.25  xalign 0.5 ypos 80
        Chara "* 「？！」"
        Narration "* 她微微一驚，循聲轉頭，卻沒發現半個人影。"
        hide Chara
        Chara "* 「......」"
        Narration "* 她定睛一看，發現有朵奇怪的花在看她。"
        
        show Flowey worried: 
            zoom 0.2  xalign 0.5 ypos 220
        Flowey "*「妳怎麼會在這裡？」"
        hide Flowey
        Chara "* 「......？」"
        Narration "* 她快速比了幾個手勢。"
        
        show Chara despair: 
            zoom 0.25  xalign 0.5 ypos 80
        Chara "* (不對……他怎麼可能看得懂。)"
        hide Chara
        Flowey "* 「！！」"
        Narration "* 那朵花興奮地靠了過來。"
        
        $ Flowey = "Flowey"
        show Flowey happy_goat: 
            zoom 0.25  xalign 0.5 ypos 150
        Flowey "* 「當然！是我Asriel啊！」"
        Flowey "* 「不過我現在變成一朵小花就是了，說來話長。」"
        hide Flowey
        Chara "* 「！」"
        Narration "* 她的眼中出現光彩，比了一個特別的手勢，急切地向小花投以疑問的眼神。"
        Chara "* 「......？」"

        show Flowey worried: 
            zoom 0.25  xalign 0.5 ypos 150
        Flowey "* 「這個嘛.....。」"

        show Flowey look_away: 
            zoom 0.25  xalign 0.5 ypos 150   
        Flowey "* 「他......沒能活下來。」"
        hide Flowey

        show Chara sad: 
            zoom 0.25  xalign 0.5 ypos 150 
        Chara "* 「......。」"
        hide Chara

        show Flowey sad:
            zoom 0.25  xalign 0.5 ypos 150  
        Flowey "* 「......。」"
        Chara "* (至少 Asriel 沒有死，已經是不幸中的大幸了。）"
        hide Flowey sad

        show Chara sad_smile:
            zoom 0.25  xalign 0.5 ypos 80 
        Narration "* Chara 比了一連串手勢，並附上一個淺笑。"
        hide Chara
        Flowey "* 「我也很高興能再見到妳。」"

        show Flowey sad:
            zoom 0.25  xalign 0.5 ypos 150  
        Flowey "* 「......」"
        Narration "* 沉默片刻，小花臉色凝重地開口："
        hide Flowey sad

        show Flowey worried: 
            zoom 0.25  xalign 0.5 ypos 150
        Flowey "* 「抱歉，我很不想說這些，但地下出事了。」"
        Flowey "* 「到處都是奇怪的黑色東西，看到我就撲過來攻擊，路上還有好多塵埃......」"
        Flowey "* 「我跑遍了整個地下，都沒看到任何怪物，或許剩下的怪物躲起來了。」"
        Flowey "* 「後來我在實驗室看到 Misty 之前研究的東西，就是那個重置鍵，妳還記得吧？」"
        hide Flowey
        Chara "*  點頭。"

        show Flowey worried: 
            zoom 0.25  xalign 0.5 ypos 150
        Flowey "*「我找到這玩意時，它整個毀了。」"
        hide Flowey
        Narration "* 小花凝視某處空氣。{w}忽然，一個橘色、毀損的按鍵浮現在他眼前。"
        Flowey "* 「這裡是唯一安全的地方。」"
        Flowey "* 「我一直在試著修這個東西，但我不確定它恢復了多少功能。」"
        Narration "* 他蹙眉，伸出藤蔓，試著將一塊飄在旁邊碎片拼回按鍵本體，"
        Narration "* 但一放手，碎片又懶洋洋地飄開。"
        Flowey "* 「搞不懂是什麼原理。」"
        Narration "* 小花看向 Chara ，按鍵隨之消失。"

        show Flowey worried: 
            zoom 0.25  xalign 0.5 ypos 150
        Flowey "* 「Chara，我能不能拜託妳一件事？」"
        hide Flowey
        Chara "* 「......？」"
        Narration "* 歪頭表示疑問。"
        Flowey "* 「帶上我，我們一起去弄清楚到底出了什麼事，"
        Flowey "* 也看看能不能找到其他怪物，還有 Misty 的研究筆記？當然找到他本人更好。」"
        Flowey "* 「我單獨行動應付不了那些黑色東西，沒辦法好好搜尋線索。」"
        Flowey "* 「妳覺得呢？」"
        Narration "* 他一臉期盼地等待著答覆。"

        menu:
            "* 要帶上小花嗎？"
            "Yes":
                jump chapter_1_1_1_3 #跳到回答Yes的label
            "No":
                jump chapter_1_1_1_4 #跳到回答No的label

    elif persistent.Flowey_click_count == 2:
        $ renpy.block_rollback()
        Flowey "* 「哦！Chara你回來了？」"
        Flowey "* 「呃......你看起來有點糟糕。」"
        Flowey "* 「需要幫忙嗎？」"  

    elif persistent.Flowey_click_count == 3 or persistent.Flowey_click_count == 4 :
        $ renpy.block_rollback()
        "* 「嗯？」"

    elif persistent.Flowey_click_count == 5 or persistent.Flowey_click_count == 6:
        $ renpy.block_rollback()
        Flowey "* 「......」"

    elif persistent.Flowey_click_count ==7:
        $ renpy.block_rollback()
        Flowey "* 「喂！你是故意的吧？！」"
        Flowey "* 「沒事就沒事，幹嘛要回來惹我？！」"
        Flowey "* 「我和 Chara 是朋友，所以我會給予她一定的通融，"
        Flowey "* 但對於你/妳們，我耐心是有限的！」"
        Flowey "* 「都怪你/妳，她現在很不舒服！！」"
        Flowey "* 「這是我最後的警告，臭玩家！要做什麼趕快做！」"

    else: 
        $ renpy.block_rollback()
        Flowey "* 「煩死了！」"
        Flowey "* 「滾！！！」"
        hide Flowey
        Narration "* 小花以極快的速度鑽回土裡了。"
        jump chapter_1_1_1_1
    
    jump chapter_1_1_1_1
