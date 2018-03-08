import os

os.system("ls ../data/ > main_folders.txt")

with open("main_folders.txt") as f:
	lines = f.readlines()

with open("final_names.txt", 'a') as f:
	for line in lines:
		line = line.strip()
		if line.find(".") == -1:
			os.system("ls ../data/{}/ > tmp_names.txt".format(line))
			with open("tmp_names.txt") as g:
				sublines1 = g.readlines()
				for l in sublines1:
					l = l.strip()
					if l.find(".") == -1:
						os.system("ls ../data/{}/{}/ > tmp_names2.txt".format(line, l))
						with open("tmp_names2.txt") as h:
							sublines2 = h.readlines()
							for l2 in sublines2:
								l2 = l2.strip()
								l2 = "\ ".join(l2.split(" "))
								if l2.find(".txt") == -1:
									os.system("ls ../data/{}/{}/{}/ > tmp_file_names.txt".format(line, l, l2))
									with open("tmp_file_names.txt") as k:
										text_file_names = k.readlines()
										for tfn in text_file_names:
											tfn = tfn.strip()
											if tfn.find(".txt") != -1:
												print(line+"/"+l+"/"+l2+"/"+tfn, file=f)
									os.system("rm tmp_file_names.txt")
						os.system("rm tmp_names2.txt")
			os.system("rm tmp_names.txt")