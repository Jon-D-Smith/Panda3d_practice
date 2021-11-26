from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Loading the Scene
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Adding a spin camera Task
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Adding the Panda
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005,0.005,0.005)
        self.pandaActor.reparentTo(self.render)
        self.pandaActor.loop("walk")
        # function to spin the camera
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.9
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

app = MyApp()
app.run()