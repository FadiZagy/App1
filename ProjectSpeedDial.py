from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, SwapTransition, NoTransition, CardTransition, SlideTransition, \
    WipeTransition, FadeTransition, FallOutTransition, RiseInTransition
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivy.core.window import Window

Window.size = (310, 580)


class ScreenManagerr(ScreenManager):
    pass

class addd(MDScreen):
    def presss(self):
        self.manager.current = "feedback"
        self.manager.transition.direction = "down"




class Calculator(MDScreen):

    def clear(self):
        self.ids.text_id.text = "0"


    def number(self, number):

        if "Error" in self.ids.text_id.text:
            self.ids.text_id.text = f''

        if self.ids.text_id.text == "0":
            self.ids.text_id.text = ""
            data = self.ids.text_id.text
            self.ids.text_id.text = f'{data}{str(number)}'
        else:
            data = self.ids.text_id.text
            self.ids.text_id.text = f'{data}{str(number)}'

    def sign(self, sign):
        data = self.ids.text_id.text
        self.ids.text_id.text = f'{data}{sign}'

    def math(self):
        data = self.ids.text_id.text
        try:
            answer = eval(data)  # eval() to evaluate the math
            self.ids.text_id.text = f'{answer}'

        except:
            self.ids.text_id.text = f'Error'

    def dot(self):

        data = self.ids.text_id.text
        if "+" in data and "." not in data[-1]:  # get the last letter [-1]
            self.ids.text_id.text = f'{data}.'
        elif "." in data:
            pass
        else:
            self.ids.text_id.text = f'{data}.'

    def remove(self):

        data = self.ids.text_id.text
        remove = data[:-1]  # removed the last letter [:-1]
        self.ids.text_id.text = f'{remove}'

    def minis(self):
        data = self.ids.text_id.text
        if "-" in data:

            self.ids.text_id.text = f'{data.replace("-", "")}'
        else:
            self.ids.text_id.text = f'-{data}'
class FeedBack(MDScreen):
    def open(self):

        if not self.manager.has_screen('add_screen'):
            self.manager.add_widget(addd(name='add_screen'))
        self.manager.current = 'add_screen'
        self.manager.transition.direction = "up"






class FadiApp(MDApp):
    def build(self):
        self.icon = "User.png"
        # Load KV files
        self.root = Builder.load_file("screenmanager.kv")
        Builder.load_file("calculator.kv")
        Builder.load_file("feedback.kv")
        Builder.load_file("addd.kv")
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        # Add Screens to screen manager
        self.root.ids.screen_manager.transition = SlideTransition()

        self.root.ids.screen_manager.add_widget(Calculator(name='calculator'))
        self.root.ids.screen_manager.add_widget(FeedBack(name='feedback'))


        return self.root

    def on_start(self):
        super().on_start()
        self.root.ids.speed_dial.data = {
            'Calculator': ['calculator',
                           "on_press", lambda x: self.calculator_callback()],  # icon name
            'Feedback': ['comment-quote',
                         "on_press", lambda x: self.feedback_callback()]  # icon name
        }

    def calculator_callback(self):
        self.theme_cls.theme_style = "Light"
        self.root.ids.screen_manager.current = "calculator"
        self.root.ids.screen_manager.transition.duration = 0.20
        self.root.ids.screen_manager.transition.direction = "right"

    def feedback_callback(self):
        self.theme_cls.theme_style = "Light"
        self.root.ids.screen_manager.current = "feedback"
        self.root.ids.screen_manager.transition.duration = 0.20
        self.root.ids.screen_manager.transition.direction = "left"


if __name__ == "__main__":
    FadiApp().run()
