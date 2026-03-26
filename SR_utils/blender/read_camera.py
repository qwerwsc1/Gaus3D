## 在blender的scripts中渲染图像

import bpy, math

# ========= 1) 相机参数 =========

cam_loc = (
1.1925366015069097, 0.3810943478448384, -2.3167104770817306
)
cam_rot_deg = (
196.62487806862669, -20.42983688619551, -19.185832094452437
)  # Euler XYZ, degrees

focal_mm = 67.04         # Focal Length
shift_x, shift_y = 0.0, 0.0
clip_start, clip_end = 0.1, 100.0

# 分辨率（可选）
res_x, res_y = 777, 581

# ========= 2) 灯光参数（Point Light） =========
light_name   = "Light"
light_type   = "POINT"     # 'POINT' / 'SUN' / 'SPOT' / 'AREA'
light_loc    = (
1.1925366015069097, 0.3810943478448384, -2.3167104770817306
)
light_rot_deg= (
196.62487806862669, -20.42983688619551, -19.185832094452437
)  # 对 POINT 旋转无效
power        = 110      # Power / Energy
normalize    = True        # 仅对支持的光型设置（AREA/部分版本的SPOT）
radius       = 0.1         # 阴影软硬 (shadow_soft_size)
use_shadow   = True        # 勾选 Shadow

# ========= 工具函数 =========
def deg2rad(e): return tuple(math.radians(v) for v in e)

def ensure_camera():
    cam = bpy.context.scene.camera
    if cam is None:
        for ob in bpy.context.scene.objects:
            if ob.type == 'CAMERA':
                bpy.context.scene.camera = ob
                return ob
        cam_data = bpy.data.cameras.new("Camera")
        cam = bpy.data.objects.new("Camera", cam_data)
        bpy.context.scene.collection.objects.link(cam)
        bpy.context.scene.camera = cam
    return cam

def ensure_light(name, ltype='POINT'):
    ob = bpy.data.objects.get(name)
    if ob and ob.type == 'LIGHT':
        ob.data.type = ltype
        return ob
    ldat = bpy.data.lights.new(name=name, type=ltype)
    ob = bpy.data.objects.new(name, ldat)
    bpy.context.scene.collection.objects.link(ob)
    return ob

# ========= 相机 =========
cam = ensure_camera()
cam.rotation_mode = 'XYZ'
cam.location = cam_loc
cam.rotation_euler = deg2rad(cam_rot_deg)

cd = cam.data
cd.type = 'PERSP'
cd.lens = focal_mm
cd.lens_unit = 'MILLIMETERS'
cd.shift_x = shift_x
cd.shift_y = shift_y
cd.clip_start = clip_start
cd.clip_end = clip_end

# 可选分辨率
scene = bpy.context.scene
scene.render.resolution_x = res_x
scene.render.resolution_y = res_y

# ========= 灯光 =========
Lobj = ensure_light(light_name, light_type)
Lobj.location = light_loc
Lobj.rotation_mode = 'XYZ'
Lobj.rotation_euler = deg2rad(light_rot_deg)  # 对 POINT 不起作用，保留无害

L = Lobj.data
L.type = light_type
L.energy = power
L.shadow_soft_size = radius
L.use_shadow = use_shadow

# 只有在支持的光型/版本上才设置 use_normalized，避免报错
if hasattr(L, "use_normalized") and light_type in {"AREA", "SPOT"}:
    L.use_normalized = normalize

print("[OK] Camera & Light updated without errors.]")


## 在blender的scripts中渲染图像

import bpy, math

# ========= 1) 相机参数 =========

cam_loc = (
1.1925366015069097, 0.3810943478448384, -2.3167104770817306
)
cam_rot_deg = (
196.62487806862669, -20.42983688619551, -19.185832094452437
)  # Euler XYZ, degrees

focal_mm = 67.04         # Focal Length
shift_x, shift_y = 0.0, 0.0
clip_start, clip_end = 0.1, 100.0

# 分辨率（可选）
res_x, res_y = 777, 581

# ========= 2) 灯光参数（Point Light） =========
light_name   = "Light"
light_type   = "POINT"     # 'POINT' / 'SUN' / 'SPOT' / 'AREA'
light_loc    = (
1.1925366015069097, 0.3810943478448384, -2.3167104770817306
)
light_rot_deg= (
196.62487806862669, -20.42983688619551, -19.185832094452437
)  # 对 POINT 旋转无效
power        = 110      # Power / Energy
normalize    = True        # 仅对支持的光型设置（AREA/部分版本的SPOT）
radius       = 0.1         # 阴影软硬 (shadow_soft_size)
use_shadow   = True        # 勾选 Shadow

# ========= 工具函数 =========
def deg2rad(e): return tuple(math.radians(v) for v in e)

def ensure_camera():
    cam = bpy.context.scene.camera
    if cam is None:
        for ob in bpy.context.scene.objects:
            if ob.type == 'CAMERA':
                bpy.context.scene.camera = ob
                return ob
        cam_data = bpy.data.cameras.new("Camera")
        cam = bpy.data.objects.new("Camera", cam_data)
        bpy.context.scene.collection.objects.link(cam)
        bpy.context.scene.camera = cam
    return cam

def ensure_light(name, ltype='POINT'):
    ob = bpy.data.objects.get(name)
    if ob and ob.type == 'LIGHT':
        ob.data.type = ltype
        return ob
    ldat = bpy.data.lights.new(name=name, type=ltype)
    ob = bpy.data.objects.new(name, ldat)
    bpy.context.scene.collection.objects.link(ob)
    return ob

# ========= 相机 =========
cam = ensure_camera()
cam.rotation_mode = 'XYZ'
cam.location = cam_loc
cam.rotation_euler = deg2rad(cam_rot_deg)

cd = cam.data
cd.type = 'PERSP'
cd.lens = focal_mm
cd.lens_unit = 'MILLIMETERS'
cd.shift_x = shift_x
cd.shift_y = shift_y
cd.clip_start = clip_start
cd.clip_end = clip_end

# 可选分辨率
scene = bpy.context.scene
scene.render.resolution_x = res_x
scene.render.resolution_y = res_y

# ========= 灯光 =========
Lobj = ensure_light(light_name, light_type)
Lobj.location = light_loc
Lobj.rotation_mode = 'XYZ'
Lobj.rotation_euler = deg2rad(light_rot_deg)  # 对 POINT 不起作用，保留无害

L = Lobj.data
L.type = light_type
L.energy = power
L.shadow_soft_size = radius
L.use_shadow = use_shadow

# 只有在支持的光型/版本上才设置 use_normalized，避免报错
if hasattr(L, "use_normalized") and light_type in {"AREA", "SPOT"}:
    L.use_normalized = normalize

print("[OK] Camera & Light updated without errors.]")
