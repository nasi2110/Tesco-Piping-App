from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.carousel import Carousel
from kivy.core.window import Window

# The Plan Database
PLAN_DATA = {
    "SINGLE": {
        "Plan 01": [12, 13], "Plan 02": [14, 15], "Plan 03": [16, 17],
        "Plan 11": [18, 19], "Plan 12": [20, 21], "Plan 13": [22, 23],
        "Plan 14": [24, 25], "Plan 21": [26, 27], "Plan 22": [28, 29],
        "Plan 23": [30, 31], "Plan 31": [32, 33], "Plan 32": [34, 35],
        "Plan 41": [36, 37]
    },
    "DOUBLE": {
        "Plan 52": [38, 39], "Plan 53A": [40, 41], "Plan 53B": [42, 43],
        "Plan 53C": [44, 45], "Plan 54": [46, 47], "Plan 55": [48, 49],
        "Plan 71": [50, 51], "Plan 72": [52, 53], "Plan 74": [54, 55]
    },
    "QUENCH": {
        "Plan 51": [56, 57], "Plan 61": [58, 59], "Plan 62": [60, 61],
        "Plan 65A": [62, 63], "Plan 65B": [64, 65], "Plan 66A": [66, 67],
        "Plan 66B": [68, 69], "Plan 75": [70, 71], "Plan 76": [72, 73]
    },
    "GAS": {
        "Plan 99": [74, 75]
    }
}

class LandingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Image(source='tesco_logo.jpg', size_hint_y=0.4, allow_stretch=True))
        content = BoxLayout(padding=40)
        btn = Button(text="Mechanical Seal\nAPI Plans", background_color=(0.9, 0.1, 0.1, 1), font_size='24sp', halign='center')
        btn.bind(on_release=lambda x: setattr(self.manager, 'current', 'dashboard'))
        content.add_widget(btn)
        layout.add_widget(content)
        layout.add_widget(Label(text="©2026 Tesco Engineering", size_hint_y=0.1, color=(0.5,0.5,0.5,1)))
        self.add_widget(layout)

class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.on_back_button)
        self.main_layout = BoxLayout(orientation='vertical')
        
        # Navigation
        nav_bar = GridLayout(cols=4, size_hint_y=0.1)
        for c in ["SINGLE", "DOUBLE", "QUENCH", "GAS"]:
            b = Button(text=c, background_normal='', background_color=(0.8, 0, 0, 1), font_size='12sp')
            b.bind(on_release=self.show_plans)
            nav_bar.add_widget(b)
        self.main_layout.add_widget(nav_bar)

        # Content Area
        self.display = FloatLayout()
        self.banner = Image(source='company_banner.jpg', size_hint=(1, 1), allow_stretch=True, keep_ratio=False)
        self.display.add_widget(self.banner)
        
        # Scrollable Floating List
        self.scroll = ScrollView(size_hint=(0.5, 0.7), pos_hint={'x': 0.05, 'top': 0.95})
        self.list_grid = GridLayout(cols=1, size_hint_y=None, spacing=2)
        self.list_grid.bind(minimum_height=self.list_grid.setter('height'))
        self.scroll.add_widget(self.list_grid)
        
        self.main_layout.add_widget(self.display)
        self.add_widget(self.main_layout)

    def on_back_button(self, window, key, *args):
        if key == 27:
            if self.scroll.parent:
                self.display.remove_widget(self.scroll)
                return True
            self.manager.current = 'landing'
            return True
        return False

    def show_plans(self, instance):
        self.list_grid.clear_widgets()
        category = instance.text
        for plan_name in PLAN_DATA[category]:
            btn = Button(text=plan_name, size_hint_y=None, height=50)
            btn.bind(on_release=lambda x: self.open_carousel(category, x.text))
            self.list_grid.add_widget(btn)
        if not self.scroll.parent:
            self.display.add_widget(self.scroll)

    def open_carousel(self, cat, plan_name):
        self.display.clear_widgets()
        carousel = Carousel(direction='right')
        # Map indices: 0=Image, 1=Notes
        img_idx, note_idx = PLAN_DATA[cat][plan_name]
        
        # The 4 Slides: Plan Img, Plan Notes, Legend (Pg 4), Symbol Notes (Pg 5)
        pages = [img_idx, note_idx, 4, 5]
        for p in pages:
            carousel.add_widget(Image(source=f'page_{p}.jpg', allow_stretch=True))
        
        self.display.add_widget(carousel)

class TescoApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LandingScreen(name='landing'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        return sm

if __name__ == '__main__':
    TescoApp().run()
