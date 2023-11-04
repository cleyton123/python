# Importe os módulos necessários do Kivy e outros módulos relevantes
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import psutil



# Classe principal do aplicativo
class BatteryMonitorApp(App):
    def build(self):
        # Defina a estrutura da interface de usuário com um layout BoxLayout vertical
        layout = BoxLayout(orientation='vertical')

        # Adicione um rótulo à interface de usuário
        layout.add_widget(Label(text='Monitor de Bateria do Notebook'))

        # Crie um rótulo para exibir o nível da bateria
        self.battery_label = Label(text='Bateria: N/A')
        layout.add_widget(self.battery_label)

        # Adicione um botão à interface de usuário
        start_button = Button(text='Iniciar Monitoramento')
        start_button.bind(on_release=self.start_monitor)
        layout.add_widget(start_button)

        return layout

    # Função para iniciar o monitoramento da bateria
    def start_monitor(self, instance):
        # Agende a atualização do nível da bateria a cada 5 segundos
        Clock.schedule_interval(self.update_battery, 5)

    # Função para atualizar o nível da bateria
    def update_battery(self, dt):
        battery = psutil.sensors_battery()
        if battery is not None:
            percent = battery.percent
            # Atualize o rótulo com o novo nível da bateria
            self.battery_label.text = f'Bateria: {percent}%'
        else:
            self.battery_label.text = 'Bateria: N/A (ou não suportada)'

# Executar o aplicativo quando este arquivo é executado
if __name__ == '__main__':
    BatteryMonitorApp().run()
