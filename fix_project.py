#!/usr/bin/env python3
import re

# Read the project file
with open('./Forge.xcodeproj/project.pbxproj', 'r') as f:
    lines = f.readlines()

# IDs to remove (all the manually added onboarding files)
ids_to_remove = [
    'E86125A0', 'E86125A1', 'E86125A2', 'E86125A3', 'E86125A4',
    'E86125A5', 'E86125A6', 'E86125A7', 'E86125A8', 'E86125A9',
    'E86125942F413CB400579751', 'E86125952F413CB400579751',
    'E86125962F413CB400579751', 'E86125972F413CB400579751',
    'E86125982F413CB400579751', 'E86125992F413CB400579751',
    'E861259A2F413CB400579751', 'E861259B2F413CB400579751',
    'E861259C2F413CB400579751', 'E861259D2F413CB400579751',
    'E861259E2F413CB400579751', 'E861259F2F413CB400579751'
]

# Filter out lines containing these IDs
new_lines = []
for line in lines:
    should_keep = True
    for id_to_remove in ids_to_remove:
        if id_to_remove in line:
            should_keep = False
            break
    if should_keep:
        new_lines.append(line)

# Write back
with open('./Forge.xcodeproj/project.pbxproj', 'w') as f:
    f.writelines(new_lines)

print(f"✅ Removed {len(lines) - len(new_lines)} lines with duplicate references")
print(f"Original: {len(lines)} lines")
print(f"New: {len(new_lines)} lines")
