# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
import bpy

bl_info = {
    "name": "Bonjour Suzanne",
    "author": "Dave Keeshan",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "category": "Object",
}

def execute_decorator(func):
    if not hasattr(bpy.types.Scene, "debug"):
        bpy.types.Scene.debug = {}
    
    def function_wrapper(self, x):
        if not self.bl_idname in bpy.types.Scene.debug:
            bpy.types.Scene.debug[self.bl_idname] = {}
        for key in self.__annotations__.keys():
            bpy.types.Scene.debug[self.bl_idname][key] = getattr(self, key)
        y = func(self, x)
        return y
    return function_wrapper

class IMPORT_OT_xxx(bpy.types.Operator):
    """FIX ME"""

    bl_idname = "import_scene.xxx"
    bl_label = "Import SUZANNE"
    bl_description = "FIX ME"
    bl_options = {"REGISTER", "UNDO"}

    VAR0 : bpy.props.BoolProperty(
        name="Variable 0",
        description="Set a Boolean value",
        default=False,
    )

    def invoke(self, context, event): 
        raise Exception(self.VAR0)
        wm = context.window_manager
        wm.invoke_props_dialog(self)
        return {"RUNNING_MODAL"}

    @execute_decorator
    def execute(self, context):
        return {"FINISHED"}

def menu_func(self, context):
    self.layout.operator(IMPORT_OT_xxx.bl_idname, text="Bonjour Suzanne (.XXX)")


classes = (
    IMPORT_OT_xxx,
)

def register():
    print("Hello World")
    for cls in classes:
         bpy.utils.register_class(cls)

    bpy.types.TOPBAR_MT_file_import.append(menu_func)


def unregister(): # pragma: no cover
    print("Goodbye World") 
    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.types.TOPBAR_MT_file_import.remove(menu_func)
