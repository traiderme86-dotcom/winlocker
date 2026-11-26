[app]
title = WinLocker
package.name = winlocker
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Разрешения
android.permissions = INTERNET

# Настройки экрана (портрет, на весь экран)
orientation = portrait
fullscreen = 1

# Используемые библиотеки
requirements = python3,kivy

# Архитектуры (arm64 для современных телефонов)
android.archs = arm64-v8a
android.allow_backup = True