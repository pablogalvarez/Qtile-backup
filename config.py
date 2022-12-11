import os
import re
import subprocess
from libqtile import layout, bar, widget, hook
from libqtile.config import Drag, Group, Key, Match, Screen
from libqtile.command import lazy

mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')

# BEGIN CODE FOR KEYS CONFIGURATION

keys = [
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "shift"], "f", lazy.layout.flip()),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
]

# END CODE FOR KEYS

# BEGIN CODE FOR GROUPS

groups = [
   Group(
       name="Terminal",
       layout="monadtall",
       label="",
   ),
   Group(
       name="Internet",
       layout="monadtall",
       label="",
       matches=[Match(wm_class=["firefox"])],
   ),
   Group(
       name="Development",
       layout="monadtall",
       label="",
       matches=[Match(wm_class=["code"])],
   ),
   Group(
       name="Other",
       layout="monadtall",
       label="",
   ),
]

for index, group in enumerate(groups, start=1):
    keys.extend([
        Key([mod], str(index), lazy.group[group.name].toscreen()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key([mod, "shift"], str(index), lazy.window.togroup(group.name) , lazy.group[group.name].toscreen()),
    ])

# END CODE FOR GROUPS

# BEGIN CODE FOR LAYOUTS

layout_config = {
    'border_focus': '#a151d3',
    'border_width': 2,
    'margin': 4,
}

layouts = [
    layout.MonadTall(**layout_config),
    layout.MonadWide(**layout_config),
    layout.Matrix(**layout_config),
    # layout.Floating(
    #     border_focus="#a151d3",
    #     border_width=2,
    # ),
]

# floating_layout = layout.Floating(float_rules=[
#     *layout.Floating.default_float_rules,
#     Match(wm_class='confirmreset'),
#     Match(wm_class='makebranch'),
#     Match(wm_class='maketag'),
#     Match(wm_class='ssh-askpass'),
#     Match(title='branchdialog')
#     Match(title='pinentry'),
#     Match(wm_class='Arcolinux-welcome-app.py'),
#     Match(wm_class='Arcolinux-calamares-tool.py'),
#     Match(wm_class='confirm'),
#     Match(wm_class='dialog'),
#     Match(wm_class='download'),
#     Match(wm_class='error'),
#     Match(wm_class='file_progress'),
#     Match(wm_class='notification'),
#     Match(wm_class='splash'),
#     Match(wm_class='toolbar'),
#     Match(wm_class='Arandr'),
#     Match(wm_class='feh'),
#     Match(wm_class='Galculator'),
#     Match(wm_class='archlinux-logout'),
#     Match(wm_class='xfce4-terminal'),
# ],  fullscreen_border_width = 0, border_width = 0)

# END CODE FOR LAYOUTS

# BEGIN CODE FOR SCREENS

colors = {
    'light': 'c0c5ce',
    'dark': '#0f101a',
}

widgets = {
    "groups": widget.GroupBox(
        font="CaskaydiaCove NF",
        fontsize=35,
        margin_y=3,
        margin_x=0,
        padding_y=6,
        padding_x=10,
        borderwidth=0,
        disable_drag=True,
        active='#ffffff',
        inactive='#4c566a',
        rounded=False,
        highlight_method="block",
        this_current_screen_border='#a151d3',
        foreground=colors['light'],
        background=colors['dark']
    ),
    "separator": widget.Sep(
        linewidth=0,
        padding=20,
        foreground=colors['light'],
        background=colors['dark']
    ),
    "window_desc": widget.WindowName(
        font="CaskaydiaCove NF",
        fontsize=15,
        foreground="#bd93f9",
        background=colors['dark'],
    ),
    "clock": widget.Clock(
        foreground="#000000",
        font='CaskaydiaCove NF',
        fontsize=15,
        background='#ffb86c',
        format="%d-%m-%Y %H:%M",
        padding=10,
    ),
    "ip": widget.TextBox(
        text='IP address -> %s' % re.search(r'inet ([0-9].)*', subprocess.check_output("ifconfig").decode())[0].split(' ')[1],
        background='#ff5555',
        font='CaskaydiaCove NF',
        fontsize=15,
        foreground='#000000',
        padding=10,
    ),
    "current_layout": widget.CurrentLayout(
        background='#bd93f9',
        font='CaskaydiaCove NF',
        fontsize=15,
        foreground='#000000',
        padding=10,
    ),
    "systray": widget.Systray()
}

screens = [
    Screen(
        top=bar.Bar(
            [widgets['groups'], widgets['separator'], widgets['window_desc'], widgets['ip'], widgets['current_layout'], widgets['clock']],
            size=30,
            opacity=1
        ),
    ),
]

# END CODE FOR SCREENS


# BEGIN CODE FOR MOUSE

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

# END CODE FOR MOUSE

dgroups_key_binder = None
dgroups_app_rules = []

main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"