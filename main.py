from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen

kv='''

Manager:
    Fir:

<Fir>:
    MDLabel:
        id:l1
        text:'JAI MAHAKAL'
        pos_hint:{'center_x':0.8,'center_y':0.8}
    
    MDRectangleFlatButton:
        text:'HAR HAR MAHADEV'
        pos_hint:{"center_x":0.5,"center_y":0.5}
        on_press:
            l1.text=self.text            

'''

class Fir(Screen):
    pass

class Manager(ScreenManager):
    pass
    

class Demo(MDApp):
    def build(self):
        self.bu=Builder.load_string(kv)
        return self.bu
        
Demo().run()
        