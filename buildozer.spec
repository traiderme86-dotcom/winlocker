[app]
title = WinLocker
package.name = winlocker
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Разрешения
android.permissions = INTERNET

# Автоматическое принятие лицензий SDK (это исправит ошибку)
android.accept_sdk_license = True

# Настройки экрана
orientation = portrait
fullscreen = 1

# Библиотеки
requirements = python3,kivy
