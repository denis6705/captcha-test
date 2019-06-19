# -*- coding: utf-8 -*-

from pydub import AudioSegment


def create_wave(path_to_wave_files,beep_file, captcha_text, output_file):
    # Загружам наш бип файл - используем чтобы обозначить начало и конец результирующего файла
    beep = AudioSegment.from_wav(beep_file)
    sounds_cache = []
    # Загружаем наши цифры от 0 до 9
    for digit in range(10):
        sounds_cache.append(AudioSegment.from_wav(path_to_wave_files + str(digit) + ".wav"))
    # Начинаем собирать результирующий файл
    result = beep
    for char in captcha_text:
        result += sounds_cache[int(char)]
    result += beep
    result.export(output_file, format="wav")


def main():
    path_to_wave_files = "sounds/ru_digits/"
    beep_file = "sounds/beep.wav"
    output_file = "output.wav"

    create_wave(path_to_wave_files, beep_file, "4455", output_file)


if __name__ == "__main__":
    main()
    

