from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty
from kivy.core.window import Window

mi_km = 1.609344


class ConverterApp(App):
    message = StringProperty()

    def build(self):
        Window.size = (500, 300)

        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.text_to_num()
        result = mi_km * value
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        miles = self.text_to_num() + change
        self.root.ids.user_input.text = str(miles)
        self.handle_calculate()

    def auto_calculate(self, miles):
        self.message = str(mi_km * miles)

    def text_to_num(self):
        try:
            return float(self.root.ids.user_input.text)
        except ValueError:
            return 0.0


ConverterApp().run()
