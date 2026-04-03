import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"The Alarm set for {alarm_time}")
    ringtone = "alarm_clock_old.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Wake Up..!")
            is_running = False

            pygame.mixer.init()
            pygame.mixer.music.load(ringtone)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the Alarm Time (HH:MM:SS):")
    set_alarm(alarm_time)
