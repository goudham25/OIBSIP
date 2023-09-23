from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class CalculatorApp(App):
    def build(self):
  
        main_layout = BoxLayout(orientation='vertical')
        # Equation label
        equation_label = Label(font_size=40, halign='right', valign='middle', size_hint=(1, 0.2))
        main_layout.add_widget(equation_label)

        # Result label
        result_label = Label(font_size=50, halign='right', valign='middle', size_hint=(1, 0.2))
        main_layout.add_widget(result_label)

        # Buttons
        button_layout = GridLayout(cols=4, size_hint=(1, 0.6))
        buttons = [
            'AC', 'DEL', '+/-', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '%', '0', '.', '='
        ]

        # Button_click function
        for button_text in buttons:
            button = Button(text=button_text, pos_hint={'center_x': 0.5, 'center_y': 0.5}, on_release=self.button_release)
            button_layout.add_widget(button)

        main_layout.add_widget(button_layout)
        self.equation_label = equation_label
        self.result_label = result_label

        return main_layout

    def button_release(self, instance):
        button_text = instance.text

        if button_text == '=':
            try:
                result = str(eval(self.equation_label.text))
                self.result_label.text = result
            except Exception:
                self.result_label.text = 'Error'
            finally:
                self.equation_label.text = ''

        elif button_text == 'AC':
            self.equation_label.text = ''
            self.result_label.text = ''

        elif button_text == '%':
            equation = self.equation_label.text
            if equation == '':
                return
            percentage = float(equation) / 100
            self.equation_label.text = str(percentage)

        elif button_text == '.':
            equation = self.equation_label.text
            if '.' in equation:
             return
            self.equation_label.text += '.'

        elif button_text == '+/-':
            equation = self.equation_label.text

            if equation == '':
                return
            last_char = equation[-1]

            if last_char.isdigit():
                num = int(equation)
                num *= -1
                self.equation_label.text = str(num)

        elif button_text == 'DEL':
            equation = self.equation_label.text
            
            if equation == '':
                return
            equation = equation[:-1]
            self.equation_label.text = equation

        else:
            current_equation = self.equation_label.text
            new_equation = current_equation + button_text
            self.equation_label.text = new_equation

if __name__ == '__main__':
    CalculatorApp().run()
