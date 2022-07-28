#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bpy
import numpy as np
import mathutils

TEMP_FLAG_NAME = "__tempFragment__"
VERTEX_GROUP_NAME="frag"
ARMATURE_NAME="PhysicsObjectAmt"



col = bpy.context.collection.objects.items()
empties = []
for i in col:
    if i[1].type == 'EMPTY':
        empties.append(i)

for e in empties:
    bpy.ops.object.select_all(action='DESELECT')
    root = bpy.data.meshes.new(e[0]+"__mesh")
    obj = bpy.data.objects.new(e[0]+"_mesh",root)
    scene = bpy.context.scene
    scene.collection.objects.link(obj)
    meshes = e[1].children
    for mesh in meshes:
        mesh.select_set(True)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.join()
        
pass            