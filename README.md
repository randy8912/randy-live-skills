# 🚀 Randy Live Skills — Portfolio & Live Development Showcase

[![Django](https://img.shields.io/badge/Django-5.2.7-green)](https://www.djangoproject.com/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-v4-blue)](https://tailwindcss.com/)
[![Render](https://img.shields.io/badge/Hosted%20on-Render.com-purple)](https://render.com/)
[![LinkedIn](https://img.shields.io/badge/Connect%20on-LinkedIn-blue)](https://www.linkedin.com/in/randy-saija)
[![GitHub](https://img.shields.io/badge/Follow-randy8912-black)](https://github.com/randy8912)

---

## 🧠 Over dit project

**Randy Live Skills** is mijn persoonlijke Django‑5 portfolio en “live skills” showcase — een plek waar ik mijn groei als developer zichtbaar maak.  
De site is gebouwd met **Django 5**, **Tailwind CSS v4**, en **Whitenoise** voor veilige hosting op **Render.com**.  
Het doel: een schaalbare, veilige en transparante weergave van mijn leerreis als software‑ontwikkelaar.

---

## 🔧 Tech Stack
- **Framework:** Django 5.2.7  
- **Styling:** TailwindCSS v4  
- **Database:** SQLite (local dev)  
- **Static handling:** Whitenoise  
- **Deployment:** Render.com  
- **Environment management:** python‑dotenv  
- **Language:** Python 3.12

---

## ✨ Features
- 📂 Dynamische project‑CMS via Django‑Admin  
- 🧭 Filtering, search & pagination  
- 🧱 Responsive design met TailwindCSS  
- 🎨 Scroll reveal & spotlight effects via JS  
- 🧑‍💼 Veilige, .env‑based configuratie  
- 🔐 Whitenoise static file compression  
- 🌍 Automatische Render‑deploy via GitHub push  

---

## 🌐 Live demo
👉 [https://randy-live-skills.onrender.com](https://randy-live-skills.onrender.com)

---

## ⚙️ Installatie

```bash
# 1. Clone de repo
git clone https://github.com/randy8912/randy-live-skills.git
cd randy-live-skills

# 2. Activeer virtuele omgeving
python -m venv .venv
source .venv/bin/activate

# 3. Installeer dependencies
pip install -r requirements.txt
npm install

# 4. Compileer CSS
npm run tw:build

# 5. Run de app
python manage.py runserver
```

---

## ☁️ Deployment op Render
Gebruik het volgende build‑ en start‑commando:

**Build command**
```bash
pip install -r requirements.txt && npm install && npm run tw:build && python manage.py collectstatic --noinput
```

**Start command**
```bash
gunicorn app.wsgi:application
```

---

## 💼 Over de maker
👋 Ik ben **Randy Saija**, een gepassioneerde developer met een achtergrond in techniek en AI‑creatie.  
Ik bouw applicaties die technologie, storytelling en menselijke creativiteit verbinden.  
📫 [LinkedIn](https://www.linkedin.com/in/randy-saija) — [GitHub](https://github.com/randy8912)

---

## 📝 Licentie
MIT License © 2025 Randy Saija — [RDS‑Solutions](https://github.com/randy8912)