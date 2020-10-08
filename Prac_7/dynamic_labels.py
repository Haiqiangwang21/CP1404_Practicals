from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Cool", "Wool", "Pool", "Bool"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widget()
        return self.root

    def create_widget(self):
        for name in self.names:
            names = Label(text=name, id=name)
            self.root.ids.names_box.add_widget(names)


DynamicLabelsApp().run()
