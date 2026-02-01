[app]
title = TESCO Piping
package.name = tescoapp
package.domain = com.tesco.engineering
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Critical Requirements
requirements = python3,kivy==2.2.1,pillow,setuptools

orientation = landscape
fullscreen = 1
icon.filename = icon.jpg

# Android Architecture
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk_api = 21

[buildozer]
log_level = 2
warn_on_root = 0
