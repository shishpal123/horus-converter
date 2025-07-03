# Horus File Converter 🌐

Convert your data files (CSV, JSON, Images, Audio) into Horus-compatible format — instantly through the web.

[🌍 Try It Live](https://horus-converter.onrender.com/)

---

## 🚀 Features

- ✅ Convert **CSV** to Horus format
- ✅ Convert **JSON** to Horus format
- ✅ Convert **Images (PNG)** to RGB pixel data in Horus format
- ✅ Convert **Audio (WAV)** to tabular audio data
- ✅ Download the converted file as `.csv`
- ✅ Simple, fast, and user-friendly web interface

---

## 📸 Demo

![demo](https://github.com/yourusername/horus-converter/assets/demo-screenshot.gif)

---

## 🛠 Tech Stack

- **Flask** (Python Web Framework)
- **Pandas, NumPy, SciPy, scikit-image, matplotlib**
- **HTML5 + CSS3** for frontend
- **Render.com** for free cloud hosting
- **Gunicorn** as production web server

---

## 📂 Project Structure

horus-converter/
│
├── app/
│ ├── templates/ → HTML Templates
│ ├── static/ → CSS, JS
│ ├── converters/ → Python logic for each file type
│ └── app.py → Flask routes
│
├── uploads/ → Uploaded files (auto-created)
├── converted/ → Output files (auto-created)
├── run.py → Entry point for Gunicorn
├── requirements.txt → Project dependencies
└── README.md → You're reading it!

yaml
Copy code

---

## 🚀 Deployment

This project is deployed on **Render** (free tier). To deploy your own:

1. Fork this repo
2. Add your environment on [Render](https://render.com)
3. Set the Start Command: `gunicorn run:app`
4. You're live!

---

## 👨‍💻 Author

**Shishpal**
- 📧 [LinkedIn](https://www.linkedin.com/in/shishpal-bharatsingh-rawat-8aba262b0/))
- 🧠 Python Developer | Data Science Enthusiast | Full Stack Learner

---

## 🙌 Contributions

Feel free to fork, open issues, or suggest improvements!
