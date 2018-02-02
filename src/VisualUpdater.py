"""

User interface for configuring and running the HydroShare update utility

"""
import wx
from GuiComponents.VisualH2OMainWindow import VisualH2OWindow
from Common import *

__title__ = 'Visual H20 Utility'


def main():
    APP_SETTINGS = Common(sys.argv)
    app = wx.App()
    frame = VisualH2OWindow(None, -1, __title__)
    app.MainLoop()


if __name__ == "__main__":
    main()
