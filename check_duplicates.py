#!/usr/bin/env python3
import re
from collections import Counter

# Read the project file
with open('./Forge.xcodeproj/project.pbxproj', 'r') as f:
    content = f.read()

# Find all PBXBuildFile entries
build_files = re.findall(r'(\w+) /\* (\S+\.swift) in Sources \*/', content)

# Count occurrences
file_counts = Counter([name for _, name in build_files])

print("Files in build phase:")
for filename, count in file_counts.items():
    if count > 1:
        print(f"  ❌ {filename}: {count} times (DUPLICATE!)")
    else:
        print(f"  ✓ {filename}: {count} time")

# Check for duplicates
duplicates = [name for name, count in file_counts.items() if count > 1]
if duplicates:
    print(f"\n🚨 Found {len(duplicates)} duplicate(s)!")
else:
    print("\n✅ No duplicates found in PBXBuildFile section")
