from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock

from win10toast import ToastNotifier

class UpdateableNotificationApp(App):
    def build(self):
        self.timer_count = 10  # Set the initial timer count in seconds
        self.button = Button(text='Send Notification', on_press=self.send_notification)
        self.notifier = ToastNotifier()
        return self.button

    def send_notification(self, instance):
        self.update_notification()  # Initial notification
        self.schedule_notification_updates()

    def update_notification(self, dt=None):
        self.notifier.show_toast("Updateable Notification",
                                 f"Timer: {self.timer_count} seconds remaining",
                                 duration=1)  # Set a short duration for each update

        if self.timer_count <= 0:
            self.notifier.show_toast("Updateable Notification",
                                     "Timer finished!",
                                     duration=5)  # Set a longer duration for the final notification
            return False

        self.timer_count -= 1

    def schedule_notification_updates(self):
        Clock.schedule_interval(self.update_notification, 1)  # Schedule updates every second

if __name__ == '__main__':
    UpdateableNotificationApp().run()
