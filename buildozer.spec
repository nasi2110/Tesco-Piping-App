[app]
title = TESCO API plans
package.name = tescoapp
package.domain = com.tesco.engineering
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.1

# Critical Requirements
requirements = python3,kivy==2.2.1,pillow,setuptools

orientation = landscape
fullscreen = 1
icon.filename = icon.png

# --- RELEASE SETTINGS ---
# This ensures Buildozer produces an APK file
android.release_artifact = apk
# Set to 0 to remove the 'debug' watermark from your icon
android.debug_artifacts = 0

# Android Architecture
# arm64-v8a is for modern phones. 
# You can add armeabi-v7a if you want to support very old phones.
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk_api = 21

[buildozer]
log_level = 2
warn_on_root = 0
