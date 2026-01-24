import os
from argparse import ArgumentParser

dtu_scenes = ['scan24', 'scan37', 'scan40', 'scan55', 'scan63', 'scan65', 'scan69', 'scan83', 'scan97', 'scan105', 'scan106', 'scan110', 'scan114', 'scan118', 'scan122']
tnt_scenes = ['Barn', 'Caterpillar', 'Ignatius', 'Truck', 'Meetingroom', 'Courthouse']
m360_scenes = ["bicycle", "flowers", "garden", "stump", "treehill", "room", "counter", "kitchen", "bonsai"]
parser = ArgumentParser(description="Full evaluation script parameters")
parser.add_argument('--dataset', "-dataset", required=True, type=str)
args, _ = parser.parse_known_args()

# all_scenes = []
# all_scenes.extend(dtu_scenes)
# all_scenes.extend(tnt_scenes)
# all_scenes.extend(m360_scenes)



common_args = ""
#for scene in dtu_scenes:
#for scene in tnt_scenes:
for scene in m360_scenes:
    source = args.dataset + "/" + scene
    print("python img2normal.py -s " + source)
    os.system("python img2normal.py -s " + source)
