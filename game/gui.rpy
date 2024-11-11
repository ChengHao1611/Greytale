################################################################################
## 初始化
################################################################################

## init offset 語句導致此文件中的初始化語句在任何其他文件中的 init 語句之前運
## 行。
init offset = -2

## 呼叫 gui.init 將樣式重置為合理的預設值，並設定遊戲的寬度和高度
init python:
    gui.init(1920, 1080)

## 啟用螢幕或變換中無效或不穩定屬性的檢查
define config.check_conflicting_properties = True


################################################################################
## GUI 配置變數
################################################################################


## 顔色 ##########################################################################
##
## 介面中文字的顏色

## 整個介面中使用的強調色，用於標記和突出顯示文字
define gui.accent_color = u'#ffffff'

## 當文字按鈕既未被選取也未被懸停時所使用的顏色
define gui.idle_color = u'#FFFFFF'
## 小顏色適用於小文本，需要更亮/更暗才能達到與普通文本相同的效果
define gui.idle_small_color = u'#FFFFFF'

## 用於懸停的按鈕和欄的顏色
define gui.hover_color = u'#FFF200'

## 當文字按鈕被選取但未獲得焦點時所使用的顏色。如果按鈕是目前畫面或首選項值，則
## 按鈕將被選取
define gui.selected_color = u'#ffffff'

## 無法選擇文字按鈕時使用的顏色
define gui.insensitive_color = u'#8888887f'

## 顏色用於未填充的條形部分。這些顏色不直接使用，而是在重新生成條形圖像檔案時使
## 用
define gui.muted_color = u'#3d5166'
define gui.hover_muted_color = u'#5b7a99'

## 用於對話和選單選擇文字的顏色
define gui.text_color = u'#ffffff'
define gui.interface_text_color = u'#ffffff'


## 字形和字形大小 #####################################################################

## 用於遊戲內文字的字形
define gui.text_font = "fonts/Cubic_11_1.010_R.ttf"

## 用於角色名稱的字形
define gui.name_text_font = "fonts/Cubic_11_1.010_R.ttf"

## 用於遊戲外文本的字形
define gui.interface_text_font = "fonts/Cubic_11_1.010_R.ttf"

#目前尚未搞懂
define gui.textbutton_text_font = "fonts/Cubic_11_1.010_R.ttf"
define gui.navigation_button_text_font = "fonts/Cubic_11_1.010_R.ttf"
define gui.quick_button_text_font = "fonts/Cubic_11_1.010_R.ttf"
define gui.confirm_button_text_font = "fonts/Cubic_11_1.010_R.ttf"
define gui.choice_button_text_font = "fonts/Cubic_11_1.010_R.ttf"
define gui.game_menu_button_text_font = "fonts/Cubic_11_1.010_R.ttf"

## 正常對話文字的大小
define gui.text_size = 40

## 角色名稱的大小
define gui.name_text_size = 55

## 遊戲用戶介面中的文字的大小
define gui.interface_text_size = 40

## 遊戲用戶介面中標籤的大小
define gui.label_text_size = 40

## 通知螢幕上的文字大小
define gui.notify_text_size = 24

## 遊戲標題的大小
define gui.title_text_size = 75

#待修改，翻譯內容
# translate English style default:
#     font "fonts/DTM-Mono.otf"

# translate English python:
#     gui.text_font = "fonts/DTM-Mono.otf"
#     gui.name_text_font = "fonts/DTM-Sans.otf"
#     gui.interface_text_font = "fonts/DTM-Mono.otf"
#     gui.navigation_button_text_font = "fonts/DTM-Sans.otf"
#     gui.quick_button_text_font = "fonts/DTM-Sans.otf"
#     gui.confirm_button_text_font = "fonts/DTM-Sans.otf"
#     gui.choice_button_text_font = "fonts/DTM-Sans.otf"
#     gui.button_text_font = "fonts/DTM-Sans.otf"
#     gui.title_text_size = 45
#     gui.text_size = 35


## 主選單和遊戲選單 ####################################################################

## 用於主選單和遊戲選單的圖像
define gui.demo_stamp= "gui/demo.png"
define gui.font_title= "gui/FONT.png"
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## 對話 ##########################################################################
##
## 這些變數控制對話如何一次一行地顯示在螢幕上

## 包含對話的文本框的高度
define gui.textbox_height = 278

## 文本框在螢幕上垂直的位置。0.0 是頂部，0.5 是中心，1.0 是底部
define gui.textbox_yalign = 1.0


## 對話角色的名字相對於文本框的位置。這些可以是從左側或頂部開始的整數像素，也可
## 以是到中心的 0.5 個像素
define gui.name_xpos = 360
define gui.name_ypos = -10

## 角色名稱的水平對齊方式。左對齊可以為 0.0，居中對齊可以為 0.5，右對齊可以為
## 1.0
define gui.name_xalign = 0.0

## 包含角色名稱的框的寬度、高度和邊框，或無以自動調整其大小
define gui.namebox_width = None
define gui.namebox_height = None

## 包含角色名稱的框的邊框，按左、上、右、下順序排列
define gui.namebox_borders = Borders(5, 5, 5, 5)

## 如果為 True ，名稱框的背景將平鋪，如果為 False ，則名稱框的背景將縮放
define gui.namebox_tile = False


## 對話相對於文本框的位置。這些可以是相對於文字方塊左側或頂部的整數像素，或相對
## 於中心的 0.5 個像素
define gui.dialogue_xpos = 400
define gui.dialogue_ypos = 90

## 對話文字的最大寬度，以像素為單位
define gui.dialogue_width = 1000

## 對話文字的水平對齊方式。左對齊可以為 0.0，居中對齊可以為 0.5，右對齊可以為
## 1.0
define gui.dialogue_text_xalign = 0.0


## 按鈕 ##########################################################################
##
## 這些變數與 gui/button 中的圖像檔案一起控制按鈕顯示方式的各個方面

## 按鈕的寬度和高度，以像素為單位。如果沒有，Ren'Py 會計算其尺寸
define gui.button_width = None
define gui.button_height = None

## 按鈕兩側的邊框，依左、上、右、下順序排列
define gui.button_borders = Borders(6, 6, 6, 6)

## 如果為 True ，背景圖像將平鋪。如果為 False ，背景圖像將線性縮放
define gui.button_tile = False

## 按鈕使用的字型
define gui.button_text_font = gui.interface_text_font

## 按鈕使用的文字大小
define gui.button_text_size = gui.interface_text_size

## 各種狀態下按鈕文字的顏色
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## 按鈕文字的水平對齊方式。（0.0 為左，0.5 為中，1.0 為右）
define gui.button_text_xalign = 0.0


## 這些變數會覆寫不同類型按鈕的設定。請參閱 gui 文檔以了解可用按鈕的類型以及每個
## 按鈕的用途
##
## 預設介面使用這些自訂設定：

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## 您也可以透過新增正確命名的變數來新增自己的自訂設定。例如，您可以取消註解以下
## 行以設定導覽按鈕的寬度

# define gui.navigation_button_width = 250


## 選項按鈕 ########################################################################
##
## 選擇按鈕用於遊戲內選單

define gui.choice_button_width = 500
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(10, 10, 10, 10)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_yalign = 1.0
define gui.choice_button_text_idle_color = u'#ffffff'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = u'#ffffff'

## 存檔槽按鈕 #######################################################################
##
## 存檔槽按鈕是一種特殊類型的按鈕。它包含縮圖和描述儲存槽內容的文字。與其他類型
## 的按鈕一樣，儲存槽使用 gui/button 中的圖像檔案

## 儲存槽按鈕
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## 儲存槽使用的縮圖的寬度和高度
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## 儲存槽網格中的列數和行數
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## 位置和間距 #######################################################################
##
## 這些變數控制各種用戶介面元素的位置和間距

## 導航按鈕左側一般相對於螢幕左側的位置
define gui.navigation_xpos = 60

## 跳過指示器的垂直位置
define gui.skip_ypos = 15

## 通知畫面的垂直位置
define gui.notify_ypos = 68

## 選單選項之間的間距
define gui.choice_spacing = 40

## 主選單和遊戲選單導航部分中的按鈕
define gui.navigation_spacing = 15

## 控制首選項之間的間距
define gui.pref_spacing = 15

## 控制首選項按鈕之間的間距
define gui.pref_button_spacing = 0

## 存檔頁面按鈕之間的間距
define gui.page_spacing = 0

## 存檔槽之間的間距
define gui.slot_spacing = 15

## 主選單文字的位置
define gui.main_menu_text_xalign = 1.0


## 框架 ##########################################################################
##
## 當不存在覆蓋層或視窗時，這些變數控制可以包含使用者介面元件的框架的外觀

## 通用框架
define gui.frame_borders = Borders(6, 6, 6, 6)

## 用作確認螢幕一部分的框架
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## 用作跳過螢幕一部分的框架
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## 用作通知螢幕一部分的框架
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## 應該平鋪框架背景嗎？
define gui.frame_tile = False


## 條、捲軸和滑塊 #####################################################################
##
## 這些控制條、捲軸和滑塊的外觀和大小
##
## 預設 GUI 僅使用滑塊和垂直滾動條。所有其他捲軸僅在創建者編寫的螢幕中使用

## 水平條、捲軸和滑塊的高度。垂直條、捲軸和滑塊的寬度
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## 如果需要條圖平鋪，則為 True。如果需要條圖線性縮放，則為 False
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## 水平邊框
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## 垂直邊框
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## 如何處理 gui 中不可滾動的捲軸。 "hide" 隱藏它們，而 None 則顯示它們
define gui.unscrollable = "hide"


## 歷史 ##########################################################################
##
## 歷史畫面顯示玩家已經閱讀過的對話

## Ren'Py 將保留的對話歷史記錄區塊的數量
define config.history_length = 250

## 歷史畫面條目的高度，或設爲 None 以犧牲性能為代價使高度可變
define gui.history_height = 150

## 在歷史畫面條目之間添加的額外空間。
define gui.history_spacing = 0

## 給予對話角色名稱的標籤的位置、寬度和對齊方式
define gui.history_name_xpos = 130
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## 對話文字的位置、寬度和對齊方式
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 900
define gui.history_text_xalign = 0.0


## NVL-模式 ######################################################################
##
## NVL 模式畫面顯示 NVL 模式角色所說的對話

## NVL 模式背景視窗的背景邊框
define gui.nvl_borders = Borders(0, 15, 0, 30)

## Ren'Py 將顯示的 NVL 模式條目的最大數量。當要顯示的條目多於此時，最舊的條目將
## 被刪除。
define gui.nvl_list_length = 6

## NVL 模式條目的高度。將其設為 None 以使條目動態調整高度
define gui.nvl_height = 173

## 當 gui.nvl_height 為 None 時 NVL 模式條目之間的間距，以及 NVL 模式條目和選單
## 之間的間距
define gui.nvl_spacing = 15

## 給予對話角色名稱的標籤的位置、寬度和對齊方式
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## 對話文字的位置、寬度和對齊方式
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## nvl_thought 文字的位置、寬度和對齊方式（由 nvl_narrator 字元表示的文字）
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## nvl menu_buttons 的位置
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## 在地化 #########################################################################

## 這控制允許換行的位置。預設值適用於大多數語言。可用值的清單可以在 https://
## www.renpy.org/doc/html/style_properties.html#style-property-language 中找到財
## 產語言

define gui.language = "unicode"


################################################################################
## 行動裝置
################################################################################

init python:

    ## 這增加了快捷按鈕的大小，使它們在平板電腦和手機上更容易觸摸
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## 這會改變各種 GUI 元素的大小和間距，以確保它們在手機上輕鬆可見
    @gui.variant
    def small():

        ## 字形大小
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## 調整文本框的位置
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## 改變各種東西的大小和間距。
        gui.slider_size = 54

        gui.choice_button_width = 20
        gui.choice_button_text_size = 50

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## 檔案按鈕佈局
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL 模式
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
