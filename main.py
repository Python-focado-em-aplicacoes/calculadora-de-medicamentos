from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MedicationCalculatorApp(App):
    def build(self):
        self.title = "Calculadora de Medicamentos"
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Título
        title_label = Label(text="Calculadora de Medicamentos", font_size=24)
        layout.add_widget(title_label)
        
        # Entrada do Nome do Medicamento
        self.med_name_input = TextInput(hint_text="Nome do Medicamento", font_size=18)
        layout.add_widget(self.med_name_input)
        
        # Entrada da Dose por Unidade
        self.dose_per_unit_input = TextInput(hint_text="Dose por Unidade (mg)", font_size=18)
        layout.add_widget(self.dose_per_unit_input)
        
        # Entrada da Dose Prescrita
        self.prescribed_dose_input = TextInput(hint_text="Dose Prescrita (mg)", font_size=18)
        layout.add_widget(self.prescribed_dose_input)
        
        # Botão para Calcular
        calculate_button = Button(text="Calcular", font_size=20, size_hint_y=None, height=50)
        calculate_button.bind(on_press=self.calculate_dose)
        layout.add_widget(calculate_button)
        
        # Resultado
        self.result_label = Label(text="", font_size=20)
        layout.add_widget(self.result_label)
        
        return layout
    
    def calculate_dose(self, instance):
        try:
            dose_per_unit = float(self.dose_per_unit_input.text)
            prescribed_dose = float(self.prescribed_dose_input.text)
            quantity = prescribed_dose / dose_per_unit
            self.result_label.text = f"Quantidade necessária: {quantity:.2f} unidades"
        except ValueError:
            self.result_label.text = "Por favor, insira valores válidos."

if __name__ == "__main__":
    MedicationCalculatorApp().run()
