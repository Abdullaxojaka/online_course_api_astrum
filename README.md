# Online Kurslar Boshqaruvi API

Bu loyiha kurslar, darslar va o‘qituvchilarni boshqarish uchun RESTful API yaratadi. Ushbu API Django REST Framework va DRF Spectacular yordamida ishlab chiqilgan.

---

## 📋 **Xususiyatlar**

- **O‘qituvchi boshqaruvi:**
  - Qo‘shish, o‘zgartirish, o‘chirish va ro‘yxat olish.
  - Email validatsiyasi.

- **Kurs boshqaruvi:**
  - Kurslarni qo‘shish, yangilash, o‘chirish va ko‘rish.
  - Boshlanish va tugash sanalarining to‘g‘riligini tekshirish.

- **Dars boshqaruvi:**
  - Darslarni kurslarga bog‘lash.
  - Tartib raqamini validatsiya qilish.

- **Swagger dokumentatsiyasi:**
  - Swagger va Redoc orqali API hujjatlarini avtomatik yaratish.

---

## 👨🏻‍💻 **Ishlatish bo‘yicha yo‘riqnoma**

```plaintext

pip install -r requirements.txt
```
```
python manage.py makemigrations 
python manage.py migrate
```
```
python manage.py createsuperuser
```
```
python manage.py runserver
```

---

## 📂 **Loyiha Tuzilishi**

```plaintext
.
├── core/
│   ├── admin.py        # Model ma'muriy interfeys sozlamalari
│   ├── apps.py         # Core ilovasining konfiguratsiyasi
│   ├── models.py       # Instructor, Course, va Lesson modellari
│   ├── serializers.py  # API ma'lumotlarini qayta ishlash
│   ├── urls.py         # Core uchun URL marshrutlari
│   ├── views.py        # API funksionalligi
│
├── config/
│   ├── settings.py     # Django sozlamalari
│   ├── urls.py         # Loyihaning asosiy URL marshrutlari
│   ├── wsgi.py         # WSGI kirish nuqtasi
│
├── manage.py           # Django boshqaruv fayli
├── requirements.txt    # Loyiha uchun kerakli kutubxonalar
└── README.md           # Ushbu fayl
