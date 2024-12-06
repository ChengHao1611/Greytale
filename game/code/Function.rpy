
init python:
    ##傳入背景的圖片，就能在對話時產生背景
    def bgOfDialogue(bg):
        ##禁止回調
        renpy.block_rollback()

        renpy.scene()
        renpy.show(bg)
        renpy.show("bg_White")
        
        renpy.pause(0.2)