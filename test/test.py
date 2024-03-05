from kivymd.app import MDApp
from kivy.lang import Builder
from plyer import filechooser
from plyer import notification
from pygame.mixer import Sound
import pygame



kv = '''
MDFloatLayout:
    MDRaisedButton:
        text: "Upload Music"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_release: app.show_filechooser()
    MDRaisedButton:
        text: "Send Notifs"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_release: app.show_notif()
        
        '''
class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def show_filechooser(self):
        filechooser.open_file(filters=["*mp3", "*wav", "*aac", "*ogg"], on_selection=self.selected)

    def show_notif(self):
        notification.notify(title="DIKO ALAM", timeout= 1, message="diko alam kung pano yung di natatanggal na notifs omg", app_name="TESTING LANG")

    def selected(self, selection):
        if selection:
            if selection:
                pygame.mixer.init()
                # If a file is selected, play the sound
                sound = Sound(selection[0])
                sound.set_volume(0.5)
                sound.play(fade_ms=500)


        
app = MyApp()
app.run()

app.play_sound()