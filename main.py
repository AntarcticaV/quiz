from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config


class QuizApp(App):

    def build(self):
        self.questions = ['What color is the sky?',
                          'What is 2+2?', 'What is the capital of France?']
        self.answers = ['blue', '4', 'Paris']
        self.index = 0

        layout = BoxLayout(orientation='vertical')
        self.question_label = Label(
            text=self.questions[self.index], size_hint=(1, 0.5))
        layout.add_widget(self.question_label)

        self.answer_button = Button(text='Show answer', size_hint=(1, 0.2))
        self.answer_button.bind(on_press=self.show_answer)
        layout.add_widget(self.answer_button)

        self.next_button = Button(text='Next question', size_hint=(1, 0.2))
        self.next_button.bind(on_press=self.next_question)
        layout.add_widget(self.next_button)

        return layout

    def show_answer(self, instance):
        self.question_label.text = self.answers[self.index]

    def next_question(self, instance):
        self.index += 1
        if self.index == len(self.questions):
            self.index = 0
        self.question_label.text = self.questions[self.index]


if __name__ == '__main__':
    Config.set("graphics", "resizable", 0)
    Config.set("graphics", "width", 360)
    Config.set("graphics", "height", 800)
    Config.write()
    QuizApp().run()
