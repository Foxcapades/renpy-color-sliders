screen color_picker():
    default hsl_picker = HSLPicker(_color_picker_color)
    default rgb_picker = RGBPicker(_color_picker_color)
    default tabs = [ "RGB", "HSL" ]

    frame:
        modal True
        style "_color_picker_backdrop"

        frame:
            style "_color_picker_container"

            vbox:
                use _color_picker_tab_bar(tabs)

                frame:
                    style "_color_picker_body"

                    if _color_picker_tab == "HSL":
                        use _color_picker_hsl_body(hsl_picker)
                    elif _color_picker_tab == "RGB":
                        use _color_picker_rgb_body(rgb_picker)


screen _color_picker_tab_bar(tabs):
    hbox:
        style "_color_picker_tab_bar"

        for val in tabs:
            button:
                if _color_picker_tab == val:
                    style "_color_picker_tab_selected"
                else:
                    style "_color_picker_tab_deselected"

                text val:
                    if _color_picker_tab == val:
                        style "_color_picker_tab_text_selected"
                    else:
                        style "_color_picker_tab_text_deselected"

                action SetVariable("_color_picker_tab", val)


screen _color_picker_hsl_body(bg_picker):
    default hue_value = HSLPickerInputValue(bg_picker, "hue_str", bg_picker.set_hue)
    default sat_value = HSLPickerInputValue(bg_picker, "saturation_str", bg_picker.set_saturation)
    default lig_value = HSLPickerInputValue(bg_picker, "lightness_str", bg_picker.set_lightness)
    default hex_value = HexInputValue('_color_picker_color')

    vbox:
        spacing 20

        hbox:
            spacing 20

            frame:
                style "_color_picker_preview"

            vbox:
                spacing 20

                vbox:
                    text "Hue":
                        style "_color_picker_bar_text"
                    bar:
                        style "_color_picker_bar"
                        value bg_picker.hue
                        range 359
                        changed bg_picker.set_hue
                vbox:
                    text "Saturation":
                        style "_color_picker_bar_text"
                    bar:
                        style "_color_picker_bar"
                        value bg_picker.saturation
                        range 100
                        changed bg_picker.set_saturation
                vbox:
                    text "Brightness":
                        style "_color_picker_bar_text"
                    bar:
                        style "_color_picker_bar"
                        value bg_picker.lightness
                        range 100
                        changed bg_picker.set_lightness

        use _color_picker_footer(hex_value, bg_picker)


screen _color_picker_rgb_body(bg_picker):
    default r_value = RGBPickerInputValue(bg_picker, "red", bg_picker.set_red)
    default g_value = RGBPickerInputValue(bg_picker, "green", bg_picker.set_green)
    default b_value = RGBPickerInputValue(bg_picker, "blue", bg_picker.set_blue)
    default h_value = HexInputValue('_color_picker_color')

    vbox:
        spacing 20

        hbox:
            spacing 20

            frame:
                style "_color_picker_preview"

            vbox:
                spacing 20

                vbox:
                    text "Red":
                        style "_color_picker_bar_text"
                    bar:
                        style "_color_picker_bar"
                        value bg_picker.red
                        range 255
                        changed bg_picker.set_red
                vbox:
                    text "Green":
                        style "_color_picker_bar_text"
                    bar:
                        style "_color_picker_bar"
                        value bg_picker.green
                        range 255
                        changed bg_picker.set_green
                vbox:
                    text "Blue":
                        style "_color_picker_bar_text"
                    bar:
                        style "_color_picker_bar"
                        value bg_picker.blue
                        range 255
                        changed bg_picker.set_blue

        use _color_picker_footer(h_value, bg_picker)


screen _color_picker_footer(h_value, bg_picker):
    hbox:
        style "_color_picker_footer"

        button:
            style "_color_picker_text_box"
            key_events True

            input:
                value h_value
                prefix '#'
                length 6
                copypaste True

            action h_value.Toggle()

        textbutton "Done":
            text_style "_color_picker_text_button"
            action Return(bg_picker.hex_string)
