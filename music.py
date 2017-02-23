import pygame
import time
import threading
import random
import display

class Music(pygame.mixer.Sound):
    def __init__(self, filename, singer, title):
        pygame.mixer.Sound.__init__(self, filename)
        self.singer = singer
        self.title = title
        
class MusicThread(threading.Thread):
    def __init__(self):
        pygame.init()
        threading.Thread.__init__(self)
        
        self.__suspend = False
        self.__exit = False
        self.__pause = False
        self.song_list = []
        self.song_list.append(Music("RedVelvet RussianRoulette.wav", "RedVelvet", "RussianRoulette"))
        self.song_list.append(Music("Twice TT.wav", "Twice", "TT"))
        self.song_list.append(Music("ZICO Bermuda.wav", "Zico", "Bermuda"))
        self.now_song = None
        self.next_song = None
        self.flag_next = False
        self.power = False
        self.volume = 0.5

    def play_music_seq(self):
        while True:
            for i in range(0, len(self.song_list)):
                self.now_song = self.song_list[i]
                self.now_song.set_volume(self.volume)
                print("song start: " + ' - '.join(self.get_music_info()))
                self.song_list[i].play()
                while not self.flag_next and self.power:
                    pass
                if not self.power:
                    pygame.mixer.stop()
                    break
                pygame.mixer.fadeout(1000)
                time.sleep(1)
                self.flag_next = False

            if not self.power:
                break
        
    def run(self):
        while(True):
            while not self.power:
                pass
            self.play_music_seq()
            if self.__exit:
                break
        print("thread stop")
        pygame.mixer.stop()

    def play_next_music(self):
        self.flag_next = True
        
    def pause(self):
        if not self.__pause:
            print("music pause...")
            pygame.mixer.pause()
            self.__pause = True
            
    def unpause(self):
        if self.__pause:
            print("music unpause...")
            pygame.mixer.unpause()
            self.__pause = False
         
    def exit(self):
        self.__exit = True
        if self.power:
            self.push_power_switch()
        
    def push_power_switch(self):
        self.power = not self.power
        self.now_song = None
        
    def get_music_info(self):
        if self.now_song == None:
            return ["None", "None"]
        return [self.now_song.singer, self.now_song.title]

    def get_current_info(self, num):
        if self.now_song == None:
            return ["None", "None"]
        self.next_song = self.song_list[num]
        return [self.next_song.singer, self.next_song.title]

    def volume_up(self):
        if self.now_song != None:
            print("volume up...")
            self.volume += 0.1
            self.now_song.set_volume(self.volume)

    def volume_down(self):
        if self.now_song != None:
            print("volume down...")
            self.volume -= 0.1
            self.now_song.set_volume(self.volume)
