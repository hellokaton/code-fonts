# coding=utf-8

from vanilla import *
from defconAppKit.windows.baseWindow import BaseWindowController
from mojo.events import addObserver, removeObserver
import math

class ShowMouseCoordinatesTextBox(TextBox):
    """
    A vanilla text box with some goodies about the mouse.
    """
    def __init__(self, *args, **kwargs):
		self.observers = {"mouseMoved", "mouseDragged", "mouseUp"}
		# initialize the parent object, and add all of the observers 
        super(ShowMouseCoordinatesTextBox, self).__init__(*args, **kwargs)
        addObserver(self, "mouseMoved", "mouseMoved")
        addObserver(self, "mouseDragged", "mouseDragged")
        addObserver(self, "mouseUp", "mouseUp")
    
    def mouseMoved(self, info):
        point = info["point"]
        text = u"%.0f %.0f" % (point.x, point.y)
        self.set(text)

    def mouseDragged(self, info):
        point = info["point"]
        positionSymbol = unichr(8982)
        deltaPoint = info["delta"]
        angle = math.degrees(math.atan2(deltaPoint.y, deltaPoint.x))
        distance = math.hypot(deltaPoint.x, deltaPoint.y)
        text = u"%.0f %.0f   %.0f %.0f   %.2f°   %.0f" % (point.x, point.y, deltaPoint.x, deltaPoint.y, angle, distance)
        self.set(text)
        
    def mouseUp(self, info):
        point = info["point"]
        text = u"%.0f %.0f" % (point.x, point.y)
        self.set(text)

    def _breakCycles(self):
        super(ShowMouseCoordinatesTextBox, self)._breakCycles()
        removeObserver(self, "mouseMoved")
        removeObserver(self, "mouseDragged")
        removeObserver(self, "mouseUp")

class ShowMouseCoordinates(BaseWindowController):
    """
    Attach a vanilla text box to a window.
    """
    def __init__(self):
        addObserver(self, "glyphWindowDidOpen", "glyphWindowDidOpen")

    def glyphWindowDidOpen(self, info):
        window = info["window"]
        vanillaView = ShowMouseCoordinatesTextBox((20, -30, -20, 22), "", alignment="left", sizeStyle="mini")
        superview = window.editGlyphView.enclosingScrollView().superview()
        view = vanillaView.getNSTextField()
        frame = superview.frame()
        vanillaView._setFrame(frame)
        superview.addSubview_(view)
                
    def windowCloseCallback(self, sender):
        super(ShowMouseCoordinatesTextBox, self).windowCloseCallback(sender)
        removeObserver(self, "glyphWindowDidOpen")

ShowMouseCoordinates()
