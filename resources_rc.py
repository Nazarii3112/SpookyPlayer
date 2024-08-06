# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (pyrcc5)

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x00\x00\
"

qt_resource_name = b"\
\x00\x05\
\x00\x69\x00\x6d\x00\x61\x00\x67\x00\x65\
\x00\x09\
\x00\x69\x00\x63\x00\x6f\x00\x6e\x00\x2e\x00\x69\x00\x63\x00\x6f\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x14\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x14\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct_v1, qt_resource_name, qt_resource_data)

def qInitResources():
    QtCore.qRegisterResourceData(0x02, qt_resource_struct_v2, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct_v1, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x02, qt_resource_struct_v2, qt_resource_name, qt_resource_data)

qInitResources()
