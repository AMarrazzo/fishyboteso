from fishing_mode import *


class FishEvent(ABC):
    @abstractmethod
    def onEnterCallback(self, previousMode):
        pass

    @abstractmethod
    def onExitCallback(self, currentMode):
        pass

class HookEvent(FishEvent):

    def onEnterCallback(self, previousMode):
        G.fishCaught += 1
        timeToHook = time.time() - G.stickInitTime
        print("HOOOOOOOOOOOOOOOOOOOOOOOK....... " + str(G.fishCaught) + " caught " + " in " + str(
            round_float(timeToHook)) + " secs")
        pyautogui.press('e')

    def onExitCallback(self, currentMode):
        pass


class LookEvent(FishEvent):

    def onEnterCallback(self, previousMode):
        Record.HaltExe()
        pyautogui.press('e')

    def onExitCallback(self, currentMode):
        pass


class IdleEvent(FishEvent):

    def __init__(self, use_net):
        self.use_net = use_net

    def onEnterCallback(self, previousMode):
        if self.use_net:
            net.sendHoleDeplete(G.fishCaught)

        if previousMode.name == "hook":
            print("HOLE DEPLETED")
        elif previousMode.name == "stick":
            print("FISHING INTERRUPTED")

        G.fishCaught = 0
        Record.UnHaltExe()

    def onExitCallback(self, currentMode):
        pass


class StickEvent(FishEvent):

    def onEnterCallback(self, previousMode):
        G.stickInitTime = time.time()

    def onExitCallback(self, currentMode):
        pass
