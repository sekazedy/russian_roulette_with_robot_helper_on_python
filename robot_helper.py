#My first python program

import os
import psutil
import sys
import shutil
import random


def duplicate_file(filename):
	if os.path.isfile(filename):
		newfile = filename + "_copy"
		shutil.copy(filename, newfile)
		if os.path.exists(newfile):
			print("File ", newfile, " was successfully created!")
			return True
		else:
			print("Error! Something went wrong while copying!")
			return False

def sys_info():
	print("Current DIR:", os.getcwd())
	print("Platform:", sys.platform)		#shows platform info
	print("File system encoding:", sys.getfilesystemencoding())		#shows file system encoding
	print("User info:", psutil.users())		#shows user info
	print("User login:", os.getlogin())		#shows user login
	print("CPU count:", psutil.cpu_count())		#shows CPU count

def delete_duplicates(file_dir):
	dup_cnt = 0
	file_list = os.listdir(file_dir)
	for f in file_list:
		fullname = os.path.join(file_dir, f)
		if fullname.endswith("_copy"):
			os.remove(fullname)
			if not os.path.exists(fullname):
				dup_cnt += 1
	return dup_cnt

def duplicate_files(dirname):
	file_list = os.listdir(dirname)
	i = 0
	while i < len(file_list):
		duplicate_file(file_list[i])
		i += 1

def random_delete(dirname):
	file_list = os.listdir(dirname)
	if file_list:
		i = random.randrange(0, len(file_list))
		fullname = os.path.join(dirname, file_list[i])
		if os.path.isfile(fullname):
			os.remove(fullname)
			print("File ", fullname, " was randomly deleted!")


def main():
	print("My first python program!")
	print("Hello, progger!")
	name = input("Speak your name: ")
	print("All hale the mighty", name)

	answer = ''
	while answer != "Q":
		answer = input("Are you about to get to work? (Y/N/Q):")
		if answer == 'Y':
			print("Allrighty, then! What we'll do?")
			print(" [1] - show file list")
			print(" [2] - show system info")
			print(" [3] - show process list")
			print(" [4] - copy file in current directory")
			print(" [5] - copy user specified file")
			print(" [6] - delete files from user specified dir")
			print(" [7] - delete random file from specified dir")
			do = int(input("Choose your DESTINY: "))

			if do == 1:
				print(os.listdir())
			elif do == 2:
				sys_info()
			elif do == 3:
				print(psutil.pids())	#shows current working processes IDs
			elif do == 4:
				#duplicate all files in directory, writing to their names postfix '_copy'
				duplicate_files('.')
			elif do == 5:
				filename = input("Specify file to copy: ")
				duplicate_file(filename)
			elif do == 6:
				file_dir = input("Specify directory: ")
				dup_cnt = delete_duplicates(file_dir)
				print(dup_cnt, " file duplicates were deleted!")
			elif do == 7:
				dirname = input("Write directory name: ")
				random_delete("test")
			else:
				pass
		elif answer == 'N':
			print("Get high and relax")
		elif answer == 'Q':
			pass
		else:
			print("Are you nuts?! Y OR N!")

if __name__ == "__main__":
	main()
