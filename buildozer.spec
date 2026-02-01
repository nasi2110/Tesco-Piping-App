[app]

# (1) The Title of your app
title = TESCO Piping

# (2) The name of the package (no spaces)
package.name = tescoapp
package.domain = com.tesco.engineering

# (3) Extensions to include (Make sure jpg is here!)
source.include_exts = py,png,jpg,kv,atlas

# (4) THE ICON (Make sure this matches your renamed file exactly)
icon.filename = icon.jpg

# (5) Requirements
requirements = python3,kivy==2.2.1,pillow,setuptools

# (6) Android specific settings
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk_api = 21
# It is safer to let Buildozer choose the NDK version automatically
# android.ndk = 25b 

# (7) Orientation
orientation = landscape

[buildozer]
# This section prevents the "NoSectionError" we saw earlier
log_level = 2
warn_on_root = 0
