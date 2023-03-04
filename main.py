from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout


class check_box(GridLayout):

    def __init__(self, **kwargs):
        super(check_box, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text='Male'))
        self.active = CheckBox(active=True)
        self.add_widget(self.active)

        self.lbl_active = Label(text='Checkbox is on')
        self.add_widget(self.lbl_active)

        self.active.bind(active=self.on_checkbox_Active)

    def on_checkbox_Active(self, checkboxInstance, isActive):
        if isActive:
            self.lbl_active.text = "Checkbox is ON"
            print("Checkbox Checked")
        else:
            self.lbl_active.text = "Checkbox is OFF"
            print("Checkbox unchecked")


class CheckBoxApp(App):
    def build(self):

        return check_box()


# Run the app
if __name__ == '__main__':
    CheckBoxApp().run()
