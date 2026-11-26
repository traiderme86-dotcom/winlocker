from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.utils import platform

# --- НАСТРОЙКИ ---
SECRET_CODE = "2407"
MINUTES = 15
SECONDS_TOTAL = MINUTES * 60

class LockerScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20
        self.remaining_seconds = SECONDS_TOTAL

        # Тексты
        self.add_widget(Label(text="ВЫ ПОПАЛИСЬ НА WINLOCKER", font_size='18sp', color=(1,0,0,1), bold=True))
        self.add_widget(Label(text="Чтобы разблокировать, напишите\nв Telegram (@Flovexy)", font_size='14sp', color=(1,1,1,1)))
        
        # Поле ввода (сразу на экране)
        self.pwd = TextInput(hint_text="Введите пароль", password=True, multiline=False, size_hint=(0.8, None), height=50, pos_hint={'center_x': 0.5})
        self.pwd.bind(on_text_validate=self.check_password)
        self.add_widget(self.pwd)
        
        # Текст ошибки (скрыт)
        self.error_label = Label(text="", color=(1,0,0,1), font_size='12sp')
        self.add_widget(self.error_label)
        
        # Таймер
        self.timer_label = Label(text="ДО ВАШЕЙ МУЧИТЕЛЬНОЙ СМЕРТИ ОСТАЛОСЬ:\n15:00", font_size='14sp', color=(1,0,0,1))
        self.add_widget(self.timer_label)

        Clock.schedule_interval(self.update_timer, 1)

    def check_password(self, instance):
        if instance.text == SECRET_CODE:
            App.get_running_app().stop() # Закрываем при верном пароле
        else:
            self.error_label.text = "ЗАМЕЧЕНО: НЕПРАВИЛЬНЫЙ ВВОД ПАРОЛЯ\nПРЕДОТВРАЩЕНИЕ WINLOCKER ОШИБКА"
            Clock.schedule_once(self.clear_error, 3)
            instance.text = ""

    def clear_error(self, dt):
        self.error_label.text = ""

    def update_timer(self, dt):
        if self.remaining_seconds <= 0:
            App.get_running_app().stop() # Закрываем по таймеру
            return False
        mins = self.remaining_seconds // 60
        secs = self.remaining_seconds % 60
        self.timer_label.text = f"ДО ВАШЕЙ МУЧИТЕЛЬНОЙ СМЕРТИ ОСТАЛОСЬ:\n{mins:02d}:{secs:02d}"
        self.remaining_seconds -= 1
        return True

class LockerApp(App):
    def build(self):
        return LockerScreen()

if __name__ == '__main__':
    LockerApp().run()