# TECHNOKALA — PHASE 00
## Repository Audit + Minimal Bootstrap

### هدف
پروژه حسابداری فروشگاه تکنوکالا را بررسی و فقط زیرساخت اولیه قابل اجرا را آماده کن.

### Source of Truth
GitHub:
https://github.com/davar2000-png/store-appnew

قبل از هر تغییری:
1. کل ساختار فعلی Repository را بررسی کن.
2. فایل‌های موجود، package.json، README و Git status را بررسی کن.
3. اگر فایل‌های PROJECT_STATE.md / ROADMAP.md / ARCHITECTURE.md / AI_HANDOFF.md / DECISIONS.md / PHASE_REGISTRY.md / CHANGELOG.md وجود دارند، ابتدا آن‌ها را بخوان.
4. وضعیت واقعی پروژه را با مستندات مقایسه کن.
5. فرض نکن که Phase قبلی کامل است؛ فقط بر اساس وضعیت واقعی Repository تصمیم بگیر.

---

## قوانین مهم

- فقط همین Phase را انجام بده.
- در این Phase هیچ ماژول تجاری مثل فروش، خرید، انبار، اشخاص، چک یا حسابداری را پیاده‌سازی نکن.
- از ایجاد معماری پیچیده یا Dependency غیرضروری خودداری کن.
- پروژه باید Windows-compatible باشد.
- کاربر مبتدی است؛ ساختار را ساده و قابل نگهداری نگه دار.
- اگر Repository از قبل دارای ساختار مناسب است، آن را دوباره‌سازی نکن.
- هیچ فایل مهم موجود را بدون دلیل حذف نکن.
- هیچ داده واقعی یا Legacy Database را وارد نکن.

---

## اگر پروژه خالی یا ناقص است

حداقل Skeleton زیر را آماده کن:

Electron
+
React
+
TypeScript
+
Vite

هدف این Phase فقط این است که یک Desktop App پایه داشته باشیم که:

- با npm install نصب شود.
- با npm run dev اجرا شود.
- پنجره Electron باز شود.
- React UI نمایش داده شود.
- npm run build با موفقیت انجام شود.

فعلاً SQLite، ORM، Migration، Authentication و Business Modules را اضافه نکن مگر اینکه Repository فعلی از قبل به آن‌ها وابسته باشد.

---

## UI اولیه

یک صفحه بسیار ساده و تمیز فارسی RTL بساز:

عنوان:
«نرم‌افزار حسابداری و مدیریت فروشگاه تکنوکالا»

زیرعنوان:
«زیرساخت اولیه پروژه آماده است»

هیچ Dashboard یا فرم تجاری در این Phase ساخته نشود.

---

## مستندات پروژه

در پایان وضعیت واقعی پروژه را در این فایل‌ها ثبت یا اصلاح کن:

### PROJECT_STATE.md
شامل:
- وضعیت فعلی پروژه
- Stack فعلی
- نحوه اجرای پروژه
- نتیجه تست‌ها
- Phase فعلی
- Phase بعدی پیشنهادی

### ROADMAP.md
فقط Roadmap سطح بالا را ثبت کن.

### ARCHITECTURE.md
معماری فعلی واقعی را ثبت کن.
اگر هنوز معماری کامل نشده، صریحاً بنویس.

### AI_HANDOFF.md
برای AI بعدی بنویس:
- چه چیزی انجام شد
- چه چیزی انجام نشد
- وضعیت Git
- دستور اجرای پروژه
- تست‌های انجام‌شده
- Phase بعدی پیشنهادی
- هر نکته‌ای که AI بعدی باید بداند

### PHASE_REGISTRY.md
Phase 00 را با وضعیت:
COMPLETED
ثبت کن، فقط اگر واقعاً کامل و تست شده است.

### CHANGELOG.md
تغییرات Phase 00 را ثبت کن.

---

## تست اجباری

حداقل این موارد را اجرا کن:

1. npm install
2. npm run dev یا معادل واقعی پروژه
3. بررسی باز شدن Electron
4. npm run build
5. بررسی خطاهای TypeScript
6. بررسی Git diff
7. بررسی Git status

اگر تستی شکست خورد، آن را اصلاح کن.
اگر قابل اصلاح نیست، Phase را COMPLETED اعلام نکن.

---

## Git

پس از موفقیت:

git add .

git commit -m "phase-00: audit and minimal bootstrap"

git push origin main

اگر Branch فعلی main نیست، Branch واقعی را بررسی کن و از Branch صحیح Repository استفاده کن.

هرگز force push نکن.

---

## ZIP تحویلی

پس از موفقیت، یک ZIP از وضعیت نهایی پروژه بساز.

نام:

TechnoKala-Phase-00-YYYYMMDD-HHMM.zip

ZIP باید شامل Source Code و مستندات پروژه باشد.

این موارد را داخل ZIP قرار نده:
- node_modules
- فایل‌های موقت
- cache
- build cache غیرضروری
- فایل‌های شخصی
- secrets
- API keys
- passwords

---

## Token Safety

اگر احساس کردی Token/Context رو به اتمام است:

هیچ Feature جدیدی شروع نکن.

فوراً وارد:

SAFE RELEASE MODE

شو:

1. تغییرات فعلی را کامل کن.
2. تست کن.
3. مستندات را به‌روز کن.
4. ZIP بساز.
5. Git commit کن.
6. Git push کن.
7. گزارش نهایی بده.

---

## گزارش نهایی اجباری

در پایان فقط یک گزارش دقیق بده با این ساختار:

PHASE: 00
STATUS: COMPLETED / BLOCKED

### Repository Audit
- وضعیت اولیه:
- مشکلات پیدا شده:
- اصلاحات انجام شده:

### Implementation
- تغییرات انجام‌شده:

### Tests
- npm install:
- dev run:
- Electron:
- build:
- TypeScript:

### Git
- branch:
- commit:
- push:

### ZIP
- filename:
- location:

### Documentation
- PROJECT_STATE:
- ROADMAP:
- ARCHITECTURE:
- AI_HANDOFF:
- PHASE_REGISTRY:
- CHANGELOG:

### Next Phase
کوچک‌ترین Phase منطقی بعدی را پیشنهاد بده.

### Important
اگر چیزی واقعاً انجام نشده، آن را COMPLETED اعلام نکن.
از گزارش ساختگی یا حدس‌زدن وضعیت Repository خودداری کن.

پس از گزارش، متوقف شو و منتظر Phase بعدی بمان.