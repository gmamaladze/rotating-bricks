import bpy
import math
import mathutils

def spherical(radius, phi, theta):
    x = radius * math.sin(phi) * math.cos(theta)
    y = radius * math.sin(phi) * math.sin(theta)
    z = radius * math.cos(phi)
    return mathutils.Vector((x, y, z))

def show():
    scene = bpy.context.scene
    for obj in scene.objects:
        print(obj.name)

def remove(name):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[name].select = True
    bpy.ops.object.delete()

def light(at):
    bpy.ops.object.select_all(action='DESELECT')
    lamp_data = bpy.data.lamps.new(name='Lamp', type='POINT')
    lamp_data.energy = 10
    lamp_object = bpy.data.objects.new(name='Lamp', object_data=lamp_data)
    lamp_object.location = at
    bpy.context.scene.objects.link(lamp_object)

def camera(at):
    camera = bpy.data.objects['Camera']
    origin = mathutils.Vector((0, 0, 0))
    anchor = camera.matrix_world.to_translation()
    direction = origin - at
    rot_quat = direction.to_track_quat('-Z', 'Y')
    camera.rotation_euler = rot_quat.to_euler()
    camera.location = at

bpy.ops.import_scene.obj(filepath='/brick.obj')
remove('Cube')
remove('Plane')
remove('Lamp')
at = spherical(15, math.radians(45), math.radians(315))
light(at)
camera(at)
show()

bpy.context.scene.render.filepath = '/output/rendering.png'
bpy.context.scene.render.resolution_x = 800
bpy.context.scene.render.resolution_y = 600

bpy.ops.render.render(write_still=True)
