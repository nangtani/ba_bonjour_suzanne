import bpy

def test_bool():
    bpy.ops.import_scene.xxx("EXEC_DEFAULT", VAR0=True)
    assert bpy.types.Scene.debug["IMPORT_SCENE_OT_xxx"]["VAR0"]
    bpy.ops.import_scene.xxx("EXEC_DEFAULT", VAR0=False)
    assert not bpy.types.Scene.debug["IMPORT_SCENE_OT_xxx"]["VAR0"]


