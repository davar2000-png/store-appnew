# تکنوکالا — ساختار پروژه

- `src/head.html` / `src/tail.html`: HTML و CSS
- `src/js/NN-*.js`: کد برنامه به ترتیب شماره (همه سراسری‌اند؛ `onclick`های درون‌خطی همین را لازم دارند)
- `python3 build.py` → `dist/app.html` (تک‌فایل؛ کنار پوشه `assets/` قرار دهید)
- `node --test` → تست محاسبات (تابع `selfTests` در `55-audit-selftests.js`)

قانون: فقط `src/` را ویرایش کنید؛ `dist/` خروجی است.
