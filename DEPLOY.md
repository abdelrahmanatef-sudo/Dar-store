# 🚀 دليل النشر على GitHub + Firebase

## المتطلبات

1. حساب GitHub
2. حساب Google (لـ Firebase)
3. Node.js مثبت على جهازك

---

## الخطوة 1: رفع المشروع على GitHub

### 1.1 إنشاء repository جديد
- اذهب إلى [github.com](https://github.com)
- اضغط على **New Repository**
- اسم المستودع: `dar-store`
- اختر **Public**
- اضغط **Create repository**

### 1.2 رفع الملفات
افتح Terminal في مجلد المشروع ونفّذ:

```bash
# تهيئة Git
git init

# إضافة جميع الملفات
git add .

# أول commit
git commit -m "Initial commit - Dar Store complete"

# ربط بالمستودع البعيد (استبدل USERNAME باسم المستخدم)
git remote add origin https://github.com/YOUR_USERNAME/dar-store.git

# رفع الملفات
git push -u origin main
```

---

## الخطوة 2: إعداد Firebase Hosting

### 2.1 تثبيت Firebase CLI
```bash
npm install -g firebase-tools
```

### 2.2 تسجيل الدخول
```bash
firebase login
```
يفتح المتصفح لتسجيل الدخول بحساب Google.

### 2.3 إنشاء مشروع Firebase
- اذهب إلى [Firebase Console](https://console.firebase.google.com)
- اضغط **Add project**
- اسم المشروع: `dar-store`
- أكمل الخطوات

### 2.4 تهيئة المشروع
في مجلد المشروع:
```bash
firebase init hosting
```

اختارات:
- ✅ Use an existing project → اختر `dar-store`
- ? What do you want to use as your public directory? → `.` (نقطة)
- ? Configure as a single-page app? → `Yes`
- ? Set up automatic builds and deploys with GitHub? → `Yes`
- ? File index.html already exists. Overwrite? → `No`

### 2.5 النشر
```bash
firebase deploy
```

سيظهر لك رابط الموقع، مثل:
```
✔ Deploy complete!

Project Console: https://console.firebase.google.com/project/dar-store/overview
Hosting URL: https://dar-store.web.app
```

---

## الخطوة 3: ربط GitHub Actions (اختياري - Auto Deploy)

لما تفعّلت الخطوة 2.4، Firebase عمل لك workflow تلقائي.

لو مش شغال، عدّل الملف:
`.github/workflows/firebase-hosting-merge.yml`

وتأكد إنه فيه:
```yaml
- uses: actions/checkout@v4
- uses: FirebaseExtended/action-hosting-deploy@v0
  with:
    repoToken: '${{ secrets.GITHUB_TOKEN }}'
    firebaseServiceAccount: '${{ secrets.FIREBASE_SERVICE_ACCOUNT }}'
    channelId: live
```

---

## 🔥 خدمات Firebase اللي ممكن تضيفها

### 1. Firebase Authentication (تسجيل الدخول)
```bash
firebase init authentication
```

### 2. Firebase Firestore (قاعدة بيانات)
```bash
firebase init firestore
```

### 3. Firebase Storage (رفع صور)
```bash
firebase init storage
```

---

## 📝 ملاحظات مهمة

- **ملف `.firebaserc`**: عدّل فيه `YOUR-FIREBASE-PROJECT-ID` بـ ID المشروع الحقيقي
- **النطاق المخصص**: ممكن تربط دومين خاص من Firebase Console → Hosting → Add custom domain
- **SSL مجاني**: Firebase بيقدم HTTPS تلقائي

---

## 🎯 الأوامر السريعة

```bash
# نشر يدوي
firebase deploy

# نشر Hosting فقط
firebase deploy --only hosting

# معاينة محلية
firebase serve

# فتح Console
firebase open
```

---

## 📞 دعم

لو واجهت أي مشكلة، افتح Issue في المستودع أو تواصل معنا.
