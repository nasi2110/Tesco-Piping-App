from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# Set the default orientation to landscape (best for engineering plans)
Window.orientation = 'landscape'

class CoverScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Assuming page_1.jpg is your cover/index page
        self.add_widget(Image(source='page_1.jpg', allow_stretch=True, keep_ratio=False))
        
        btn = Button(
            text="START EXPLORING", 
            size_hint=(0.3, 0.1), 
            pos_hint={'center_x': 0.5, 'y': 0.1},
            background_color=(0.1, 0.6, 0.9, 1),
            bold=True
        )
        btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'categories'))
        self.add_widget(btn)

class CategoryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = GridLayout(cols=2, padding=50, spacing=30)
        
        categories = ["PROCESS SIDE", "BETWEEN SEALS", "ATMOSPHERIC SIDE", "GENERAL LAYOUT"]
        for cat in categories:
            btn = Button(text=cat, bold=True, background_color=(0.2, 0.3, 0.4, 1))
            btn.bind(on_press=self.select_cat)
            layout.add_widget(btn)
        self.add_widget(layout)

    def select_cat(self, instance):
        self.manager.get_screen('list').load_category(instance.text)
        self.manager.current = 'list'

class ListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = BoxLayout(orientation='vertical')
        
        # Scrollable area for the plan list
        self.scroll = ScrollView(size_hint=(1, 0.9))
        self.grid = GridLayout(cols=1, size_hint_y=None, spacing=10, padding=20)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)
        
        self.main_layout.add_widget(self.scroll)
        
        # Bottom navigation
        back_btn = Button(text="BACK TO CATEGORIES", size_hint_y=0.1)
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'categories'))
        self.main_layout.add_widget(back_btn)
        
        self.add_widget(self.main_layout)

    def load_category(self, category):
        self.grid.clear_widgets()
        
        # Dictionary mapping Categories to (Plan Name, Image Page Number, Notes Page Number)
        # Adjust these numbers based on your PDF extraction
        data = {
            "PROCESS SIDE": [("Plan 01", 12, 13), ("Plan 02", 14, 15), ("Plan 11", 18, 19)],
            "BETWEEN SEALS": [("Plan 52", 38, 39), ("Plan 53A", 40, 41)],
            "ATMOSPHERIC SIDE": [("Plan 51", 56, 57), ("Plan 62", 60, 61)],
            "GENERAL LAYOUT": [("Plan 99", 74, 75)]
        }
        
        for name, img, note in data.get(category, []):
            btn = Button(text=name, size_hint_y=None, height=120)
            btn.bind(on_press=lambda x, i=img, n=note: self.open_viewer(i, n))
            self.grid.add_widget(btn)

    def open_viewer(self, img_idx, note_idx):
        self.manager.get_screen('viewer').setup(img_idx, note_idx)
        self.manager.current = 'viewer'

class ViewerScreen(Screen):
    def setup(self, img_idx, note_idx):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical')
        
        # Carousel for swiping between Plan Image and Notes
        carousel = Carousel(direction='right')
        carousel.add_widget(Image(source=f'page_{img_idx}.jpg'))
        carousel.add_widget(Image(source=f'page_{note_idx}.jpg'))
        
        layout.add_widget(carousel)
        
        back_btn = Button(text="BACK TO PLAN LIST", size_hint_y=0.1)
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'list'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)

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
