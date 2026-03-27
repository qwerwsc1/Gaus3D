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


import bpy
import math

# ========= 1) 相机参数 =========
cam_loc = (-0.6112140519550432,0.23841978822770363,4.346691734195055)
cam_rot_deg = (2.4364557619498726, 16.63132954544926, -177.06094764241905)

focal_mm = 21.4
shift_x, shift_y = 0.0, 0.0
clip_start, clip_end = 0.1, 100.0
res_x, res_y = 978, 544

# ========= 2) 灯光参数 =========
light_name = "Light"
light_type = "AREA"   # 改成 SUN
light_loc = (-0.6112140519550432,0.23841978822770363,4.346691734195055)
light_rot_deg = (2.4364557619498726, 16.63132954544926, -177.06094764241905)
power = 170.0
use_shadow = True

# ========= 3) 材质参数 =========
target_obj_name = None
base_color = (0.749, 0.471, 0.349, 1.0)   # rgb(191,120,89)
emission_strength = 0.25                  # 给一点自发光，防止颜色被光照洗掉

def deg2rad(e):
    return tuple(math.radians(v) for v in e)

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

def ensure_light(name, ltype='SUN'):
    ob = bpy.data.objects.get(name)
    if ob and ob.type == 'LIGHT':
        ob.data.type = ltype
        return ob
    ldat = bpy.data.lights.new(name=name, type=ltype)
    ob = bpy.data.objects.new(name, ldat)
    bpy.context.scene.collection.objects.link(ob)
    return ob

def make_clay_material(mat_name="ClayOrange"):
    mat = bpy.data.materials.get(mat_name)
    if mat is None:
        mat = bpy.data.materials.new(mat_name)

    mat.use_nodes = True
    nt = mat.node_tree
    nodes = nt.nodes
    links = nt.links
    nodes.clear()

    out = nodes.new(type="ShaderNodeOutputMaterial")
    out.location = (500, 0)

    diffuse = nodes.new(type="ShaderNodeBsdfDiffuse")
    diffuse.location = (0, 100)
    diffuse.inputs["Color"].default_value = base_color

    emission = nodes.new(type="ShaderNodeEmission")
    emission.location = (0, -80)
    emission.inputs["Color"].default_value = base_color
    emission.inputs["Strength"].default_value = emission_strength

    mix = nodes.new(type="ShaderNodeAddShader")
    mix.location = (250, 0)

    links.new(diffuse.outputs["BSDF"], mix.inputs[0])
    links.new(emission.outputs["Emission"], mix.inputs[1])
    links.new(mix.outputs["Shader"], out.inputs["Surface"])

    return mat

def assign_material_to_object(obj, mat):
    if obj.type != 'MESH':
        return
    obj.data.materials.clear()
    obj.data.materials.append(mat)

def assign_material_scene_wide(mat, target_obj_name=None):
    if target_obj_name is not None:
        obj = bpy.data.objects.get(target_obj_name)
        if obj is None:
            print(f"[Warn] Object '{target_obj_name}' not found.")
            return
        assign_material_to_object(obj, mat)
    else:
        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH':
                assign_material_to_object(obj, mat)

scene = bpy.context.scene

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

scene.render.resolution_x = res_x
scene.render.resolution_y = res_y

# ========= 渲染/色彩管理 =========
scene.render.engine = 'BLENDER_EEVEE'   # 或 CYCLES
scene.view_settings.view_transform = 'Standard'
scene.view_settings.look = 'None'
scene.view_settings.exposure = -0.3     # 降一点曝光
scene.view_settings.gamma = 1.0

# ========= 世界背景 =========
if scene.world is None:
    scene.world = bpy.data.worlds.new("World")
scene.world.use_nodes = True
bg = scene.world.node_tree.nodes.get("Background")
if bg is not None:
    bg.inputs[0].default_value = (0.85, 0.85, 0.85, 1.0)  # 不要太白
    bg.inputs[1].default_value = 0.4                       # 降低背景强度

# ========= 灯光 =========
Lobj = ensure_light(light_name, light_type)
Lobj.location = light_loc
Lobj.rotation_mode = 'XYZ'
Lobj.rotation_euler = deg2rad(light_rot_deg)

L = Lobj.data
L.type = light_type
L.energy = power
if hasattr(L, "use_shadow"):
    L.use_shadow = use_shadow

# ========= 材质 =========
mat = make_clay_material()
assign_material_scene_wide(mat, target_obj_name)

print("[OK] Updated camera, light, world, and material.")
