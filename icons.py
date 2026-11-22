# APK simgesini (gözlüklü tavşan) Android klasörlerine yerleştirir
from PIL import Image, ImageDraw
r='android/app/src/main/res/'
ic=Image.open('icon-512.png').convert('RGBA');fg=Image.open('icon-foreground.png').convert('RGBA')
for d,a,b in [('mdpi',48,108),('hdpi',72,162),('xhdpi',96,216),('xxhdpi',144,324),('xxxhdpi',192,432)]:
    p=r+'mipmap-'+d+'/'
    x=ic.resize((a,a),Image.LANCZOS);x.save(p+'ic_launcher.png')
    m=Image.new('L',(a,a),0);ImageDraw.Draw(m).ellipse([0,0,a-1,a-1],fill=255);y=Image.new('RGBA',(a,a),(0,0,0,0));y.paste(x,(0,0),m);y.save(p+'ic_launcher_round.png')
    fg.resize((b,b),Image.LANCZOS).save(p+'ic_launcher_foreground.png')
open(r+'values/ic_launcher_background.xml','w').write('<?xml version="1.0" encoding="utf-8"?><resources><color name="ic_launcher_background">#5B3DF5</color></resources>')
