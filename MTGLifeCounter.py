import os
import json
import webbrowser
import random
from kivy.app import App
from kivy.base import EventLoop
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.graphics import Rectangle
from kivy.graphics.texture import Texture
from functools import partial
from kivy.uix.filechooser import FileChooser
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.filechooser import FileChooserIconView
from kivy.graphics import Color

from MTGKeywords import keywords
from MTGKeywords import keywords_favorites


class MTGLifeCounter(App):
    player_name = 'Planeswalker'

    player_health = 40
    player_health_bool = True

    commander_health = 21
    commander_health_bool = False

    # -------------------- Save/Load - WORK IN PROGRESS --------------------

    def __init__(self, **kwargs):
        super(MTGLifeCounter, self).__init__(**kwargs)
        self.data_file = "data.json"
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.player_name = data.get('player_name', self.player_name)
                self.player_health = data.get('player_health', self.player_health)
                self.player_health_bool = data.get('player_health_bool', self.player_health_bool)
                self.commander_health = data.get('commander_health', self.commander_health)
                self.commander_health_bool = data.get('commander_health_bool', self.commander_health_bool)

    # can use this as a reference later to save commander_tax and mana_counters
    def save_data(self):
        data = {
            'player_name': self.player_name,
            'player_health': self.player_health,
            'player_health_bool': self.player_health_bool,
            'commander_health': self.commander_health,
            'commander_health_bool': self.commander_health_bool
        }
        with open(self.data_file, 'w') as file:
            json.dump(data, file)

    def on_stop(self):
        self.save_data()

    def on_start(self):
        self.load_data()

    # -------------------- Build the App --------------------

    def build(self):
        # Set the window size to fullscreen
        Window.fullscreen = 'auto'

        # Get the path of the "Images" folder
        images_folder = 'Images'

        # Get a list of all files in the "Images" folder
        files = os.listdir(images_folder)

        # Filter out non-image files (optional)
        image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png'))]

        # Select the first image in the list
        if image_files:
            random_image = random.choice(image_files)

            # Create an Image widget and load the image from the "Images" folder
            self.image = Image(source=os.path.join(images_folder, random_image), allow_stretch=True, keep_ratio=False)

            # Create a counter variables to keep track of the number of clicks
            self.click_counter_plus = 0
            self.click_counter_minus = 0

            # Create references to the scheduled reset timer
            self.reset_timer_plus = None
            self.reset_timer_minus = None

            # Create a BoxLayout as the root layout
            root_layout = GridLayout(cols=1)

            # Create a RelativeLayout to contain the Image widget and labels
            layout = RelativeLayout(size_hint=(1, 0.7))

            # Create an Image widget and load the image from the "Images" folder
            image = Image(source=os.path.join(images_folder, random_image), allow_stretch=True, keep_ratio=False)

            # Bind the on_touch_down event to a callback function
            image.bind(on_touch_down=self.on_image_touch)


            # Create labels for the main interface (player, commander, plus/minus, name)
            # you can change X in while ***** .canvas Color(0,0,0,X) to increase or decrease opaque/fade
            # Create a dark background for the player name label
            player_name_label = Label(
                text=str(self.player_name), font_size=200, size_hint=(None, None),
                pos_hint={'center_x': 0.5, 'center_y': 0.9}, color=(0.9, 0.9, 0.9, 1)
            )
            # alternative color code: color=get_color_from_hex('#5b7575')


            # Create a dark background for the player health label
            player_health_background = RelativeLayout(size_hint=(None, None), size=(250, 180),
                                                      pos_hint={'center_x': 0.5, 'center_y': 0.55})
            with player_health_background.canvas:
                Color(0, 0, 0, .0)
                self.player_health_background_rect = Rectangle(pos=player_health_background.pos,
                                                               size=player_health_background.size)
            player_health_label = Label(
                text=str(self.player_health), font_size=200, size_hint=(None, None),
                pos_hint={'center_x': 0.5, 'center_y': 0.55}, color=(1, 1, 1, 1)
            )
            player_health_background.add_widget(player_health_label)


            # Create a dark background for the commander health label
            commander_health_background = RelativeLayout(size_hint=(None, None), size=(225, 150),
                                                         pos_hint={'center_x': 0.5, 'center_y': 0.45})
            with commander_health_background.canvas:
                Color(0, 0, 0, 0)
                self.commander_health_background_rect = Rectangle(pos=commander_health_background.pos,
                                                                  size=commander_health_background.size)
            commander_health_label = Label(
                text=str(self.commander_health), font_size=150, size_hint=(None, None),
                pos_hint={'center_x': 0.5, 'center_y': 0.45}, color=(1, 1, 1, 1)
            )
            commander_health_background.add_widget(commander_health_label)


            plus_label = Label(
                text=str('+'), font_size=150, size_hint=(None, None),
                pos_hint={'center_x': 0.9, 'center_y': 0.5}
            )
            minus_label = Label(
                text=str('-'), font_size=150, size_hint=(None, None),
                pos_hint={'center_x': 0.1, 'center_y': 0.5}
            )
            temp_plus_label = Label(
                text=str(''), font_size=100, size_hint=(None, None),
                pos_hint={'center_x': 0.65, 'center_y': 0.5}
            )
            temp_minus_label = Label(
                text=str(''), font_size=100, size_hint=(None, None),
                pos_hint={'center_x': 0.35, 'center_y': 0.5}
            )

            # Add the image and labels to the layout
            layout.add_widget(image)
            layout.add_widget(player_name_label)
            layout.add_widget(player_health_background)
            layout.add_widget(commander_health_background)
            layout.add_widget(plus_label)
            layout.add_widget(minus_label)
            layout.add_widget(temp_plus_label)
            layout.add_widget(temp_minus_label)

            # Create a layout for the button row
            button_row_layout = BoxLayout(orientation='horizontal', size_hint=(1, None),
                                          height=Window.height * 0.2)

            # Create buttons and add them to the button row, then bind their methods/functions
            button1 = Button(text='Dictionary')
            button1.bind(on_release=self.open_window_keywords)  # Bind on_release event to open_window_keywords function
            button2 = Button(text='Change Health')
            button2.bind(on_release=self.update_health_counter_button)
            button3 = Button(text='Extra')
            button3.bind(on_release=self.open_window_extra)
            button4 = Button(text='Options')
            button4.bind(on_release=self.open_options_popup)
            button_row_layout.add_widget(button1)
            button_row_layout.add_widget(button2)
            button_row_layout.add_widget(button3)
            button_row_layout.add_widget(button4)

            # Add the layout and button row to the root layout
            root_layout.add_widget(layout)
            root_layout.add_widget(button_row_layout)

            # Assign main interface labels as an instance variable
            self.player_health_label = player_health_label
            self.commander_health_label = commander_health_label
            self.temp_plus_label = temp_plus_label
            self.temp_minus_label = temp_minus_label
            self.player_name_label = player_name_label

            # Bind the on_key_down event to a callback function
            EventLoop.window.bind(on_key_down=self.close_application)

            return root_layout
        else:
            print("No images found in the 'Images' folder.")

    def update_health_background(self, instance, value):
        self.health_background.pos = instance.pos
        self.health_background.size = instance.size

    # -------------------- Options Interface --------------------

    def open_options_popup(self, instance):
        # Create a BoxLayout for the popup content
        content_layout = BoxLayout(orientation='vertical', spacing=10)

        # Create buttons for "Change Name" and "Change Background"
        change_name_button = Button(text='Change Name')
        change_name_button.bind(on_release=self.change_name)  # Bind on_release event to change_name function

        # Add buttons to the content layout
        content_layout.add_widget(change_name_button)

        # Create a Popup with the content layout
        popup = Popup(title='Options', content=content_layout, size_hint=(None, None), size=(300, 200))
        popup.open()

    def change_name(self, instance):
        # Create a TextInput widget for user input
        text_input = TextInput(text=self.player_name, size_hint=(None, None), size=(300, 100))

        # Create a function for updating the player name based on the input
        def update_name(instance):
            self.player_name = text_input.text
            self.player_name_label.text = str(self.player_name)  # Update the player name label
            popup.dismiss()

        # Create a button for confirming the name change
        confirm_button = Button(text='Confirm', on_release=update_name)

        # Create a BoxLayout to contain the TextInput and Confirm button
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(text_input)
        layout.add_widget(confirm_button)

        # Create a Popup with the layout
        popup = Popup(title='Change Name', content=layout, size_hint=(None, None), size=(600, 300))
        popup.open()

    # -------------------- Extras Interface --------------------

    def open_window_extra(self, instance):
        # Create the layouts for the popup window
        popup_layout = BoxLayout(orientation='vertical', spacing=20, padding=20)  # Root layout for the popup

        # commander layout ----
        # Create the commander tax layout
        commander_tax_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=100, spacing=10)

        # Create the label for the commander tax
        commander_tax_label = Label(text='Commander Tax: Two Colorless per One Counter', size_hint=(0.4, 1),
                                    halign='right', valign='middle', font_size=50)
        commander_tax_layout.add_widget(commander_tax_label)

        # Create the label for the commander tax value
        commander_tax_value_label = Label(text='0', size_hint=(0.1, 1), halign='center', valign='middle', font_size=50)
        commander_tax_layout.add_widget(commander_tax_value_label)

        # Create the buttons for increasing and decreasing the commander tax
        commander_tax_increase_button = Button(text='+', on_release=partial(self.increase_commander_tax,
                                                                            commander_tax_value_label),
                                               size_hint=(0.2, 1), font_size=50)
        commander_tax_decrease_button = Button(text='-', on_release=partial(self.decrease_commander_tax,
                                                                            commander_tax_value_label),
                                               size_hint=(0.2, 1), font_size=50)
        commander_tax_layout.add_widget(commander_tax_increase_button)
        commander_tax_layout.add_widget(commander_tax_decrease_button)

        # mana layout ----
        # Create the mana counter layout
        mana_counter_layout = GridLayout(cols=6, size_hint=(1, 0.6), spacing=10)

        # Create the widgets for the mana counter layout
        mana_counter_label = Label(text='Mana Counter', size_hint=(1, None), height=50, halign='center',
                                   valign='middle',
                                   font_size=30)
        mana_counter_layout.add_widget(mana_counter_label)

        # rules layout ----
        rules_layout = BoxLayout(orientation='vertical', spacing=20, padding=20)

        # Create the label for the rules layout
        rules_label = Label(text='Click the button below to view the rules', size_hint=(1, None), height=50,
                            halign='center',
                            valign='middle', font_size=30)
        rules_layout.add_widget(rules_label)

        # Create the button for opening the rules link
        rules_button = Button(text='View Rules', on_release=self.open_rules_link, size_hint=(1, None), height=50,
                              font_size=30)
        rules_layout.add_widget(rules_button)


        # Create a layout for each color
        colors = ['White', 'Black', 'Blue', 'Red', 'Green']
        mana_labels = {}  # Dictionary to store mana labels by color
        for color in colors:
            color_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.6), height=80, spacing=5)

            # Create a label for the color
            color_label = Label(text=color, size_hint=(1, 0.4), halign='center', valign='middle', font_size=50)
            color_layout.add_widget(color_label)

            # Create a label for the mana value and add it to the color layout
            mana_label = Label(text='0', size_hint=(1, 0.4), halign='center', valign='middle', font_size=50)
            color_layout.add_widget(mana_label)
            mana_labels[color] = mana_label  # Store mana label for later access

            # Create buttons for adding and removing mana
            button_layout = BoxLayout(size_hint=(1, 0.2), spacing=5)

            add_button = Button(text='+', on_release=partial(self.add_mana, color, mana_label),
                                size_hint=(None, None), size=(150, 80), font_size=50)
            remove_button = Button(text='-', on_release=partial(self.remove_mana, color, mana_label),
                                   size_hint=(None, None), size=(150, 80), font_size=50)

            button_layout.add_widget(add_button)
            button_layout.add_widget(remove_button)

            color_layout.add_widget(button_layout)
            mana_counter_layout.add_widget(color_layout)

        # Create a layout for the reset button
        reset_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=60, spacing=10)

        # Create the reset button and bind it to the reset_mana method
        reset_button = Button(text='Reset', on_release=partial(self.reset_mana, mana_labels), size_hint=(0.5, 1),
                              font_size=24)
        reset_layout.add_widget(reset_button)

        # Add the layouts to the popup layout
        popup_layout.add_widget(commander_tax_layout)
        popup_layout.add_widget(mana_counter_layout)
        popup_layout.add_widget(reset_layout)
        popup_layout.add_widget(rules_layout)

        # Create the popup window
        popup = Popup(title='Extra Window', content=popup_layout, size_hint=(0.8, 0.8))

        # Open the popup window
        popup.open()

    def add_mana(self, color, mana_label, button):
        # Handle adding mana for the given color
        current_mana = int(mana_label.text)
        current_mana += 1
        mana_label.text = str(current_mana)

    def remove_mana(self, color, mana_label, button):
        # Handle removing mana for the given color
        current_mana = int(mana_label.text)
        if current_mana > 0:
            current_mana -= 1
            mana_label.text = str(current_mana)

    def reset_mana(self, mana_labels, button):
        # Reset all mana labels to 0
        for mana_label in mana_labels.values():
            mana_label.text = '0'

    def increase_commander_tax(self, commander_tax_label, button):
        current_tax = int(commander_tax_label.text)
        current_tax += 1
        commander_tax_label.text = str(current_tax)

    def decrease_commander_tax(self, commander_tax_label, button):
        current_tax = int(commander_tax_label.text)
        if current_tax > 0:
            current_tax -= 1
            commander_tax_label.text = str(current_tax)

    def open_rules_link(self, instance):
        import webbrowser
        webbrowser.open("https://magic.wizards.com/en/how-to-play")

    # -------------------- Life Counters // Main Screen --------------------

    def on_image_touch(self, instance, touch):
        if touch.x < instance.width / 2:
            # Left side clicked
            print("Left side clicked")
            if self.player_health_bool:

                # check if other label is counting, if so cancel it
                if self.click_counter_plus > 0:
                    self.reset_temp_plus_label()
                    if self.reset_timer_plus is not None:
                        self.reset_timer_plus.cancel()
                else:
                    pass

                self.player_health -= 1

                # Update the player health label text
                self.player_health_label.text = str(self.player_health)

                # Increment the click counter
                self.click_counter_minus -= 1

                # Update the temporary plus label with the click count
                self.temp_minus_label.text = '{}'.format(self.click_counter_minus)

                # Cancel any existing reset timer
                if self.reset_timer_minus is not None:
                    self.reset_timer_minus.cancel()

                # Schedule the reset_temp_plus_label method after 5 seconds
                self.reset_timer_minus = Clock.schedule_once(lambda dt: self.reset_temp_minus_label(), 4)
            else:
                # check if other label is counting, if so cancel it
                if self.click_counter_plus > 0:
                    self.reset_temp_plus_label()
                    if self.reset_timer_plus is not None:
                        self.reset_timer_plus.cancel()

                self.commander_health -= 1

                # Update the player health label text
                self.commander_health_label.text = str(self.commander_health)

                # Increment the click counter
                self.click_counter_minus -= 1

                # Update the temporary plus label with the click count
                self.temp_minus_label.text = '{}'.format(self.click_counter_minus)

                # Cancel any existing reset timer
                if self.reset_timer_minus is not None:
                    self.reset_timer_minus.cancel()

                # Schedule the reset_temp_plus_label method after 5 seconds
                self.reset_timer_minus = Clock.schedule_once(lambda dt: self.reset_temp_minus_label(), 4)
        else:
            # Right side clicked
            print("Right side clicked")
            if self.player_health_bool:

                # check if other label is counting, if so cancel it
                if self.click_counter_minus < 0:
                    self.reset_temp_minus_label()
                    if self.reset_timer_minus is not None:
                        self.reset_timer_minus.cancel()
                else:
                    pass

                self.player_health += 1

                # Update the player health label text
                self.player_health_label.text = str(self.player_health)

                # Increment the click counter
                self.click_counter_plus += 1

                # Update the temporary plus label with the click count
                self.temp_plus_label.text = '+{}'.format(self.click_counter_plus)

                # Cancel any existing reset timer
                if self.reset_timer_plus is not None:
                    self.reset_timer_plus.cancel()

                # Schedule the reset_temp_plus_label method after 5 seconds
                self.reset_timer_plus = Clock.schedule_once(lambda dt: self.reset_temp_plus_label(), 4)
            else:
                if self.click_counter_minus < 0:
                    self.reset_temp_minus_label()
                    if self.reset_timer_minus is not None:
                        self.reset_timer_minus.cancel()
                else:
                    pass

                self.commander_health += 1

                # Update the player health label text
                self.commander_health_label.text = str(self.commander_health)

                self.click_counter_plus += 1

                # Update the temporary plus label with the click count
                self.temp_plus_label.text = '+{}'.format(self.click_counter_plus)

                # Cancel any existing reset timer
                if self.reset_timer_plus is not None:
                    self.reset_timer_plus.cancel()

                # Schedule the reset_temp_plus_label method after 5 seconds
                self.reset_timer_plus = Clock.schedule_once(lambda dt: self.reset_temp_plus_label(), 4)

    def update_health_counter_button(self, instance):

        if self.player_health_bool:
            self.player_health_bool = False
            self.commander_health_bool = True
        else:
            self.player_health_bool = True
            self.commander_health_bool = False

    def update_temp_plus_label(self, duration):
        self.temp_plus_label.text = ''
        Clock.schedule_once(lambda dt: self.reset_temp_plus_label(), duration)

    def reset_temp_plus_label(self):
        # Reset the click counter to 0
        self.click_counter_plus = 0

        # Reset the temporary plus label
        self.temp_plus_label.text = ''

        # Reset the reset timer reference
        self.reset_timer_plus = None

    def update_temp_minus_label(self, duration):
        self.temp_minus_label.text = ''
        Clock.schedule_once(lambda dt: self.reset_temp_minus_label(), duration)

    def reset_temp_minus_label(self):
        # Reset the click counter to 0
        self.click_counter_minus = 0

        # Reset the temporary plus label
        self.temp_minus_label.text = ''

        # Reset the reset timer reference
        self.reset_timer_minus = None

    # -------------------- Keywords Interface --------------------

    def open_window_keywords(self, instance):
        # sort keywords list in order
        keywords.sort()

        # Create the popup
        popup = Popup(
            title='Keyword Dictionary',
            background_color=(0.9, 0.9, 0.9, 0.9),
            size_hint=(None, None),
            size=(Window.width * 0.8, Window.height * 0.8),
            auto_dismiss=True
        )

        # Create a BoxLayout to hold the entire content
        content_layout = BoxLayout(orientation='vertical')

        # Create a ScrollView and add it to the content layout
        scroll_view = ScrollView(
            bar_width=30,
            scroll_type=['bars'],
            bar_color=get_color_from_hex('#5b7575'),
            bar_inactive_color=get_color_from_hex('#5b7575'),
            effect_cls='ScrollEffect',
            do_scroll_y=True,
            do_scroll_x=False
        )
        content_layout.add_widget(scroll_view)

        # Create a BoxLayout to hold the labels
        labels_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        labels_layout.bind(minimum_height=labels_layout.setter('height'))

        # Add labels for each item in the keyword list
        for keyword in keywords:
            # Create a Label widget with formatted text for the keyword
            formatted_keyword = f"{keyword}"
            label_keyword = Label(
                text=formatted_keyword,
                size_hint_y=None,
                font_size=60,
                height=40,
                markup=True,
                halign='left',
                text_size=(None, None)  # Disable the default text size
            )
            label_keyword.bind(
                width=lambda instance, value: instance.setter('text_size')(instance, (value, None))
            )
            label_keyword.bind(
                texture_size=lambda instance, value: instance.setter('size')(instance, value)
            )
            labels_layout.add_widget(label_keyword)

            # Create a Label widget for the description with a font size of 30 and not bold
            label_description = Label(
                text='',
                size_hint_y=None,
                height=10,
                font_size=30,
                bold=False,
                halign='left',
                text_size=(None, None)  # Disable the default text size
            )
            label_description.bind(
                width=lambda instance, value: instance.setter('text_size')(instance, (value, None))
            )
            label_description.bind(
                texture_size=lambda instance, value: instance.setter('size')(instance, value)
            )
            labels_layout.add_widget(label_description)

        # Add the labels layout to the scroll view
        scroll_view.add_widget(labels_layout)

        # Create a BoxLayout for the buttons
        buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=Window.height * 0.2)

        # Create the buttons and add them to the buttons layout // not fully implemented yet // favorites/regular list
        # button1 = Button(text='KEYWORDS', size_hint=(0.3, 0.5))
        # button2 = Button(text='FAVORITES', size_hint=(0.3, 0.5))
        # buttons_layout.add_widget(button1)
        # buttons_layout.add_widget(button2)

        # Add the buttons layout to the content layout
        content_layout.add_widget(buttons_layout)

        # Assign the content layout as the content of the popup
        popup.content = content_layout

        # Open the popup
        popup.open()

    # -------------------- App Code --------------------

    def close_application(self, window, key, *args):
        if key == 27:  # Escape key
            App.get_running_app().stop()


if __name__ == '__main__':
    MTGLifeCounter().run()
