import os
import argparse

dtu_scenes = ['scan24', 'scan37', 'scan40', 'scan55', 'scan63', 'scan65', 'scan69', 'scan83', 'scan97', 'scan105', 'scan106', 'scan110', 'scan114', 'scan118', 'scan122']
tnt_scenes = ['Barn', 'Caterpillar', 'Ignatius', 'Truck', 'Meetingroom', 'Courthouse']
m360_scenes = ["bicycle", "flowers", "garden", "stump", "treehill", "room", "counter", "kitchen", "bonsai"]

def rename_files(folder):
    if not os.path.isdir(folder):
        print(f"❌ Folder not found: {folder}")
        return

    normals_path = os.path.join(folder, "normals")
    files = os.listdir(normals_path)
    renamed_count = 0

    for filename in files:
        if "_normal" not in filename:
            continue

        old_path = os.path.join(normals_path, filename)

        stem, ext = os.path.splitext(filename)
        new_name = stem.replace("_normal", "") + ext
        new_path = os.path.join(normals_path, new_name)

        # 防止覆盖已有文件
        if os.path.exists(new_path):
            print(f"⚠️ Skip (target exists): {new_name}")
            continue

        os.rename(old_path, new_path)
        print(f"✔ Renamed: {filename} → {new_name}")
        renamed_count += 1

    print(f"\n✅ Done. Renamed {renamed_count} files.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch remove '_normal' from filenames")
    parser.add_argument("--folder", default='/media/wangsc/T7/datasets/dtu_dataset/dtu', help="Folder containing normal images")
    args = parser.parse_args()

    for scene in dtu_scenes:
        rename_files(args.folder + "/" + scene)
