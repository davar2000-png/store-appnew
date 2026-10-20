#!/usr/bin/env python3
"""Builds dist/app.html (version from src/VERSION) by concatenating src/head.html + src/js/*.js (sorted) + src/tail.html."""
import glob,os
r=os.path.dirname(os.path.abspath(__file__))
rd=lambda p:open(p,encoding="utf-8",newline="").read()
ver=rd(r+"/src/VERSION").strip()
import base64
def icon(n):
    p=r+"/desktop/app/"+n
    return ("data:image/png;base64,"+base64.b64encode(open(p,"rb").read()).decode()) if os.path.exists(p) else ""
out=rd(r+"/src/head.html").replace("__VERSION__",ver).replace("__ICON64__",icon("icon-64.png")).replace("__ICON128__",icon("icon-128.png"))+"".join(rd(f) for f in sorted(glob.glob(r+"/src/js/*.js")))+rd(r+"/src/tail.html")
js="".join(rd(f) for f in sorted(glob.glob(r+"/src/js/*.js")))
if "</script" in js.lower():raise SystemExit("خطا: رشته‌ی </script> داخل فایل‌های js مجاز نیست (به صورت <\\/script> بنویسید)")
os.makedirs(r+"/dist",exist_ok=True)
open(r+"/dist/app.html","w",encoding="utf-8",newline="").write(out)
if "__VERSION__" in out:raise SystemExit("خطا: __VERSION__ جایگزین نشد")
print("built dist/app.html v"+ver,len(out),"bytes")
