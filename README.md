README.md
Loyiha haqida
Ushbu loyiha so'rovlarni (lead) boshqarish uchun mo'ljallangan tizim hisoblanadi. Tizim attorney (advokat) guruhiga asoslangan. Bu tizimda attorneylar ro'yxatdan o'tgan holda so'rovlarni ko'rish va ularning statusini o'zgartirish huquqiga ega bo'lishadi.
Loyihani ishga tushirish
Loyihani ishga tushirish uchun Docker Compose dan foydalaning:
bashdocker-compose up -d
Tizim default ravishda 8080 portda ishlaydi.
Tizimga kirish
Tizim dashboardiga quyidagi ma'lumotlar orqali kirish mumkin:

Login: admin
Parol: SecurePassword

Foydalanuvchilarni sozlash

"Attorneys" guruhini yaratish:

Dashboardga administrator sifatida kiring
"Groups" bo'limiga o'ting
"Create Group" tugmasini bosing
Guruh nomi: "attorneys" deb kiriting
"Lead edit" ruxsatini belgilang
Guruhni saqlang


Yangi foydalanuvchi yaratish va guruhga qo'shish:

"Users" bo'limiga o'ting
"Create User" tugmasini bosing
Kerakli ma'lumotlarni kiriting
"Group" maydonidan "attorneys" guruhini tanlang
Foydalanuvchini saqlang



API endpointlari
Ochiq API

POST /api/v1/leads - Tizimga yangi so'rov (lead) yuborish uchun (autentifikatsiya talab qilinmaydi)

Attorneys guruhi a'zolari uchun API
Ushbu API endpointlari faqat "attorneys" guruhiga a'zo bo'lgan foydalanuvchilar uchun mavjud:

GET /api/v1/leads - Barcha so'rovlar ro'yxatini olish
GET /api/v1/leads/{id} - Bitta so'rovni ID bo'yicha olish
PATCH /api/v1/leads/{id} - So'rov statusini o'zgartirish

Autentifikatsiya

POST /api/v1/auth/login - Attorneylar uchun tizimga kirish (login/parol bilan)

Muhim eslatmalar

Attorney foydalanuvchilar faqat lead statusini o'zgartirish huquqiga ega
Barcha API so'rovlarida (ochiq API dan tashqari) authentication token talab qilinadi
Autentifikatsiyadan o'tish uchun /api/v1/auth/login endpointidan foydalaning