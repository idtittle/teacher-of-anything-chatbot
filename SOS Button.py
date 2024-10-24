
from kivy.lang import Builder
from kivy.app import App
import webbrowser  # Import the webbrowser module

kv = '''
BoxLayout:
    orientation: 'vertical'

    Button:  # Change the button to an "SOS" button
        text: 'SOS'
        on_release: app.trigger_sos()
'''

class SosApp(App):

    def build(self):
        return Builder.load_string(kv)

    def trigger_sos(self):
        # Open the link using the webbrowser module
        webbrowser.open("https://tinyurl.com/28grjemq")

if _name_ == '_main_':
    SosApp().run()
