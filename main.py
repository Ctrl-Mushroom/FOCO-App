from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.properties import StringProperty
from kivy.clock import Clock
import json
import requests
import time
from kivy.core.window import Window
Window.size = (300, 630)

'''DateTime:
            id: needs
            text:app.secs
'''
help_str = '''

#:import Calendar calendar.Calendar
ScreenManager:

    WelcomeScreen:
    MainScreen:
    LoginScreen:
    SignupScreen:
    DietScreen:
    RoutineScreen:
    MilestoneScreen:
    ProfileScreen:

<Day@MDRaisedButton>:
    font_size: 10
    datepicker: self.parent.datepicker
    color: [1,1,1,1]
    background_color: root.color if self.text != "" else [0,0,0,0]
    disabled: True if self.text == "" else False
    on_release:
        root.datepicker.picked = [int(self.text), root.datepicker.month, root.datepicker.year]

<Week@MDBoxLayout>:
    datepicker: root.parent
    orientation: "horizontal"
    weekdays: ["","","","","","",""]
    Day:
        text: str(root.weekdays[0])
        size_hint: (1,1)
    Day:
        text: str(root.weekdays[1])
        size_hint: (1,1)
    Day:
        text: str(root.weekdays[2])
        size_hint: (1,1)
    Day:
        text: str(root.weekdays[3])
        size_hint: (1,1)
    Day:
        text: str(root.weekdays[4])
        size_hint: (1,1)
    Day:
        text: str(root.weekdays[5])
        size_hint: (1,1)
    Day:
        text: str(root.weekdays[6])
        size_hint: (1,1)
<WeekDays@MDBoxLayout>:
    Label:
        font_size: 10
        text: "Sun"
    Label:
        font_size: 10
        text: "Mon"
    Label:
        font_size: 10
        text: "Tue"
    Label:
        font_size: 10
        text: "Wed"
    Label:
        font_size: 10
        text: "Thu"
    Label:
        font_size: 10
        text: "Fri"
    Label:
        font_size: 10
        text: "Sat"
<NavBar@MDBoxLayout>:
    orientation: "vertical"
    datepicker: self.parent
    Widget:
    BoxLayout:
        orientation: "horizontal"
        MDRaisedButton:
            size_hint:(1,1)
            color: [1,1,1,1]
            font_size: 10
            text: "<"
            on_release:
                if root.datepicker.month == 1 and spin.hint_text == 'months': root.datepicker.year -= 1
                if spin.hint_text == 'months': root.datepicker.month = 12 if root.datepicker.month == 1 else root.datepicker.month - 1
        Label:
            id: spin
            color: (1,1,1,1)
            font_size: 10
            hint_text: 'months'
            text: root.datepicker.months[root.datepicker.month-1]
            on_text:
                root.datepicker.month = root.datepicker.months.index(self.text)+1
        Label:
            color: (1,1,1,1)
            font_size: 10
            text: str(root.datepicker.year)
            on_text:
                root.datepicker.year = int(self.text)
        MDRaisedButton:
            size_hint:(1,1)
            color: [1,1,1,1]
            font_size: 10
            text: ">"
            on_release:
                if root.datepicker.month == 12 and spin.hint_text == 'months': root.datepicker.year += 1
                if spin.hint_text == 'months': root.datepicker.month = 1 if root.datepicker.month == 12 else root.datepicker.month + 1
<DatePicker@MDBoxLayout>:
    year: 2021
    month: 3
    picked: ["","",""]
    months: ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    calendar: Calendar(firstweekday=6)
    days: [(i if i > 0 else "") for i in self.calendar.itermonthdays(self.year, self.month)] + [""] * 14
    orientation: "vertical"
    NavBar:
    WeekDays:
    Week:
        weekdays: root.days[0:7]
    Week:
        weekdays: root.days[7:14]
    Week:
        weekdays: root.days[14:21]
    Week:
        weekdays: root.days[21:28]
    Week:
        weekdays: root.days[28:35]
    Week:
        weekdays: root.days[35:]
    Widget:

<WelcomeScreen>:
    name:'welcomescreen'
    RelativeLayout:
        canvas.before:
            Color:
            Rectangle:
                source: "png/Background0.png"
                pos: self.pos
                size: self.size
        BoxLayout:
            orientation: "horizontal"
            MDRaisedButton:
                text:'SIGN IN'
                size_hint: (0.13,0)
                on_press:
                    root.manager.current = 'loginscreen'
                    root.manager.transition.direction = 'right' 
            MDRaisedButton:
                text:'SIGN UP'
                size_hint: (0.13,0)
                on_press:
                    root.manager.current = 'signupscreen'
                    root.manager.transition.direction = 'left'

<LoginScreen>:
    name:'loginscreen'
    RelativeLayout:
        canvas.before:
            Color:
            Rectangle:
                source: "png/Background1.png"
                pos: self.pos
                size: self.size
                
        BoxLayout:
            orientation:"vertical"

        MDLabel:
            text:'Welcome Back!'
            font_style:'H4'
            halign:'center'
            pos_hint: {'center_y':0.8}
        MDTextField:
            id:login_email
            pos_hint: {'center_y':0.6,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Input Username'
            helper_text:'Required Field!'
            helper_text_mode:  'on_error'
            icon_right: 'account'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"
        MDTextField:
            id:login_password
            pos_hint: {'center_y':0.4,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Input Password'
            helper_text:'Required Field!'
            helper_text_mode:  'on_error'
            icon_right: 'account'
            icon_right_color: app.theme_cls.primary_color
            required: True
            password: True
            mode: "rectangle"
        MDRaisedButton:
            text:'Get In'
            size_hint: (0.4,0.07)
            pos_hint: {'center_x':0.5,'center_y':0.2}
            on_press:
                app.login()
                app.username_changer()

    BoxLayout:
        orientation: "horizontal"
        MDRaisedButton:
            text:'Sign In'
            size_hint: (0.13,0)
            on_press: 
                root.manager.current = 'loginscreen'
                root.manager.transition.direction = 'right'      
        MDRaisedButton:
            text:'Sign Up'
            size_hint: (0.13,0)
            on_press:
                root.manager.current = 'signupscreen'
                root.manager.transition.direction = 'left'

<SignupScreen>:
    name:'signupscreen'
    RelativeLayout:
        canvas.before:
            Color:
            Rectangle:
                source: "png/Background2.png"
                pos: self.pos
                size: self.size
        
        MDLabel:
            text:'Hello, Friend!'
            font_style:'H4'
            halign:'center'
            pos_hint: {'center_y':0.9}
        MDTextField:
            id:signup_email
            pos_hint: {'center_y':0.6,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Username'
            helper_text:'Required Field!'
            helper_text_mode:  'on_error'
            icon_right: 'account'
            icon_right_color: app.theme_cls.primary_color
            required: True
            mode: "rectangle"
        MDTextField:
            id:signup_username
            pos_hint: {'center_y':0.75,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Display Name'
            helper_text:'Required Field!'
            helper_text_mode:  'on_error'
            icon_right: 'account'
            icon_right_color: app.theme_cls.primary_color
            required: True
        MDTextField:
            id:signup_password
            pos_hint: {'center_y':0.4,'center_x':0.5}
            size_hint : (0.7,0.1)
            hint_text: 'Password'
            helper_text:'Required Field!'
            helper_text_mode:  'on_error'
            icon_right: 'account'
            icon_right_color: app.theme_cls.primary_color
            required: True
            multiline: False
            password: True
            mode: "rectangle"
        MDRaisedButton:
            text:'Start'
            size_hint: (0.4,0.07)
            pos_hint: {'center_x':0.5,'center_y':0.2}
            on_press: app.signup()

    BoxLayout:
        orientation: "horizontal"
        MDRaisedButton:
            text:'Sign In'
            size_hint: (0.13,0)
            on_press: 
                root.manager.current = 'loginscreen'
                root.manager.transition.direction = 'right'      
        MDRaisedButton:
            text:'Sign Up'
            size_hint: (0.13,0)
            on_press:
                root.manager.current = 'signupscreen'
                root.manager.transition.direction = 'left'

<DietScreen>
    name:'dietscreen'
    BoxLayout:
        canvas.before:
            Color:
            Rectangle:
                source: "png/Background7.png"
                pos: self.pos
                size: self.size
        orientation: "vertical"
        BoxLayout: 
            orientation: "vertical"
            size_hint_y: None
            height: root.height/4
            BoxLayout:
                orientation: "horizontal"
                BoxLayout:
                    orientation: "vertical"
                    Widget:
                BoxLayout:
                    orientation: "vertical"
                    size_hint_x: None
                    width: root.width/2.5
                    BoxLayout:
                    BoxLayout:
                        orientation: "vertical"
                        MDLabel:
                            text:'~ Diet ~'
                            font_style:'H6'
                            color: 1,1,1,1
                            halign:'center'
                        MDLabel:
                            id: dtype
                            font_style:'H6'
                            color: 1,1,1,1
                            halign:'center'
                    BoxLayout:
                        orientation: "vertical"
                        BoxLayout:
                            orientation: "horizontal"
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'mainscreen'
                                        root.manager.transition.direction = 'right'

                                    Image:
                                        source: "png/Schedules.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'routinescreen'
                                        root.manager.transition.direction = 'right'


                                    Image:
                                        source: "png/Exercise.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'dietscreen'
                                        root.manager.transition.direction = 'right'

                                    Image:
                                        source: "png/Diet.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 1
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'milestonescreen'
                                        root.manager.transition.direction = 'left'


                                    Image:
                                        source: "png/Milestone.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'profilescreen'
                                        root.manager.transition.direction = 'left'


                                    Image:
                                        source: "png/About.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                    BoxLayout:
                        orientation: "horizontal"
                        Widget:
                BoxLayout:
                    orientation: "vertical"
                    Widget:
        Carousel: 
            direction: 'bottom'
            pos_hint : {'center_x': 0.5, 'center_y':0}
            RelativeLayout:
                MDTextFieldRect:
                    id: diet
                    pos_hint : {'center_x':0.45, 'center_y':0.15}
                    size_hint: 0.7, None
                    halign:'center'
                    height: "30dp"                
                    hint_text: '"Create diet plan?"'
                    helper_text:'Diet description.'
                    icon_right_color: app.theme_cls.primary_color   
                MDFlatButton:
                    size_hint: 0.18,0.12
                    pos_hint : {'center_x':0.88, 'center_y':0.15}
                    on_release: app.req_diet(diet.text)
                    Image:
                        source: "png/Custom.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                MDRoundFlatButton:
                    id: dietset3
                    size_hint: 0.15,0.1
                    pos_hint : {'center_x':0.5, 'center_y':0.33}
                    on_release: app.change_diet(dietset3.text)
                    Image:
                        source: "png/Clear.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                MDRoundFlatButton:
                    id: dietset0
                    text: 'KETO'
                    font_size: 0
                    pos_hint : {'center_x':0.25, 'center_y':0.9}
                    size_hint: 0.28,0.18
                    on_release: app.change_diet(dietset0.text)
                    Image:
                        source: "png/Ketogenic.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                MDLabel:
                    text:'Ketogenic Diet'
                    text_color:'0,0,0,0'
                    font_style:'H6'
                    color: 1,1,1,1
                    halign:'left'
                    pos_hint : {'center_x':0.93, 'center_y':0.9}
                MDRoundFlatButton:
                    id: dietset1
                    text: 'PALEO'
                    font_size: 0
                    pos_hint : {'center_x':0.25, 'center_y':0.7}
                    size_hint: 0.28,0.18
                    on_release: app.change_diet(dietset1.text)
                    Image:
                        source: "png/Paleolithic.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                MDLabel:
                    text:'Paleolithic Diet'
                    text_color:'0,0,0,0'
                    font_style:'H6'
                    color: 1,1,1,1
                    halign:'left'
                    pos_hint : {'center_x':0.93, 'center_y':0.7}
                MDRoundFlatButton:
                    id: dietset2
                    text: 'LOW-CARB'
                    font_size: 0
                    pos_hint : {'center_x':0.25, 'center_y':0.5}
                    size_hint: 0.28,0.18
                    on_release: app.change_diet(dietset2.text)
                    Image:
                        source: "png/Low-Carb.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                MDLabel:
                    text:'Low-Carb Diet'
                    text_color:'0,0,0,0'
                    font_style:'H6'
                    color: 1,1,1,1
                    halign:'left'
                    pos_hint : {'center_x':0.93, 'center_y':0.5}
<RoutineScreen>:
    name:'routinescreen'
    BoxLayout:
        canvas.before:
            Color:
            Rectangle:
                source: "png/Background6.png"
                pos: self.pos
                size: self.size
        orientation: "vertical"
        BoxLayout: 
            orientation: "vertical"
            size_hint_y: None
            height: root.height/4
            BoxLayout:
                orientation: "horizontal"
                BoxLayout:
                    orientation: "vertical"
                    Widget:
                BoxLayout:
                    orientation: "vertical"
                    size_hint_x: None
                    width: root.width/2.5
                    BoxLayout:
                    BoxLayout:
                        orientation: "vertical" 
                        MDLabel:
                            text:'~ Routine ~'
                            font_style:'H6'
                            color: 1,1,1,1
                            halign:'center'
                        MDLabel:
                            id: rtype
                            font_style:'H6'
                            color: 1,1,1,1
                            halign:'center'
                    BoxLayout:
                        orientation: "vertical"
                        BoxLayout:
                            orientation: "horizontal"
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'mainscreen'
                                        root.manager.transition.direction = 'right'

                                    Image:
                                        source: "png/Schedules.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'routinescreen'
                                        root.manager.transition.direction = 'right'
                                        
                                    Image:
                                        source: "png/Exercise.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 1
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'dietscreen'
                                        root.manager.transition.direction = 'left'
                                        

                                    Image:
                                        source: "png/Diet.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'milestonescreen'
                                        root.manager.transition.direction = 'left'
                                        

                                    Image:
                                        source: "png/Milestone.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'profilescreen'
                                        root.manager.transition.direction = 'left'
                                        
                                        
                                    Image:
                                        source: "png/About.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                    BoxLayout:
                        orientation: "horizontal"
                        Widget:
                BoxLayout:
                    orientation: "vertical"
                    Widget:
        Carousel: 
            direction: 'bottom'
            pos_hint : {'center_x': 0.5, 'center_y':0}
            RelativeLayout:
                MDTextFieldRect:
                    id: routine
                    pos_hint : {'center_x':0.45, 'center_y':0.15}
                    size_hint: 0.7, None
                    halign:'center'
                    height: "30dp"                
                    hint_text: '"Custom routine?"'
                    helper_text:'Routine description.'
                    icon_right_color: app.theme_cls.primary_color   
                MDFlatButton:
                    size_hint: 0.18,0.12
                    pos_hint : {'center_x':0.88, 'center_y':0.15}
                    on_release: app.req_routine(routine.text)
                    Image:
                        source: "png/Custom.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                MDRectangleFlatButton:
                    id: routineset3
                    size_hint: 0.15,0.1
                    pos_hint : {'center_x':0.5, 'center_y':0.33}
                    on_release: app.change_routine(routineset3.text)
                    Image:
                        source: "png/Clear.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                MDRectangleFlatButton:
                    id: routineset0
                    text: 'BODYBUILD'
                    font_size: 0
                    pos_hint : {'center_x':0.25, 'center_y':0.9}
                    size_hint: 0.28,0.18
                    on_release: app.change_routine(routineset0.text)
                    Image:
                        source: "png/Bodybuild.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                MDLabel:
                    text:'Bodybuild'
                    text_color:'0,0,0,0'
                    font_style:'H6'
                    color: 1,1,1,1
                    halign:'left'
                    pos_hint : {'center_x':0.93, 'center_y':0.9}
                MDRectangleFlatButton:
                    id: routineset1
                    text: 'FLEXIBILITY'
                    font_size: 0
                    pos_hint : {'center_x':0.25, 'center_y':0.7}
                    size_hint: 0.28,0.18
                    on_release: app.change_routine(routineset1.text)
                    Image:
                        source: "png/Flexibility.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                MDLabel:
                    text:'Flexibility'
                    text_color:'0,0,0,0'
                    font_style:'H6'
                    color: 1,1,1,1
                    halign:'left'
                    pos_hint : {'center_x':0.93, 'center_y':0.7}
                MDRectangleFlatButton:
                    id: routineset2
                    text: 'HARDCORE'
                    font_size: 0
                    pos_hint : {'center_x':0.25, 'center_y':0.5}
                    size_hint: 0.28,0.18
                    on_release: app.change_routine(routineset2.text)
                    Image:
                        source: "png/Hardcore.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                MDLabel:
                    text:'HARDCORE'
                    text_color:'0,0,0,0'
                    font_style:'H6'
                    color: 1,1,1,1
                    halign:'left'
                    pos_hint : {'center_x':0.93, 'center_y':0.5}
<MilestoneScreen>:
    name: 'milestonescreen'
    BoxLayout:
        canvas.before:
            Color:
            Rectangle:
                source: "png/Background5.png"
                pos: self.pos
                size: self.size
        orientation: "vertical"
        BoxLayout: 
            orientation: "vertical"
            size_hint_y: None
            height: root.height/4
            BoxLayout:
                orientation: "horizontal"
                BoxLayout:
                    orientation: "vertical"
                    Widget:
                BoxLayout:
                    orientation: "vertical"
                    size_hint_x: None
                    width: root.width/2.5
                    BoxLayout:
                        orientation: "vertical"
                    BoxLayout:
                        orientation: "vertical"
                        Widget:
                    BoxLayout:
                        orientation: "vertical"
                        BoxLayout:
                            orientation: "horizontal"
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'mainscreen'
                                        root.manager.transition.direction = 'right'

                                    Image:
                                        source: "png/Schedules.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'routinescreen'
                                        root.manager.transition.direction = 'right'


                                    Image:
                                        source: "png/Exercise.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'dietscreen'
                                        root.manager.transition.direction = 'right'

                                    Image:
                                        source: "png/Diet.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'milestonescreen'
                                        root.manager.transition.direction = 'right'


                                    Image:
                                        source: "png/Milestone.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 1
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'profilescreen'
                                        root.manager.transition.direction = 'left'


                                    Image:
                                        source: "png/About.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                    BoxLayout:
                        orientation: "horizontal"
                        Widget:
                BoxLayout:
                    orientation: "vertical"
                    Widget:
        BoxLayout:
            orientation: "vertical"
        BoxLayout:
            orientation: "vertical"
            Widget:
    MDLabel:
        text:'Milestones Rewards!!!'
        color: 1,1,1,1
        font_style:'H5'
        halign:'center'
        pos_hint : {'center_x':0.5, 'center_y':0.93}
    MDLabel:
        text:''
        color: 1,1,1,1
        font_style:'H6'
        halign:'center'
        pos_hint : {'center_x':0.5, 'center_y':0.3}
    MDLabel:
        text:'Upcoming Themes...'
        color: 1,1,1,1
        font_style:'H6'
        halign:'center'
        pos_hint : {'center_x':0.5, 'center_y':0.25}
    
<ProfileScreen>:
    name: 'profilescreen'
    BoxLayout:
        canvas.before:
            Color:
            Rectangle:
                source: "png/Background9.png"
                pos: self.pos
                size: self.size
        orientation: "vertical"
        BoxLayout: 
            orientation: "vertical"
            size_hint_y: None
            height: root.height/4
            BoxLayout:
                orientation: "horizontal"
                BoxLayout:
                    orientation: "vertical"
                    Widget:
                BoxLayout:
                    orientation: "vertical"
                    size_hint_x: None
                    width: root.width/2.5
                    BoxLayout:
                        orientation: "vertical"
                    BoxLayout:
                        orientation: "vertical"
                        Widget:
                    BoxLayout:
                        orientation: "vertical"
                        BoxLayout:
                            orientation: "horizontal"
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'mainscreen'
                                        root.manager.transition.direction = 'right'

                                    Image:
                                        source: "png/Schedules.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'routinescreen'
                                        root.manager.transition.direction = 'right'


                                    Image:
                                        source: "png/Exercise.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'dietscreen'
                                        root.manager.transition.direction = 'right'

                                    Image:
                                        source: "png/Diet.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'milestonescreen'
                                        root.manager.transition.direction = 'right'


                                    Image:
                                        source: "png/Milestone.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'profilescreen'
                                        root.manager.transition.direction = 'right'


                                    Image:
                                        source: "png/About.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 1
                    BoxLayout:
                        orientation: "horizontal"
                        Widget:
                BoxLayout:
                    orientation: "vertical"
                    Widget:
        BoxLayout:
            orientation: "vertical"
        BoxLayout:
            orientation: "vertical"
            Widget:
    RelativeLayout:
        MDLabel:
            id: naming
            text: 'Profile'
            font_style:'H5'
            pos_hint : {'center_x':0.5, 'center_y':0.93}
            color: 1,1,1,1
            halign:'center'
        MDTextFieldRect:
            id: template
            pos_hint : {'center_x':0.45, 'center_y':0.17}
            size_hint: 0.7, None
            halign:'center'
            height: "30dp"                
            hint_text: 'Template? "submit email"'
            helper_text:'Template description.'
            icon_right_color: app.theme_cls.primary_color   
        MDFlatButton:
            size_hint: 0.2,0.14
            pos_hint : {'center_x':0.88, 'center_y':0.17}
            on_release: app.send_temp(template.text)
            Image:
                source: "png/Request.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y
        MDFlatButton:
            id: trophyset0
            text: '- - -'
            font_size: 0
            pos_hint : {'center_x':0.3, 'center_y':0.7}
            size_hint: 0.28,0.18
            on_release: app.see_trophy(trophyset0.text)
            Image:
                source: "png/Achievements.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y
        MDLabel:
            id: naming
            text: 'Achievements'
            font_style:'H6'
            pos_hint : {'center_x':0.65, 'center_y':0.73}
            color: 1,1,1,1
            halign:'center'
        MDLabel:
            id: ttype
            text: ''
            font_style:'H6'
            pos_hint : {'center_x':0.65, 'center_y':0.68}
            color: 1,1,1,1
            halign:'center'
        MDFlatButton:
            id: clearset0
            size_hint: 0.15,0.1
            pos_hint : {'center_x':0.38, 'center_y':0.66}
            on_release: app.see_trophy(clearset0.text)
            Image:
                source: "png/Refresh.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y
        MDFlatButton:
            id: friendset0
            text: '- - -'
            font_size: 0
            pos_hint : {'center_x':0.3, 'center_y':0.5}
            size_hint: 0.28,0.18
            on_release: app.see_friends(friendset0.text)
            Image:
                source: "png/Friends.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y
        MDLabel:
            id: naming
            text: 'Friends'
            font_style:'H6'
            pos_hint : {'center_x':0.65, 'center_y':0.53}
            color: 1,1,1,1
            halign:'center'
        MDLabel:
            id: ftype
            text: ''
            font_style:'H6'
            pos_hint : {'center_x':0.65, 'center_y':0.48}
            color: 1,1,1,1
            halign:'center'
        MDFlatButton:
            id: clearset1
            size_hint: 0.15,0.1
            pos_hint : {'center_x':0.38, 'center_y':0.46}
            on_release: app.see_friends(clearset1.text)
            Image:
                source: "png/Refresh.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y

<MainScreen>:
    name: 'mainscreen'
    BoxLayout:
        canvas.before:
            Color:
            Rectangle:
                source: "png/Background3.png"
                pos: self.pos
                size: self.size
        orientation: "vertical"
        BoxLayout: 
            orientation: "vertical"
            size_hint_y: None
            height: root.height/4
            BoxLayout:
                orientation: "horizontal"
                BoxLayout:
                    orientation: "vertical"
                    Widget:
                BoxLayout:
                    orientation: "vertical"
                    size_hint_x: None
                    width: root.width/2.5
                    BoxLayout:
                        orientation: "vertical"
                    BoxLayout:
                        orientation: "vertical"
                        MDLabel:
                            id:username_info
                            text:'Hello Main'
                            font_size: 10 + (root.width/150)
                            bold: True
                            color: 1,1,1,1
                            halign:'center'  
                    BoxLayout:
                        orientation: "vertical"
                        BoxLayout:
                            orientation: "horizontal"
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        print("asd")

                                    Image:
                                        source: "png/Schedules.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 1
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'routinescreen'
                                        root.manager.transition.direction = 'left'


                                    Image:
                                        source: "png/Exercise.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'dietscreen'
                                        root.manager.transition.direction = 'left'

                                    Image:
                                        source: "png/Diet.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'milestonescreen'
                                        root.manager.transition.direction = 'left'


                                    Image:
                                        source: "png/Milestone.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                            BoxLayout:
                                orientation: "vertical"
                                Button:
                                    background_color:0,0,0,0
                                    background_normal:''
                                    on_press:
                                        root.manager.current = 'profilescreen'
                                        root.manager.transition.direction = 'left'


                                    Image:
                                        source: "png/About.png"
                                        center_x: self.parent.center_x
                                        center_y: self.parent.center_y
                                        size: self.parent.size
                                        opacity: 0.75
                    BoxLayout:
                        orientation: "horizontal"
                        BoxLayout:
                            orientation: "vertical"
                            Label:
                                text:app.hrs+':'+app.mins
                                text_size:self.size
                                font_size: 12 + (root.width/150)
                                bold: True
                                halign:'right'
                                valign:'middle'
                            Label:
                                text:app.am_pm
                                text_size:self.size
                                font_size: 12 + (root.width/150)
                                bold: True
                                halign:'right'
                                valign:'middle'
                        BoxLayout:
                            orientation: "vertical"
                            size_hint_x: None
                            width: root.width/45
                            Label:
                                canvas.before:
                                    Color:
                                        rgba: (1,1,1,1)
                                    Rectangle:
                                        size: self.size
                                        pos: self.pos
                                size_hint_x: None
                                pos_hint : {'center_x':0.5,'center_y':0.5}
                                width: 2
                        BoxLayout:
                            orientation: "vertical"
                            Label:
                                text:app.mnth+' '+app.day
                                text_size:self.size
                                font_size: 12 + (root.width/150)
                                bold: True
                                halign:'left'
                                valign:'middle'
                            Label:
                                text:app.weeks
                                text_size:self.size
                                font_size: 12 + (root.width/150)
                                bold: True
                                halign:'left'
                                valign:'middle'
                BoxLayout:
                    orientation: "vertical"
                    Widget:
        BoxLayout:
            orientation: "vertical"
            BoxLayout: 
                orientation: "horizontal"
                BoxLayout:
                    orientation: "vertical"
                BoxLayout:
                    orientation: "vertical"
                    size_hint_x: None
                    width: root.width/1.57

                    DatePicker:
                    BoxLayout:
                        orientation: "vertical"
                        canvas.before:
                            Color:
                                rgba: (1,1,1,0.25)
                            Rectangle:
                                size: self.size
                                pos: self.pos
                        BoxLayout:
                            orientation: "horizontal"
                            Widget:
                                size_hint_x:0.2
                            BoxLayout:
                                orientation: "vertical"
                                Widget:
                                Label:
                                    text: "Exercise:"
                                    text_size:self.size
                                    font_size: 12 + (root.width/150)
                                    bold: True
                                    halign:'left'
                                    valign:'middle'
                                Label:
                                    text: "..."
                                Label:
                                    text: "Diet:"
                                    text_size:self.size
                                    font_size: 12 + (root.width/150)
                                    bold: True
                                    halign:'left'
                                    valign:'middle'
                                Label:
                                    text: "..."
                            Widget:
                                size_hint_x:0.2

                        Widget:
                        Widget:
                        Widget:
                BoxLayout:
                    orientation: "vertical"
        
    MDFlatButton:
        text:''
        pos_hint : {'center_x':0.88,'center_y':0.1}
        size_hint: (0.2,0.18)
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'
        Image:
            source: "png/Logout.png"
            center_x: self.parent.center_x
            center_y: self.parent.center_y
'''


class WelcomeScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass


class DietScreen(Screen):
    pass


class RoutineScreen(Screen):
    pass


class MilestoneScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


# would only need 3 pages
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcomescreen'))
sm.add_widget(MainScreen(name='mainscreen'))
sm.add_widget(LoginScreen(name='loginscreen'))
sm.add_widget(SignupScreen(name='signupscreen'))
sm.add_widget(DietScreen(name='dietscreen'))
sm.add_widget(RoutineScreen(name='routinescreen'))
sm.add_widget(MilestoneScreen(name='milestonescreen'))
sm.add_widget(ProfileScreen(name='profilescreen'))


class FoodyCoachApp(MDApp):
    time = StringProperty()
    mnth = StringProperty()
    secs = StringProperty()
    mins = StringProperty()
    hrs = StringProperty()
    day = StringProperty()
    weeks = StringProperty()
    am_pm = StringProperty()
    Timers = ""

    def build(self):
        self.strng = Builder.load_string(help_str)
        self.url = ""  # FIREBASE/REALTIME DATABASE URL
        self.icon = 'png/Outsides/FOCO.png'
        return self.strng

    def on_start(self):
        Clock.schedule_interval(self.update, 1)

    def update(self, dt=None):
        self.time = time.strftime('%H:%M:%S')
        self.mnth = time.strftime('%b')
        self.secs = time.strftime('%S')
        self.mins = time.strftime('%M')
        self.hrs = time.strftime('%I')
        self.day = time.strftime('%d')
        self.weeks = time.strftime('%A')
        self.am_pm = time.strftime('%p')

    def signup(self):
        signupemail = self.strng.get_screen('signupscreen').ids.signup_email.text
        signuppassword = self.strng.get_screen('signupscreen').ids.signup_password.text
        signupusername = self.strng.get_screen('signupscreen').ids.signup_username.text
        if signupemail.split() == [] or signuppassword.split() == [] or signupusername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Input', text='Please Enter a valid Input', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupemail, signuppassword)
            signup_info = str(
                {f'\"{signupemail}\":{{"Username":\"{signupemail}\",'
                 f'"Password":\"{signuppassword}\",'
                 f'"Display Name":\"{signupusername}\"}}'})
            signup_info = signup_info.replace(".", "-")
            signup_info = signup_info.replace("\'", "")
            to_database = json.loads(signup_info)
            print(to_database)
            signup_request = requests.patch(url=self.url, json=to_database)
            print(signup_request.ok)
            print(signup_request.content.decode())

            self.strng.get_screen('loginscreen').manager.current = 'loginscreen'

    # AUTH KEY GO TO FIREBASE/PROJECT SETTINGS/SERVICE ACCOUNTS/DATABASE SECRETS/"SHOW THE SECRET"
    auth = ''

    def login(self):
        loginemail = self.strng.get_screen('loginscreen').ids.login_email.text
        loginpassword = self.strng.get_screen('loginscreen').ids.login_password.text

        self.login_check = False
        supported_loginemail = loginemail.replace('.', '-')
        supported_loginpassword = loginpassword.replace('.', '-')
        request = requests.get(self.url + '?auth=' + self.auth)
        data = request.json()
        emails = set()
        for key, value in data.items():
            emails.add(key)
        if supported_loginemail in emails and supported_loginpassword == data[supported_loginemail]['Password']:
            self.username = data[supported_loginemail]['Display Name']
            self.login_check = True
            self.strng.get_screen('mainscreen').manager.current = 'mainscreen'
        else:
            print("user no longer exists")

    def close_username_dialog(self):
        self.dialog.dismiss()

    def username_changer(self):
        if self.login_check:
            self.strng.get_screen('mainscreen').ids.username_info.text = f"Hello there, {self.username}"

    def change_diet(self, diet_type):
        dietplan = self.strng.get_screen('loginscreen').ids.login_email.text
        self.strng.get_screen('dietscreen').ids.dtype.text = diet_type
        my_diet = '{"Diet": "%s"}' % diet_type
        requests.patch("" % dietplan, data=my_diet)

    def req_diet(self, diet_req):
        dietreq = self.strng.get_screen('loginscreen').ids.login_email.text
        set_diet = '{"Diet Request": "%s"}' % diet_req
        requests.patch("" % dietreq, data=set_diet)

    def change_routine(self, routine_type):
        routineplan = self.strng.get_screen('loginscreen').ids.login_email.text
        self.strng.get_screen('routinescreen').ids.rtype.text = routine_type
        my_routine = '{"Exercise": "%s"}' % routine_type
        requests.patch("" % routineplan,
                       data=my_routine)

    def req_routine(self, routine_req):
        routinereq = self.strng.get_screen('loginscreen').ids.login_email.text
        set_routine = '{"Exercise Request": "%s"}' % routine_req
        requests.patch("" % routinereq,
                       data=set_routine)

    def see_trophy(self, trophy_type):
        updatetrophy = self.strng.get_screen('loginscreen').ids.login_email.text
        self.strng.get_screen('profilescreen').ids.ttype.text = trophy_type
        my_trophy = '{"Achievements": "%s"}' % trophy_type
        requests.patch("" % updatetrophy,
                       data=my_trophy)

    def see_friends(self, friend_type):
        updatetrophy = self.strng.get_screen('loginscreen').ids.login_email.text
        self.strng.get_screen('profilescreen').ids.ftype.text = friend_type
        my_friends = '{"Friends": "%s"}' % friend_type
        requests.patch("" % updatetrophy,
                       data=my_friends)

    def send_temp(self, sendtemp):
        sendtemplate = self.strng.get_screen('loginscreen').ids.login_email.text
        send_temp = '{"Send Template to": "%s"}' % sendtemp
        requests.patch("" % sendtemplate,
                       data=send_temp)


''' Milestone= User may see the workout streak here, User must update everyday workout to update the streak
    def milestone_steak(self):
        #-Set the images in the change_routine
        banner_grid = self.root.ids['home_screen'].ids['banner_grid']
        routinePlan = data['routines']
        if routinePlan != "":
            routinePlan_keys = list(routinePlan.keys())
            streak = helperfunctions.count_routine_streak(routine)
            if str(streak) == 0:
                streak_label.text = "0 Day Streak. Go workout!"
            else:
                streak_label.text = str(streak) + " Day Streak!"

            #-Sort exercise by date then reverse (LATEST ON TOP!)
            routine_keys.sort(key=lambda value: datetime.strptime(routine[value]['date'], "%m/%d/%Y"))
            routine_keys = routine_keys[::-1]
            for routine_key in routine_keys:
                routine = routines[routine_key]

                #-Populate exercise grid in home screen
                R = routineBanner(routine_image=routine['routine_image'], description=routine['description'],
                                  type_image=routine['type_image'], number=routine['number'], units=routine['units'],
                                  likes=routine['likes'], date=routine['date'])
                banner_grid.add_widget(W)

        self.change_screen("home_screen", "None")
    '''

app = FoodyCoachApp()
app.run()
