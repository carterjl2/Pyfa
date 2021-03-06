from gui.contextMenu import ContextMenu
from gui.itemStats import ItemStatsDialog
import eos.types
import gui.mainFrame
import service
import gui.globalEvents as GE
import wx

class Cargo(ContextMenu):
    def __init__(self):
        self.mainFrame = gui.mainFrame.MainFrame.getInstance()

    def display(self, srcContext, selection):
        # Make sure context menu registers in the correct view
        if srcContext not in ("marketItemGroup", "marketItemMisc") or self.mainFrame.getActiveFit() is None:
            return False
        return True

    def getText(self, itmContext, selection):
        return "Add {0} to Cargo".format(itmContext)

    def activate(self, fullContext, selection, i):
        sFit = service.Fit.getInstance()
        fitID = self.mainFrame.getActiveFit()

        typeID = int(selection[0].ID)
        sFit.addCargo(fitID, typeID)
        self.mainFrame.additionsPane.select("Cargo")
        wx.PostEvent(self.mainFrame, GE.FitChanged(fitID=fitID))

Cargo.register()
