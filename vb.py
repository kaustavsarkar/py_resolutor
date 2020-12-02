import os
from os import listdir
from os.path import isdir, join
from shutil import copy, make_archive
from typing import List

import cv2 as cv

import main

audio_extensions = [".mp3"]
vb_base_path = "/home/kaustav/work/adminssions/100marks/vb/"
vb_4x_image_path = "/home/kaustav/work/adminssions/100marks/vb/4x/images"
vb_4x_audio_path = "/home/kaustav/work/adminssions/100marks/vb/4x/audio"
resolutions: List[float] = [3, 2, 1.5, 1]


def create_directories(dir_names: list, base_path: str):
	for dir_name in dir_names:
		resolution_dir = join(base_path, str(dir_name) + 'x')
		image_dir = join(join(base_path, str(dir_name) + 'x'), 'images')
		audio_dir = join(join(base_path, str(dir_name) + 'x'), 'audio')
		if not isdir(resolution_dir):
			os.mkdir(resolution_dir)
		if not isdir(image_dir):
			os.mkdir(image_dir)
		if not isdir(audio_dir):
			os.mkdir(audio_dir)


def read_image_path(base_path: str):
	four_x_images: dict = { }
	for file in listdir(vb_4x_image_path):
		file_extension = os.path.splitext(file)[1]
		if file_extension in main.image_extensions:
			four_x_images[file] = join(base_path, file)
	return four_x_images


def save_resized_image(image, resolution: float, image_name: str):
	"""
	Saves image to the created directory of the particular resolution.
	:param image:
	:param resolution:
	:param image_name:
	:return:
	"""
	filename: str = join(
		join(join(vb_base_path, str(resolution) + 'x'), 'images'), image_name)
	print(image_name)
	print(join(vb_base_path, str(resolution)))
	print(filename)
	cv.imwrite(filename, image)


def read_mp3(base_path: str) -> dict:
	audio_file_paths: dict = { }
	for file in listdir(vb_4x_audio_path):
		file_extension = os.path.splitext(file)[1]
		if file_extension in audio_extensions:
			audio_file_paths[file] = join(base_path, file)
	return audio_file_paths


def process():
	create_directories(resolutions, vb_base_path)
	image_paths = read_image_path(vb_4x_image_path)
	audio_paths = read_mp3(vb_4x_audio_path)

	for image_name, image_path in image_paths.items():
		for resolution in resolutions:
			resized_image = main.resize_image(image_path, resolution)
			save_resized_image(resized_image, resolution, image_name)

	for audio_name, audio_path in audio_paths.items():
		for resolution in resolutions:
			copy(audio_path,
			     join(join(join(vb_base_path, str(resolution) + 'x'), 'audio'),
			          audio_name))

	path_4x = join(vb_base_path, str(4) + 'x')
	make_archive(str(path_4x), 'zip', path_4x)

	for resolution in resolutions:
		path = join(vb_base_path, str(resolution) + 'x')
		make_archive(str(path), 'zip', path)


if __name__ == '__main__':
	process()
