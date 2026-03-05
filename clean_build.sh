#!/bin/bash
# Clean Xcode Build Script for FORGE

echo "🧹 Cleaning Xcode build and derived data..."

# Remove derived data for Forge project
rm -rf ~/Library/Developer/Xcode/DerivedData/Forge-*

# Remove build folder
rm -rf build/

echo "✅ Clean complete! Now open the project in Xcode and build."
