# 📝 Flutter Blog Application

This is a full-stack blog application built using **Flutter** for the frontend and **Django REST Framework** for the backend. It allows users to:

- 🧾 Register and login securely with JWT
- 🖊️ Create blog posts
- 🧠 View detailed post content
- ✏️ Edit and delete own posts
- 📃 View a styled list of blog entries

---

## 📸 Screenshots

<img src="outputs/post list screen.png" width="300">
<img src="outputs/create post screen.png" width="300">
<img src="outputs/post detail screen.png" width="300">

---

## 🛠️ Features

- Login/Logout with authentication
- Create/Edit/Delete posts
- Responsive UI with custom background images
- View snippets of blog content in card view
- Navigation to detailed post screen
- Backend: Django REST API with JWT
- Frontend: Flutter with shared preferences for token storage

---

## 🚀 Getting Started

### Prerequisites

- Flutter SDK installed
- Python + Django + DRF installed
- Android Emulator or physical device

### Run the Flutter App

```bash
cd frontend
flutter pub get
flutter run
```

### Run the Django Backend

```bash
cd backend
python manage.py runserver


