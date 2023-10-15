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

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
      
        md_bg_color: [0,154/255,0,1]
        elevation: 0
        left_action_items: [["menu", lambda x: app.callback(x)]]
        
    
    
    MDScrollView:
        MDList:

            cols: 1
            spacing: '10dp'
            padding: ('22dp', '22dp', '22dp', '22dp')
            
            MDCard:
                orientation: 'vertical'
                size_hint_x: .7
                size_hint_y: None
                height: dp(160)
                padding: ('5dp', '5dp', '5dp', '5dp')
                focus_behavior: False
                pos_hint: {"center_x": .5, "center_y": .5}
                md_bg_color: (233/255,234/255,233/255,0)
                elevation: 0
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: ('20dp', '20dp', '20dp', '20dp')
                    MDLabel:
                        text: "Entrega de reciclaje"
                        theme_text_color: "Custom"
                        font_style: 'H4'
                        bold: True
                    MDLabel:
                        text: "¿Cómo quieres entregar tu reciclaje hoy?"
                        theme_text_color: "Custom"
                        bold: True
                        font_style: 'H5'

            
            
            MDCard:
                orientation: 'vertical'
                size_hint_x: .7
                size_hint_y: None
                height: dp(160)
                padding: ('5dp', '5dp', '5dp', '5dp')
                focus_behavior: False
                pos_hint: {"center_x": .5, "center_y": .5}
                md_bg_color: (233/255,234/255,233/255,1)
                unfocus_color: (233/255,234/255,233/255,1)
                focus_color: (0,154/255,0,.2)
                radius:'20dp'
                elevation: 0
                MDBoxLayout:
                    padding: ('20dp', '20dp', '20dp', '20dp')
                    MDLabel:
                        text: "Contactar a reciclador/a y registrar entrega"
                        theme_text_color: "Custom"
                        font_style: 'H5'

                MDBoxLayout:
                    padding: ('20dp', '20dp', '20dp', '20dp')
                    size_hint_x: .5
                    size_hint_min_x:.4
                    orientation: 'vertical'
                
                    MDCard:
                        pos_hint: {'center_x': 1.8,'center_y': 0.5}
                        size_hint_x: None
                        size_hint_y: None
                        width: dp(160)
                        height: dp(45)
                        focus_behavior: False
                        md_bg_color: (0,154/255,0,1)
                        radius:'25dp'
                        elevation: 0
                        padding: ('10dp', '10dp', '10dp', '10dp')
                        MDLabel:
                            text: "Contactar"
                            theme_text_color: "Custom"
                            text_color: [1,1,1,1]
                            font_style: 'Button'
                        MDIconButton:
                            pos_hint: {'center_x': 0.5,'center_y': 0.6}
                            icon: 'account-group'
                            theme_icon_color: "Custom"
                            icon_color: (1,1,1,1)
                            icon_size: "30sp"
                                     
            MDCard:
                orientation: 'vertical'
                size_hint_x: .7
                size_hint_y: None
                height: dp(160)
                padding: ('5dp', '5dp', '5dp', '5dp')
                focus_behavior: False
                pos_hint: {"center_x": .5, "center_y": .5}
                md_bg_color: (233/255,234/255,233/255,1)
                unfocus_color: (233/255,234/255,233/255,1)
                focus_color: (0,154/255,0,.2)
                radius:'20dp'
                elevation: 0
                MDBoxLayout:
                    padding: ('20dp', '20dp', '20dp', '20dp')
                    MDLabel:
                        text: "Entregar en estación de reciclaje"
                        theme_text_color: "Custom"
                        font_style: 'H5'

                MDBoxLayout:
                    padding: ('20dp', '20dp', '20dp', '20dp')
                    size_hint_x: .5
                    size_hint_min_x:.4
                    orientation: 'vertical'
                
                    MDCard:
                        pos_hint: {'center_x': 1.8,'center_y': 0.5}
                        size_hint_x: None
                        size_hint_y: None
                        width: dp(160)
                        height: dp(45)
                        focus_behavior: False
                        md_bg_color: (0,154/255,0,1)
                        radius:'25dp'
                        elevation: 0
                        padding: ('10dp', '10dp', '10dp', '10dp')
                        MDLabel:
                            text: "Contactar"
                            theme_text_color: "Custom"
                            text_color: [1,1,1,1]
                            font_style: 'Button'
                        MDIconButton:
                            pos_hint: {'center_x': 0.5,'center_y': 0.6}
                            icon: 'account-group'
                            theme_icon_color: "Custom"
                            icon_color: (1,1,1,1)
                            icon_size: "30sp"

            MDCard:
                orientation: 'vertical'
                size_hint_x: .7
                size_hint_y: None
                height: dp(160)
                padding: ('5dp', '5dp', '5dp', '5dp')
                focus_behavior: False
                pos_hint: {"center_x": .5, "center_y": .5}
                md_bg_color: (233/255,234/255,233/255,1)
                unfocus_color: (233/255,234/255,233/255,1)
                focus_color: (0,154/255,0,.2)
                radius:'20dp'
                elevation: 0
                MDBoxLayout:
                    padding: ('20dp', '20dp', '20dp', '20dp')
                    MDLabel:
                        text: "Entregar en centro de acopio"
                        theme_text_color: "Custom"
                        font_style: 'H5'

                MDBoxLayout:
                    padding: ('20dp', '20dp', '20dp', '20dp')
                    size_hint_x: .5
                    size_hint_min_x:.4
                    orientation: 'vertical'
                
                    MDCard:
                        pos_hint: {'center_x': 1.8,'center_y': 0.5}
                        size_hint_x: None
                        size_hint_y: None
                        width: dp(160)
                        height: dp(45)
                        focus_behavior: False
                        md_bg_color: (0,154/255,0,1)
                        radius:'25dp'
                        elevation: 0
                        padding: ('10dp', '10dp', '10dp', '10dp')
                        MDLabel:
                            text: "Contactar"
                            theme_text_color: "Custom"
                            text_color: [1,1,1,1]
                            font_style: 'Button'
                        MDIconButton:
                            pos_hint: {'center_x': 0.5,'center_y': 0.6}
                            icon: 'account-group'
                            theme_icon_color: "Custom"
                            icon_color: (1,1,1,1)
                            icon_size: "30sp"
            MDCard:
                orientation: 'vertical'
                size_hint_x: .7
                size_hint_y: None
                height: dp(160)
                padding: ('5dp', '5dp', '5dp', '5dp')
                focus_behavior: False
                pos_hint: {"center_x": .5, "center_y": .5}
                md_bg_color: (233/255,234/255,233/255,1)
                unfocus_color: (233/255,234/255,233/255,1)
                focus_color: (0,154/255,0,.2)
                radius:'20dp'
                elevation: 0
                MDBoxLayout:
                    padding: ('20dp', '20dp', '20dp', '20dp')
                    MDLabel:
                        text: "Solicitar retiro a mi puerta"
                        theme_text_color: "Custom"
                        font_style: 'H5'

                MDBoxLayout:
                    padding: ('20dp', '20dp', '20dp', '20dp')
                    size_hint_x: .5
                    size_hint_min_x:.4
                    orientation: 'vertical'
                
                    MDCard:
                        pos_hint: {'center_x': 1.8,'center_y': 0.5}
                        size_hint_x: None
                        size_hint_y: None
                        width: dp(160)
                        height: dp(45)
                        focus_behavior: False
                        md_bg_color: (0,154/255,0,1)
                        radius:'25dp'
                        elevation: 0
                        padding: ('10dp', '10dp', '10dp', '10dp')
                        MDLabel:
                            text: "Contactar"
                            theme_text_color: "Custom"
                            text_color: [1,1,1,1]
                            font_style: 'Button'
                        MDIconButton:
                            pos_hint: {'center_x': 0.5,'center_y': 0.6}
                            icon: 'account-group'
                            theme_icon_color: "Custom"
                            icon_color: (1,1,1,1)
                            icon_size: "30sp"

            MDCard:
                orientation: 'vertical'
                size_hint_x: .7
                size_hint_y: None
                height: dp(160)
                padding: ('5dp', '5dp', '5dp', '5dp')
                focus_behavior: False
                pos_hint: {"center_x": .5, "center_y": .5}
                md_bg_color: (233/255,234/255,233/255,1)
                unfocus_color: (233/255,234/255,233/255,1)
                focus_color: (0,154/255,0,.2)
                radius:'20dp'
                elevation: 0
                MDBoxLayout:
                    padding: ('20dp', '20dp', '20dp', '20dp')
                    MDLabel:
                        text: "Quiero saber cómo reciclar"
                        theme_text_color: "Custom"
                        font_style: 'H5'

                MDBoxLayout:
                    padding: ('20dp', '20dp', '20dp', '20dp')
                    size_hint_x: .5
                    size_hint_min_x:.4
                    orientation: 'vertical'
                
                    MDCard:
                        pos_hint: {'center_x': 1.8,'center_y': 0.5}
                        size_hint_x: None
                        size_hint_y: None
                        width: dp(160)
                        height: dp(45)
                        focus_behavior: False
                        md_bg_color: (0,154/255,0,1)
                        radius:'25dp'
                        elevation: 0
                        padding: ('10dp', '10dp', '10dp', '10dp')
                        MDLabel:
                            text: "Contactar"
                            theme_text_color: "Custom"
                            text_color: [1,1,1,1]
                            font_style: 'Button'
                        MDIconButton:
                            pos_hint: {'center_x': 0.5,'center_y': 0.6}
                            icon: 'account-group'
                            theme_icon_color: "Custom"
                            icon_color: (1,1,1,1)
                            icon_size: "30sp"





'''
Window.size = (400,800)
#Classes primaria---------------------------
class Window(ScreenManager):
    transition=FadeTransition()
    pass


class Bienvenida(Screen):
    def __init__(self):
        super(Bienvenida, self).__init__()
        Clock.schedule_once(lambda dt: self.Icrementoexponecial(),4)
        
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
