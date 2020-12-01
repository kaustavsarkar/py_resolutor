import os
from os import listdir
from os.path import join
from shutil import copy

import main

audio_extensions = [".mp3"]


def read_mp3(base_path: str) -> dict:
	audio_file_paths: dict = { }
	for file in listdir(main.four_x_file_path):
		file_extension = os.path.splitext(file)[1]
		if file_extension in audio_extensions:
			audio_file_paths[file] = join(base_path, file)
	return audio_file_paths


def copy_mp3(base_path: str, resolutions: list, audio_file_paths: dict):
	for file_name, file_path in audio_file_paths.items():
		for resolution in resolutions:
			copy(file_path,
			     join(join(base_path, str(resolution) + 'x'), file_name))


def process():
	main.process()
	audio_file_dic = read_mp3(main.base_directory)
	copy_mp3(main.base_directory, main.resolutions, audio_file_dic)


if __name__ == '__main__':
	process()
