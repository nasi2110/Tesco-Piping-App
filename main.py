from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Window.orientation = 'landscape'

class CoverScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Using page_1.jpg as the background
        self.add_widget(Image(source='page_1.jpg', allow_stretch=True, keep_ratio=False))
        btn = Button(text="START EXPLORING", size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'y': 0.1})
        btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'categories'))
        self.add_widget(btn)

class CategoryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = GridLayout(cols=2, padding=50, spacing=20)
        cats = ["PROCESS SIDE", "BETWEEN SEALS", "ATMOSPHERIC SIDE", "GENERAL LAYOUT"]
        for cat in cats:
            btn = Button(text=cat, bold=True)
            btn.bind(on_press=self.select_cat)
            layout.add_widget(btn)
        self.add_widget(layout)
    def select_cat(self, instance):
        self.manager.get_screen('list').load_category(instance.text)
        self.manager.current = 'list'

class ListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.scroll = ScrollView()
        self.grid = GridLayout(cols=1, size_hint_y=None, spacing=10, padding=10)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)
        self.layout.add_widget(self.scroll)
        back = Button(text="BACK TO CATEGORIES", size_hint_y=0.1)
        back.bind(on_press=lambda x: setattr(self.manager, 'current', 'categories'))
        self.layout.add_widget(back)
        self.add_widget(self.layout)

    def load_category(self, category):
        self.grid.clear_widgets()
        # Mapping: (Plan Name, Image Page, Notes Page)
        data = {
            "PROCESS SIDE": [("Plan 01", 12, 13), ("Plan 02", 14, 15)],
            "BETWEEN SEALS": [("Plan 52", 38, 39)],
            "ATMOSPHERIC SIDE": [("Plan 51", 56, 57)],
            "GENERAL LAYOUT": [("Plan 99", 74, 75)]
        }
        for name, img, note in data.get(category, []):
            btn = Button(text=name, size_hint_y=None, height=120)
            btn.bind(on_press=lambda x, i=img, n=note: self.open_plan(i, n))
            self.grid.add_widget(btn)
    def open_plan(self, img, note):
        self.manager.get_screen('viewer').setup(img, note)
        self.manager.current = 'viewer'

class ViewerScreen(Screen):
    def setup(self, img, note):
        self.clear_widgets()
        l = BoxLayout(orientation='vertical')
        c = Carousel()
        c.add_widget(Image(source=f'page_{img}.jpg'))
        c.add_widget(Image(source=f'page_{note}.jpg'))
        l.add_widget(c)
        btn = Button(text="BACK TO LIST", size_hint_y=0.1)
        btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'list'))
        l.add_widget(btn)
        self.add_widget(l)

class TescoApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(CoverScreen(name='cover'))
        sm.add_widget(CategoryScreen(name='categories'))
        sm.add_widget(ListScreen(name='list'))
        sm.add_widget(ViewerScreen(name='viewer'))
        return sm

if __name__ == '__main__':
    TescoApp().run()
