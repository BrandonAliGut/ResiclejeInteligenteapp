from kivy.lang import Builder
from kivy.metrics import dp
from kivy.animation import Animation
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition,SlideTransition, RiseInTransition
from kivymd.uix.snackbar import Snackbar
from kivy.properties import StringProperty,DictProperty,NumericProperty
from kivy.clock import Clock
from paquetes_kv import *
from kivymd.uix.fitimage  import FitImage
['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'Subtitle1', 'Subtitle2', 'Body1', 'Body2', 'Button', 'Caption', 'Overline', 'Icon']


#Window.size = (400,800)
#Classes primaria---------------------------
class Window(ScreenManager):
    transition=FadeTransition()
    pass


class Bienvenida(Screen):
    def __init__(self):
        super(Bienvenida, self).__init__()
        Clock.schedule_once(lambda dt: self.Icrementoexponecial(),5)
        
    def Icrementoexponecial(self):
        
        lbl_1 = self.ids.lbl_1
       

        Animation(
            angle=0,opacity=1, y=lbl_1.height * .3, d=3.6, t="in_out_back"
        ).start(lbl_1)
        
        
class Home(Screen):
    pass

class InicioPrimario(Screen):
    transition=RiseInTransition()
    pass
class Category_selection(Screen):
    pass


class Sobre_Nosotros(Screen):
    transition_progress = .8
    pass

        

class Contactanos(Screen):
    pass
class Ingresar(Screen):
    pass


class MainApp(MDApp):
    blur_value = NumericProperty(0)
    blurs_value = NumericProperty(0)
    color_text_P = (95/255, 95/255, 95/255)
    color_oscuro_img = (34/255, 29/255, 29/255, 0.664)
    color_box = (233/255,234/255,233/255,1)
    color_box_color_u = (233/255,234/255,233/255,.4)
    color_bar = [0,154/255,0,1]
    pwhite = (34/255, 29/255, 29/255, 0.815)
    def build(self):
        #Controlador de ventanas----------
        self.wn = ScreenManager(transition=FadeTransition())
        
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Inicio",
                "height": dp(56),
                "theme_text_color": "Custom",
                "text_color": [1,1,1,1],
                "on_release": lambda x="Inicio": self.menu_callback(x),
             },
            {
                "viewclass": "OneLineListItem",
                "text": "Sobre Nosotros",
                "theme_text_color": "Custom",
                "height": dp(56),
                "text_color": [1,1,1,1],
                
                "on_release": 
                    
                    lambda x="Sobre_Nosotros": self.menu_callback(x),

             },
            {
                "viewclass": "OneLineListItem",
                "text": "Contactanos",
                "theme_text_color": "Custom",
                "height": dp(56),
                "text_color": [1,1,1,1],
                "on_release": lambda x="Contactanos": self.menu_callback(x),
             },
            {
                "viewclass": "OneLineListItem",
                "text": "Ingresar",
                "theme_text_color": "Custom",
                "height": dp(56),
                "text_color": [1,1,1,1],
                "on_release": lambda x="Ingresar": self.menu_callback(x),
             }
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
            hor_growth="right",
            elevation=0,
            border_margin=dp(4),
            background_color=(0,154/255,0,1)
        )
        
        
        screens = [
            Bienvenida(),#0
            InicioPrimario(),#1

            
       

            
            #__________Administrador__________#
            
        ]
        #mentod para agregar cada uno delas pantallas llamadas en su acto
        for a_data in screens: 
            self.wn.add_widget(a_data)
        #Uso esclusibo para el llamado de instrucciones que se ejecutaran cuando se inicie la aplicacion
        Clock.schedule_once(lambda dt: self.canviar_navigation(),1)# 10 Metodo contador de tiempo, que cumple con la patalla de flask o primer pantalla

        
        #Retornacion de las swidget,screen adn ScreenManager que inicializan las aplicaciones
        return self.wn #Retornacion de la variable principal

    def root_properti(self):
        self.root.current = "Properpantalla"# type: ignore 
        self.menu_callback("Inicio")

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, text_item):
        
        if text_item =="Inicio":
            self.wn.screens[1].ids["screen_manager"].current = "Home"
        elif text_item =="Sobre_Nosotros":
            self.wn.screens[1].ids["screen_manager"].current = "Sobre_Nosotros"
            
        self.menu.dismiss()
        Snackbar(text=text_item, bg_color=[0,154/255,0,1], elevation=1).open()
    def canviar_navigation(self):
        self.root_properti()
    def category_selection_funcion(self, text):
        print(text)


if __name__=="__main__":
    MainApp().run()
