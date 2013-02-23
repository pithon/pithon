import sys, ocempgui
sys.path.append("..")
import core2

def show_title_screen():
    renderer=ocempgui.widgets.Renderer()
    renderer.create_screen(800,600)
    singleplayerbutton=ocempgui.widgets.Button("Single Player")
    singleplayerbutton.topleft = (550, 100)
    singleplayerbutton.set_size(100,50)
    joinserverbutton=ocempgui.widgets.Button("Join Server")
    joinserverbutton.topleft = (250, 200)
    hostserverbutton=ocempgui.widgets.Button("Host Server")
    hostserverbutton.topleft = (250, 300)
    singleplayerbutton.bottomright = (350, 125)
    quitbutton=ocempgui.widgets.Button("Quit")
    quitbutton.topleft = (250, 500)
    quitbutton.bottomright = (350, 525)
    quitbutton.connect_signal(ocempgui.widgets.Constants.SIG_CLICKED, quit)
    renderer.add_widget(singleplayerbutton)
    renderer.add_widget(joinserverbutton)
    renderer.add_widget(hostserverbutton)
    renderer.add_widget(quitbutton)
    renderer.start()

show_title_screen()