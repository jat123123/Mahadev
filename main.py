from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.card import MDCard


kv='''

#:import w kivy.uix.effectwidget
Manager:
    Fir:
    Sec:        
        
<Fir>:
    name:'sc1'    
  
        
    MDBottomNavigation:
        id:bn1
        pos_hint:{'bottom':1}
        panel_color:0,1,0,1
        text_color_active:1,0,1,1
        text_color_normal:0,0,0,1
        MDBottomNavigationItem:
            name:'s1'
            icon:'home'
            text:'Home'
            Carousel:
                direction:'bottom'
                MDCard:
                    id:m1
                    elevation:99999
                    orientation:'vertical'                        
                        
                      
                MDCard:
                    id:m2                              
                   
                 
                 
                    
          
      
                      
                                                                  
        MDBottomNavigationItem:
            name:'s2'
            id:s2
            icon:'language-python'
            text:'Python'    
            Carousel:
                id:c2
                
                        

    MDTopAppBar:
        md_bg_color:0,1,0,1
        pos_hint:{'top':1}
        title:'JAI MAHAKAL'
        left_action_items:[['menu',lambda x:nd1.set_state('open')]]
    
    MDNavigationDrawer:
        id:nd1      



'''





class Sec(Screen):
    pass




class Fir(Screen):
    pass
    
    
    

class Manager(ScreenManager):
    pass




class demo(MDApp):
    def build(self):
        self.theme_cls.theme_style='Light'
        self.bu=Builder.load_string(kv)
        return self.bu
        
    def on_start(self):
        for i in range(0,10):
            self.bu.get_screen('sc1').ids.c2.add_widget(MDCard(elevation=10))
        
        
        
demo().run()
        
