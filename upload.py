import yadisk
y = yadisk.YaDisk(token="AQAAAAAFzz4bAAcWVJNhoT1G1E81liY-xuEtyr0")
#y.mkdir("/Hello Word") # Создать папку
y.upload("upload.py", "/Hello Word/upload.py") # Загружает первый файл