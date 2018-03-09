#### get gnbk files and change name
#### argv[1] = path to the original folder with contig files

import os
import shutil
import sys

old_folder = "home/sales001/assembly_per_georg/Cr15_analysis/3_BGC/antismash_full/contigs_Cr15_metaspades"      #sys.argv[1]  #  "/path/to/folder"
#new_folder = "/Users/catarinaloureiro/PycharmProjects/assemblies/gbk_Cr15_megahit"

print("old folder ", old_folder)
dir_path = old_folder.split("/")
#print(len(dir_path))
# print(dir_path)

items = ""
if old_folder.endswith('/'):
    items = (int(len(dir_path))-2)
else:
    items = (int(len(dir_path))-1)

root_dir = ("/".join(dir_path[:items])) + "/"
print("root dir ", root_dir)

sample_names = (dir_path[items]).split("_")

sample_names_x = []
for name in sample_names:
    # print (name)
    if name.startswith("Cr") or name.startswith("me"):
        sample_names_x.append(name)
# print(sample_names_x)

sample = "_".join(sample_names_x)
sample_loc = "gbk_" + sample

#print(sample_names)
#print(sample)

new_path = []
new_path.append(root_dir)
new_path.append(sample_loc)
new_dir_path = ("".join(new_path)) + "/"
print("new dir path ", new_dir_path)

# if not os.path.exists(new_dir_path):
#     os.makedirs(new_dir_path)

last = (int(len(sample_names))-1)
#print(last)

# if (sample_names[last]).startswith('megahit'):
#
#     count = 0
#     for file in os.listdir(old_folder):
#         count += 1
#
#         if file.endswith('final.gbk'):
#             continue
#
#         elif file.endswith('.gbk'):
#             # print(file)
#             filenames = file.split(".")[:2]
#             # print(filenames)
#
#             new_filenames = "_".join(filenames)
#             # print(new_filenames)
#
#             final_file = sample + "_" + new_filenames + ".gbk"
#             # print(final_file)
#
#             old_file_path = old_folder + "/" + file
#             # print(old_file_path)
#             new_file_path = new_dir_path + final_file
#             # print(new_file_path)
#
#             # if final_file not in os.listdir(new_dir_path):
#             #     shutil.copy(old_file_path, new_file_path)
#
# #        print(file)
# #         if count == 5:
# #             break
#
# elif (sample_names[last]).startswith('metaspades'):
#     count = 0
#     for file in os.listdir(old_folder):
#         count += 1
#
#         if file.endswith('final.gbk'):
#             continue
#
#         elif file.endswith('.gbk'):
#             # print(file)
#             filenames = file.split(".")[:4]
#             # print(filenames)
#
#             new_filenames = "".join(filenames)
#             # print(new_filenames)
#
#             final_file = sample + "_" + new_filenames + ".gbk"
#             # print(final_file)
#
#             old_file_path = old_folder + "/" + file
#             # print(old_file_path)
#             new_file_path = new_dir_path + final_file
#             # print(new_file_path)
#
#             # if final_file not in os.listdir(new_dir_path):
#             #     shutil.copy(old_file_path, new_file_path)

        # if count == 5:
        #     break

