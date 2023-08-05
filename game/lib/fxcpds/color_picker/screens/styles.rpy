#
# Screen Body
#

style _color_picker_backdrop:
    background "#00000088"
    xfill True
    yfill True

style _color_picker_container:
    background None
    xcenter 0.5
    ycenter 0.5

style _color_picker_body:
    background "#2e2c2c"
    xsize 0.5
    xpadding 20
    ypadding 20

#
# Color HBars
#

style _color_picker_bar_text:
    color "#dddddd"
    yalign 0.5

style _color_picker_bar:
    left_bar gui.accent_color
    idle_right_bar gui.muted_color
    hover_right_bar gui.hover_muted_color
    ysize gui.bar_size

#
# Color Preview
#

style _color_picker_preview:
    background "_color_picker_preview"
    xsize 270
    ysize 270
    yalign 1.0

#
# Tab Bar
#

style _color_picker_tab_bar:
    spacing 0

style _color_picker_tab:
    padding (25, 10)

style _color_picker_tab_deselected:
    is _color_picker_tab
    background "#1f1f1f"

style _color_picker_tab_selected:
    is _color_picker_tab
    background "#2e2c2c"

style _color_picker_tab_top_deselected:
    background gui.muted_color
    ysize 5
    padding (25, 0)

style _color_picker_tab_top_selected:
    background gui.accent_color
    ysize 5
    padding (25, 0)

style _color_picker_tab_text_deselected:
    color "#bbbbbb"

style _color_picker_tab_text_selected:
    color "#dddddd"

#
# Footer
#

style _color_picker_footer:
    spacing 653

style _color_picker_text_box:
    background "#ddd"
    xsize 172
    padding (6, 6)

style _color_picker_text_button:
    color "#ddd"
    hover_color "#888"
