
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from datetime import datetime
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBody
from kivymd.uix.selectioncontrol import MDCheckbox, MDSwitch
from kivymd.uix.button import MDFlatButton

Window.size = (360, 600)

class DialogContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = datetime.now().strftime("%A - %B %d, %Y")

    def on_save(self, instance, value, date_range):
        date = value.strftime("%A %B %d %Y")
        self.ids.date_text.text = str(date)

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()


class ListWithItem(TwoLineAvatarIconListItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def mark(self, check, item):
        if check.active == True:
            item.text = '[s]' + item.text + '[/s]'
        else:
            item.text = item.text.replace('[s]', '').replace('[/s]', '')

    def remove_item(self, item):
        self.parent.remove_widget(item)


class LeftCheckbox(MDCheckbox,ILeftBody):
    pass


class Confirmation(MDBoxLayout):
        pass

class TaskManagerApp(MDApp):
    task_show_dialog = None
    confirmation_show = None
    def build(self):
        self.theme_cls.primary_palette = ("Orange")

    def show_task(self):
        if not self.task_show_dialog:
            self.task_show_dialog = MDDialog(title="Select Date Bish", type="custom",
                                             radius=([20, 20, 20, 20]),
                                             content_cls=DialogContent())
            self.task_show_dialog.open()

    def add_task(self, task, task_date):
        if len(task.text) != 0:
            print(f"{task.text}, {task_date}")
            self.root.ids['container'].add_widget(ListWithItem(text="[b]"+ task.text + "[/b]",
                                                               secondary_text= task_date))
            task.text = ""
        else:
            pass

    def close_dialog(self, *args):
        self.task_show_dialog.dismiss()
        self.task_show_dialog = None


    def confirm_finish(self):
        if not self.confirmation_show:
            self.confirmation_show = MDDialog(title="Are you sure?",type='custom', content_cls=Confirmation())
            self.confirmation_show.open()


app = TaskManagerApp()
app.run()