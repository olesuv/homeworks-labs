from gtts import gTTS
from pygame import mixer

def text_to_mp3(text, filename):
    tts = gTTS(text, lang='uk')
    tts.save(filename)

def play_mp3(filename):
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()

if __name__ == "__main__":
    user_input = input("Введіть текст, який ви хочете конвертувати в MP3: ")
    output_filename = input("Введіть назву вихідного файлу (з розширенням .mp3): ")

    text_to_mp3(user_input, output_filename)
    print(f'Файл {output_filename} успішно створено.')

    play_option = input("Ви хочете прослухати MP3? (так/ні): ")
    if play_option.lower() == "так":
        play_mp3(output_filename)
