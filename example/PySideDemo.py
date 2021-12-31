# Sample Workflow Integration script

# some element IDs
winID = "com.blackmagicdesign.resolve.PySideDemo"

ui = fusion.UIManager
dispatcher = bmd.UIDispatcher(ui)

# check for existing instance
win = ui.FindWindow(winID)
if win:
    win.Show()
    win.Raise()
    exit()

winLayout = ui.VGroup([
    ui.Label({'Text': "A 2x2 grid of buttons", 'Weight': 1}),

    ui.HGroup({'Weight': 5}, [
        ui.Button({'ID': "myButton1", 'Text': "Go"}),
        ui.Button({'ID': "myButton2", 'Text': "Stop"}),
    ]),
    ui.VGap(2),
    ui.HGroup({'Weight': 5}, [
        ui.Button({'ID': "myButtonA", 'Text': "Begin"}),
        ui.Button({'ID': "myButtonB", 'Text': "End"}),
    ]),
]),

win = dispatcher.AddWindow(
    {
        'ID': winID,
        'Geometry': [100, 100, 600, 500],
        'WindowTitle': "Resolve Sample Workflow Script",
    },
    winLayout
)


def OnClose(ev):
    dispatcher.ExitLoop()


win.On[winID].Close = OnClose

# Main dispatcher loop
win.Show()
dispatcher.RunLoop()
