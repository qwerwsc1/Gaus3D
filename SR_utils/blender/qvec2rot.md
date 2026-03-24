## 从json文件中提取信息，并将旋转矩阵转换成blender的欧拉角
import json
from scipy.spatial.transform import Rotation as R

# ✅ 你提供的旋转转欧拉函数
def rot_2_euler_in_blender(rotation_matrix):
    r = R.from_matrix(rotation_matrix)
    eu = r.as_euler('xyz', degrees=True)
    eu[0] = eu[0] + 180  # X 加 180°
    return eu


def print_all_cameras(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    def process_obj(obj):
        if isinstance(obj, dict) and "rotation" in obj and "id" in obj:
            print("\n=======================================")
            print(f"Camera id: {obj['id']}")
            print(json.dumps(obj, indent=4, ensure_ascii=False))

            rot = obj["rotation"]
            euler = rot_2_euler_in_blender(rot)

            print(f"Euler XYZ (Degrees)：{euler[0]}, {euler[1]}, {euler[2]}")
            print(f"X = {euler[0]}")
            print(f"Y = {euler[1]}")
            print(f"Z = {euler[2]}")
            print("=======================================\n")

        if isinstance(obj, dict):
            for v in obj.values():
                process_obj(v)
        elif isinstance(obj, list):
            for v in obj:
                process_obj(v)

    process_obj(data)


if __name__ == "__main__":
    json_file = "/media/wangsc/T7/outputs/2dgs/dtu/scan37/cameras.json"
    print_all_cameras(json_file)
