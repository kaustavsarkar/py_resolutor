import math
import os
from os import listdir
from os.path import isdir, join
from typing import List

import cv2 as cv

base_resolution: float = 4
base_directory: str = "/home/kaustav/work/adminssions/100marks/images"
four_x_file_path: str = "/home/kaustav/work/adminssions/100marks/images/4x"
resolutions: List[float] = [3, 2, 1.5, 1]


def read_image(image_path: str):
	"""
	Returns the image read from the image path.
	:param image_path:
	:return:
	"""
	return cv.imread(image_path)


def read_base_folder(base_path: str) -> dict:
	"""
	Reads all images present in the base path. The images provided in the base
	path are considered to be of default / max size and other images shall be
	created based upon the default image size.
	:param base_path: path from where image paths are to be identified.
	:return: list of images paths to be processed.
	"""
	four_x_images: dict = { }
	for file in listdir(four_x_file_path):
		four_x_images[file] = join(base_path, file)
	return four_x_images


def create_directories(dir_names: list, base_path: str):
	"""
	Creates directories for required resolutions if not already present.
	:param dir_names: required resolutions.
	:param base_path: base path where 4x folder is located.
	:return: void
	"""
	for dir_name in dir_names:
		image_dir = join(base_path, str(dir_name) + 'x')
		if not isdir(image_dir):
			os.mkdir(image_dir)


def resize_image(image_path: str, image_resolution: float):
	image = read_image(image_path)
	current_height, current_width = image.shape[0:-1]
	ratio = image_resolution / base_resolution
	dimensions = (
		math.ceil(current_width * ratio), math.ceil(current_height * ratio))
	return cv.resize(image, dimensions, interpolation=cv.INTER_AREA)


def save_resized_image(image, resolution: float, image_name: str):
	filename: str = join(join(base_directory, str(resolution) + 'x'),
	                     image_name)
	print(image_name)
	print(join(base_directory, str(resolution)))
	print(filename)
	cv.imwrite(filename, image)


def process():
	create_directories(resolutions, base_directory)
	default_image_paths = read_base_folder(four_x_file_path)
	for file_name, file_path in default_image_paths.items():
		for resolution in resolutions:
			resized_image = resize_image(file_path, resolution)
			save_resized_image(resized_image, resolution, file_name)


process()
