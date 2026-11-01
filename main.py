import pygame
import time
import os

pygame.init()
pygame.mixer.init()

# Load song
pygame.mixer.music.load("song.mp3")

lyrics = [
    "Maybe I just wanna be yours",
    "I wanna be yours",
    "I wanna be yours",
    "Wanna be yours",
    "Wanna be yours",
    "Wanna be yours....."
]

# [Start time, End time] in seconds
timings = [
    [0.0, 3.0],
    [3.0, 6.0],
    [6.0, 9.0],
    [9.0, 12.0],
    [12.0, 15.0],
    [15.0, 19.8]
]

def show_lyrics():
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():

        current_time = pygame.mixer.music.get_pos() / 1000

        os.system("cls" if os.name == "nt" else "clear")

        print("\n\n       ♡ I WANNA BE YOURS ♡\n")

        for i, line in enumerate(lyrics):

            start, end = timings[i]

            if current_time >= end:
                print("       " + line)

            elif current_time >= start:
                progress = (current_time - start) / (end - start)

                chars = int(progress * len(line))

                print("       " + line[:chars])

            else:
                break

        time.sleep(0.03)

show_lyrics()

pygame.quit()