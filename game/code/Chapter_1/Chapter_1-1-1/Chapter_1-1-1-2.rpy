# 您可以在此編寫遊戲的腳本。
default persistent.Flowey_click_count = 0

# define命令可定義遊戲中出現的角色名稱與對應文本顏色。
define Flowey = Character('[Flowey]', color="#e4e4e4")

# image命令可用於定義一個圖像。
# eg. image eileen happy = "eileen_happy.png"
image Chara sad_smile = "images/characters/Chara/chara_sad_smile.png"
image Flowey worried = "images/characters/Flowey/flowey_worried.png"
image Flowey look_away = "images/characters/Flowey/flowey_look_away.png"
image Flowey happy_goat = "images/characters/Flowey/flowey_happy_goat.png"
image Flowey sad = "images/characters/Flowey/flowey_sad.png"



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
        Flowey "* 「當然！是我Charasriel啊！」"
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
        Chara "* (至少 Charasriel 沒有死，已經是不幸中的大幸了。）"
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
        Flowey "* 「我跑遍了整個地下，都沒看到任何怪物，或許剩下的躲起來了。」"
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
                jump Yes_1
            "No":
                jump No_1

    elif persistent.Flowey_click_count == 2:
        $ renpy.block_rollback()
        Flowey "* 「哦！Chara你回來了？」"
        Flowey "* 「呃......你看起來有點糟糕。」"
        Flowey "* 「需要幫忙嗎？」"  

    elif persistent.Flowey_click_count <= 4:
        $ renpy.block_rollback()
        "* 「嗯？」"

    elif persistent.Flowey_click_count <=6:
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

    return



label Yes_1:
    $ renpy.block_rollback()
    Chara "......。"
    Flowey "* 「啊啊太好了！！妳就把我放到你頭上吧！」"
    Chara "* ......？"
    Narration "* Chara 遲疑地看著小花，比了幾個手勢。"
    Flowey "* 「妳把手伸過來。」"
    Narration "* Chara 向小花伸出她唯一的那隻手。"
    Narration "* 小花伸出他的藤蔓，捲到 Chara 的手臂上，等待對方地將自己移到頭頂。"
    Narration "* 藤蔓輕輕穿過 Chara 的髮絲，小花最終將自己固定在她的頭髮上。"
    Flowey "* 「鏘鏘！就當我是妳的髮箍吧，妳會不會不舒服？」"
    Chara "* 「......。」"
    Chara "* 比了幾個手勢。"
    Flowey "* 「有點癢是嗎？那這樣呢？」"
    Narration "* 他挪了挪位置。"
    Chara "* 「......。」"
    Flowey "* 「那就好！如果我們找到鏡子的話，我可以再把位置喬好看一點。」"
    Chara "* 「......////。」"
    Flowey "* 「但我喜歡看妳漂漂亮亮的樣子嘛！哈哈哈哈......{w}對了！這個給妳。」"
    Narration "* 小花用藤蔓推了推突然出現在 Chara 眼前、有些破碎的重置鍵。"
    Flowey "* 「我覺得妳能用的比我好。」"
    Chara "「......。」"
    Narration "* 她觸碰橘色的按鍵，感覺到它歸屬於自己。"
    Flowey "* 「如果你看得差不多了，那就上路吧？」"

    jump chapter_1_1_1_1


label No_1:
    $ renpy.block_rollback()
    Chara "......。"
    Flowey "* 「啊？！為、為什麼......？」"
    Narration "* 他垂下頭，似乎受到很大的打擊，好一段時間說不出話來。"
    Flowey "* 「好吧，我......尊重妳的選擇。」"
    show Chara sad: 
        zoom 0.25  xalign 0.5 ypos 80
    Chara "* 「......。」" 
    Chara "* （對不起 Charasriel，但我真的不想再看到那種情況發生了。）"
    hide Chara
    Flowey "* 「那些黑色東西真的很危險，妳在地下探索時一定要小心，盡量避開它們，知道嗎？」"
    show Chara sad: 
        zoom 0.25  xalign 0.5 ypos 80 
    Chara "* 「......。」"
    Flowey "* 「Chara......。」"
    Chara "* 她比了好一大串手勢。"
    Flowey "* 「原來如此，可是，那不是妳的錯啊。」"
    show Chara despair: 
        zoom 0.25  xalign 0.5 ypos 80
    Chara "* 「......。」" 
    Chara "* （不，都是我的錯。要不是因為我，他們兩個根本不會......。）"
    show Chara sad: 
        zoom 0.25  xalign 0.5 ypos 80
    Chara "* 她比了幾個手勢。"
    hide Chara
    Flowey "* 「這樣......啊，要是我能再更強一點......。」"
    Flowey "* 「Chara，妳收下這個。」" 
    Narration "* 小花堅定地看向她，忽然，有些破碎的重置鍵出現在她眼前。"
    Flowey "* 「我相信妳比我需要這個東西。」"
    show Chara surprised: 
        zoom 0.25  xalign 0.5 ypos 80
    Chara "* 「......！！」"
    Chara "* 她倉促比劃一陣。"
    hide Chara
    Flowey "* 「噢別擔心，我會一直待在這裡等妳，它們不會過來這裡。」"
    Flowey "* 「......。」"
    Flowey "* {size=-20}「而且，如果妳之後後悔了，也隨時找得到我。」{/size}" 
    Flowey "*「所以，快收下吧，沒關係的！」"
    show Chara sad: 
        zoom 0.25  xalign 0.5 ypos 80 
    Chara "* 「......。」"
    Narration "* Chara 遲疑地伸出手，觸碰浮在空中的重置鍵。"
    Narration "* 在接觸到按鍵的瞬間，她感受到它歸屬於自己。"
    Flowey "*「如果你看得差不多了，那就上路吧？」"

    jump chapter_1_1_1_1