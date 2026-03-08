[app]
# (str) Title of your application
title = Sami AI App

# (str) Package name
package.name = samiaiapp

# (str) Package domain (needed for android packaging)
package.domain = org.sami

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# تأكد من إضافة المكتبات التي استخدمتها في AI Studio هنا
requirements = python3,kivy,kivymd,google-generativeai,requests,urllib3

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (bool) enables skip update render code (very important for some apps)
android.skip_update = False
