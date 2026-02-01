[app]
# Basic Information
title = TESCO Piping
package.name = tescoapp
package.domain = com.tesco.engineering

# Source code and extensions (Must include jpg)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# THE ICON - This must match your 1024x1024 jpg exactly
icon.filename = icon.jpg

# Requirements - Pillow is required to display your jpg plans
requirements = python3,kivy==2.2.1,pillow,setuptools

# Orientation & Fullscreen
orientation = landscape
fullscreen = 1

# Android Architecture & API
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk_api = 21

[buildozer]
# This section prevents the "NoSectionError" and handles permissions
log_level = 2
warn_on_root = 0
