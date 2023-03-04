from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.label import Label


class QuizApp(App):

    def build(self):
        self.questions = [
            {'question': 'What is the capital of France?', 'options': [
                'Paris', 'London', 'Berlin'], 'answer': 'Paris'},
            {'question': 'What is the highest mountain in the world?', 'options': [
                'Mount Everest', 'Mount Kilimanjaro', 'Mount Fuji'], 'answer': 'Mount Everest'},
            {'question': 'What is the smallest planet in the solar system?',
                'options': ['Mercury', 'Venus', 'Mars'], 'answer': 'Mercury'}
        ]
        self.index = 0

        layout = BoxLayout(orientation='vertical')
        self.question_label = Label(
            text=self.questions[self.index]['question'], size_hint=(1, 0.5))
        layout.add_widget(self.question_label)

        self.checkbox_layout = BoxLayout(orientation='vertical')
        self.checkboxes = []
        for option in self.questions[self.index]['options']:
            new_box = BoxLayout(orientation='horizontal')
            labe = Label(text=option)
            checkbox = CheckBox(group='options')
            new_box.add_widget(labe)
            new_box.add_widget(checkbox)
            self.checkboxes.append(checkbox)
            self.checkbox_layout.add_widget(new_box)
        layout.add_widget(self.checkbox_layout)

        self.submit_button = Button(text='Submit answer', size_hint=(1, 0.2))
        self.submit_button.bind(on_press=self.submit_answer)
        layout.add_widget(self.submit_button)

        return layout

    def submit_answer(self, instance):
        selected_option = ''
        for checkbox in self.checkboxes:
            if checkbox.active:
                # selected_option = checkbox.label
                break
        if selected_option == self.questions[self.index]['answer']:
            self.question_label.text = 'Correct!'
        else:
            self.question_label.text = 'Incorrect!'
        self.next_question()

    def next_question(self):
        self.index += 1
        if self.index == len(self.questions):
            self.index = 0
        self.question_label.text = self.questions[self.index]['question']
        for checkbox in self.checkboxes:
            self.checkbox_layout.remove_widget(checkbox)
        self.checkboxes = []
        for option in self.questions[self.index]['options']:
            checkbox = CheckBox(group='options')
            self.checkboxes.append(checkbox)
            self.checkbox_layout.add_widget(checkbox)


if __name__ == '__main__':
    QuizApp().run()
