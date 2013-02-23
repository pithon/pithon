import thread, time, pygame

class Loader:
    def __init__(self, images, screen, position_x=0, position_y=0, loader_x=0, loader_y=100):
        self.images=images
        self.screen=screen
        self.message="Initilizing"
        self.run=True
        self.position_x=position_x
        self.position_y=position_y
        self.loader_x=loader_x
        self.loader_y=loader_y
    def set_message(self, message):
        self.message=message
    def _start_thread(self, interval):
        i=0
        while self.run:
            screen.fill((0,0,0))
            time.sleep(interval)
            self.screen.blit(images[i], 
                             pygame.rect.Rect(self.position_x, self.position_y, images[0].get_width(), images[0].get_height()))
            #self.screen.blit(pygame.font.SysFont("", 20).render(self.message), 
            #                 pygame.rect.Rect(self.loader_x, self.loader_y, 0,0))
            i=i+1
            if i==len(self.images): i=0
        pygame.display.flip()
    def start_thread(self, interval=0.2):
        self.run=True
        #thread.start_new_thread(self._start_thread, (interval,))
        self._start_thread(interval)
    def stop_thread(self):
        self.run=False

pygame.init()
screen=pygame.display.set_mode((800,600))
images=[pygame.image.load("pithon_loader/loader1.png"),
        pygame.image.load("pithon_loader/loader2.png"),
        pygame.image.load("pithon_loader/loader3.png"),
        pygame.image.load("pithon_loader/loader4.png"),
        pygame.image.load("pithon_loader/loader5.png"),
        pygame.image.load("pithon_loader/loader6.png"),
        pygame.image.load("pithon_loader/loader7.png"),
        pygame.image.load("pithon_loader/loader8.png"),
        pygame.image.load("pithon_loader/loader9.png")]
l=Loader(images, screen)
l.start_thread()
