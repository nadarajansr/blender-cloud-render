import bpy
import os

# 1. Output directory inside Kaggle
output_dir = "/kaggle/working/renders/"
os.makedirs(output_dir, exist_ok=True)

# 2. Configure Cycles render engine for cloud GPU
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.device = 'GPU'

# Render resolution settings (e.g., 1920x1080 per camera view)
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100

# Enable GPU devices in Blender Preferences
prefs = bpy.context.preferences.addons['cycles'].preferences
prefs.get_devices()
for device in prefs.devices:
    device.use = True

# 3. Render each camera view (Front, Left, Right)
camera_names = ["Camera_Front", "Camera_Left", "Camera_Right"]

for cam_name in camera_names:
    cam_obj = bpy.data.objects.get(cam_name)
    if cam_obj:
        scene.camera = cam_obj
        output_filepath = os.path.join(output_dir, f"{cam_name.lower()}.png")
        scene.render.filepath = output_filepath
        
        print(f"Rendering view for {cam_name}...")
        bpy.ops.render.render(write_still=True)
        print(f"Saved render to {output_filepath}")
    else:
        print(f"Warning: Camera '{cam_name}' not found in scene.")

print("All 3 camera views successfully rendered!")