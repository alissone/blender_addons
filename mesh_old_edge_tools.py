import bpy

# If you don't add bl_info, it won't appear when installing an addon via menu
bl_info = {
    "name": "Restore Edge Menu missing options",
    "description": "This addon adds the options 'Select Boundary Loop' and 'Select Loop Inner Region' back to Edge Menu",
    "author": "alissone", # I'm open to any contributions at github.com/alissone/
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Edge (Ctrl+E)",
    "warning": "This addon is still experimental",
    "support": "COMMUNITY",
    "category": "Mesh"
}

def menu_f(self, context):
    layout = self.layout
    layout.separator()

    layout.operator_context = "INVOKE_DEFAULT"

    layout.operator(RegionToLoop.bl_idname, text='Select Boundary Loop')
    layout.operator(LoopToRegion.bl_idname,
                    text='Select Loop Inner Region')


class RegionToLoop(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "mesh.region_to_loop_2"
    bl_label = "Select Boundary Loop"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.active_object is not None
                and context.space_data.type == 'VIEW_3D'
                and context.active_object.type == 'MESH'
                and context.active_object.mode == 'EDIT'
                )

    def execute(self, context):
        bpy.ops.mesh.region_to_loop()
        return {'FINISHED'}


class LoopToRegion(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "mesh.loop_to_region_2"
    bl_label = "Select Loop Inner-Region"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        return (context.active_object is not None
                and context.space_data.type == 'VIEW_3D'
                and context.active_object.type == 'MESH'
                and context.active_object.mode == 'EDIT'
                )

    def execute(self, context):
        bpy.ops.mesh.loop_to_region()
        return {'FINISHED'}


def register():
    bpy.utils.register_class(RegionToLoop)
    bpy.utils.register_class(LoopToRegion)
    bpy.types.VIEW3D_MT_edit_mesh_edges.append(menu_f)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(menu_f)


def unregister():
    bpy.utils.unregister_class(RegionToLoop)
    bpy.utils.unregister_class(LoopToRegion)
    bpy.types.VIEW3D_MT_edit_mesh_edges.remove(menu_f)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(menu_f)


if __name__ == "__main__":
    register()