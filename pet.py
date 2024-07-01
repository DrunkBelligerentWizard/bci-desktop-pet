import tkinter as tk
import time
from PIL import Image
import random
from characters.fox import fox


class Pet():
    def __init__(self, petSize=0, groundLevel=-1, character=fox, useBCI=False):
        # the pet "profile"
        self.pet = character
        #the current direction
        self.dir = 'right'
        # how many cycles the pet has been moving in the current direction
        self.dirCount = 0
        # the current action the pet is performing
        self.action = 'run'
        self.lastAction = 'idle'
        self.actionsSinceLastIdle = 0
        self.idleCount = 0
        self.nonInteruptableAction = False
        
        self.window = tk.Tk()
        self.nextActionTS = time.time()
        
        # monitor resolution
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        
        # set a movment speed relative to the monitor resolution
        self.speed = (self.width+self.height)//1500
        self.zoomFac = 2*self.width//1440 if petSize == "Default" else int(petSize)
        #self.zoomFac = 4
        self.x = self.width // 10
        self.y = int(self.height - 2.66*self.pet["frameHeight"]) if groundLevel == -1 else self.height-groundLevel
        self.groundLevel = self.y
        
        # processes gifs into a form that works with tkinter and put in one dictionary
        self.gifs = self.create_tkinter_movement_gifs(self.pet)
        
        self.frame_index = 0
        self.img = self.gifs[self.dir][self.action][self.frame_index]

        # timestamp to check whether to advance frame
        self.timestamp = time.time()

        # set focushighlight to black when the window does not have focus
        self.window.config(highlightbackground='black')

        # make window frameless
        self.window.overrideredirect(True)

        # make window draw over all others
        self.window.attributes('-topmost', True)

        # turn black into transparency
        self.window.wm_attributes('-transparentcolor', 'black')

        # create a label as a container for our image
        self.label = tk.Label(self.window, bd=0, bg='black')
        # create a window of size 128x128 pixels, at coordinates 0,0
        self.window.geometry(f"{self.pet['frameHeight']* self.zoomFac}x{self.pet['frameWidth']* self.zoomFac}+{str(self.x)}+{str(self.y)}")

        # add the image to our label
        self.label.configure(image=self.img)

        # give window to geometry manager (so it will appear)
        self.label.pack()

        # run self.update() after 0ms when mainloop starts
        self.window.after(0, self.update_movment)
        self.window.mainloop()

    def update_movment(self):
        if not self.nonInteruptableAction:
            if time.time() > self.nextActionTS:
                self.nextActionTS += 0.5
                self.update_action()
            self.update_direction()
        # move left or right
        if self.action in ['idle', 'restAction1', 'restAction2']: pass
        elif self.dir == 'right':
            self.x += self.speed
            if self.action == 'jump':
                self.x += self.speed//2
                self.y -= self.speed//2
        elif self.dir == 'left':
            self.x -= self.speed
            if self.action == 'jump':
                self.x -= self.speed//2
                self.y -= self.speed//2
                
        if self.action == 'fall':
            if self.y >= self.groundLevel:
                self.action ='land'
                self.lastAction = 'fall'
                self.nonInteruptableAction = False
            else:
                self.y += self.speed
        if self.action == 'land':
            self.y = self.groundLevel
            

        # advance frame if a frames length of time has happened for the current animation
        if time.time() > self.timestamp + 1 / self.pet[self.dir][self.action]["fps"]:
            self.timestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            self.frame_index = (self.frame_index + 1) % self.pet[self.dir][self.action]["frameCount"]
            self.img = self.gifs[self.dir][self.action][self.frame_index]
            # swap from jumping to falling when the jump animation is complete
            if self.frame_index == 0 and self.action == 'jump':
                self.action = 'fall'
                self.lastAction = 'jump'
            

        # create the window
        self.window.geometry(f"{self.pet['frameHeight'] * self.zoomFac}x{self.pet['frameWidth']*self.zoomFac}+{str(self.x)}+{str(self.y)}")
        # add the image to our label
        self.label.configure(image=self.img)
        # give window to geometry manager (so it will appear)
        self.label.pack()

        # call update after 10ms
        self.window.after(10, self.update_movment)
        
    def update_direction(self):
        # if just becoming idle don't turn around
        if self.action == 'idle' and self.lastAction != 'idle':
            self.dirCount += 1
            return
        # increase chance of turning around on movement if character was idle
        dirIdleBias = 0.5 if self.lastAction == 'idle' and self.action != 'idle' else 0
        
        lastDir = self.dir
        
        # if the character will collide with the right edge of the screen
        if self.x + self.speed >= self.width:
                self.dir = 'left'
        # if the character will collide with the left edge of the screen
        elif self.x - self.speed <= 0:
            self.dir = 'right'  
        # if the character has been taking their actions in the same direction for specified amount of steps 
        elif self.dirCount >= 2:
            # change direction towards center of screen
            towardsCenter = random.random() > 1 - abs(self.x-self.width/2)/(192*self.width)
            if self.x - self.width/2 <= 0 and towardsCenter:
                self.dir = 'right'
            elif self.x - self.width/2 > 0 and towardsCenter:
                self.dir = 'left'
            # random chance to change direction if not already triggered to run towards the center
            elif random.random() > 0.8 - dirIdleBias:
                if self.dir == "right":
                    self.dir =='left'
                else: self.dir == 'right'
                
            
        if lastDir == self.dir:
            self.dirCount += 1
        else: self.dirCount = 1
    
    def update_action(self):
        tempLastAction = self.lastAction
        self.lastAction = self.action
        
        
        if tempLastAction == 'jump':
            self.action = 'fall'
        elif self.action == 'fall' and self.y >= self.groundLevel:
            self.nonInteruptableAction = False
            self.action = 'land'
        elif self.action == 'jump':
            self.action = 'jump'
        elif self.action != 'idle' and self.actionsSinceLastIdle >= 10 and random.random() > 1 - 0.02 * self.actionsSinceLastIdle:
            self.action = 'idle'
        elif self.lastAction == 'run' and random.random() > 0.975:
            self.action = 'jump'
            self.nonInteruptableAction = True
        elif self.action == 'idle' and self.idleCount > 5:
            rand = random.random()
            if rand > 0.7:
                self.action = 'run'
            elif rand < 0.2:
                self.action = 'restAction1'
            elif rand > 0.6: 
                self.action = 'restAction2'
            
        if self.action == 'land' and self.lastAction == 'land':
            self.action = 'run'
        if self.action != 'idle':
            self.actionsSinceLastIdle += 1
            self.idleCount = 0
        else: 
            self.idleCount +=1
            self.actionsSinceLastIdle = 0
            
        
    def get_frame_count(gif_path):
        with Image.open(gif_path) as img:
            return img.n_frames
        
    def create_tkinter_movement_gifs(self, pet):
        gifs = {"left": {}, "right":{}}
        for dir in gifs:
            for action in pet[dir]:
                gifs[dir][action] = [tk.PhotoImage(file=pet[dir][action]["path"], format='gif -index %i' % (i)).zoom( self.zoomFac, self.zoomFac) for i in range(pet[dir][action]["frameCount"])]
        return gifs

if __name__ == "__main__":
    Pet()