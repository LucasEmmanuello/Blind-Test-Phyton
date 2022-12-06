import random
import pygame

# List of songs to play in the blind test
songs = ["Songs/Doom.mp3"]

# Select a random song from the list
song = random.choice(songs)

# Initialize Pygame
pygame.init()

# Load the selected song and play it
pygame.mixer.music.load(song)
pygame.mixer.music.play()

# Wait for the user to guess the song
while pygame.mixer.music.get_busy():
    guess = input("Guess the song: ")
    if guess == song:
        print("Correct!")
        break
    else:
        print("Incorrect. Try again.")

# Stop the music when the user guesses the song
pygame.mixer.music.stop()
