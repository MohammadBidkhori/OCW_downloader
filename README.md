
# دانلود ویدئو از OpenCourseWare (OCW) دانشگاه فردوسی مشهد

میخواستم دوره های ocw رو بصورت آفلاین استفاده کنم . متاسفانه موقع دانلود اسم فایل درست حسابی نداشت و اینکه ممکن یک قسمت چند ویدیو داشته باشه.
با دادن لینک دوره ، اسکریپت ویدئو های مربوط به هر قسمت رو در پوشه اون قسمت دانلود میکنه .

## الزامات

- پایتون ۳.x
- کتابخانه `requests`
- کتابخانه `beautifulsoup4`
- کتابخانه `tqdm`

شما می‌توانید کتابخانه‌های مورد نیاز را با استفاده از pip نصب کنید:

```bash
pip install requests beautifulsoup4 tqdm
```
## نحوه اجرا
قبل از اجرا به این دقت کنید که لینک دوره باید یه چیزی شبیه به این باشه : 'https://ocw.um.ac.ir/course/یادگیری-عمیق/'
```bash
python downloadOCW.py
```
