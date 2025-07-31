
# 📧 Spam Email Detector 🔍🧠

A simple AI-powered spam email detector built with **Spring Boot** (Java), **Flask** (Python), and a **Naive Bayes ML model**.  
Paste any email content and find out if it's 📭 SPAM or ✅ NOT SPAM in seconds!

---

## 🚀 Tech Stack

| Backend        | AI Model       | Frontend     |
|----------------|----------------|--------------|
| ☕ Spring Boot  | 🐍 Flask + Scikit-learn | 🌐 HTML + Bootstrap |

---

## 🖥️ Project Preview

> 🔗 Paste email → 🧠 AI predicts → ✅ Shows result  
![Preview](https://github.com/monukumarjha2020/-Spam-Email-Detector-/blob/main/Screenshot%20(3739).png) *(Add your own GIF or screenshot)*

---

## 📦 Folder Structure

```
spam-email-detector/
├── backend-springboot/    # Spring Boot REST API
├── ml-model-flask/        # Python ML model (Flask API)
└── frontend/              # Static index.html file
```

---

## 🧑‍💻 How to Run (Step-by-Step)

### 🔹 1. Clone the Repo
```bash
git clone https://github.com/your-username/spam-email-detector.git
cd spam-email-detector
```

---

### 🔹 2. Run the Flask ML API 🧠

> 📍 Navigate to the `ml-model-flask` folder

```bash
cd ml-model-flask
pip install -r requirements.txt       # Install dependencies
python train_model.py                 # Train and save the model
python app.py                         # Start Flask API (localhost:5000)
```

---

### 🔹 3. Run the Spring Boot Backend ☕️

> 📍 Navigate to `backend-springboot` in IntelliJ / VS Code

- Open `SpamDetectorApplication.java`
- Click **Run**
- Backend starts at: `http://localhost:8080`

---

### 🔹 4. Open the Frontend 🌐

> 📍 Navigate to `frontend` folder

- Double-click `index.html`
- Browser will open
- Paste email text & hit **"Check Spam"**

---

## 🧪 Sample Test

| Input Email | Prediction |
|-------------|------------|
| `Claim your free prize now!` | 🚫 SPAM |
| `Hey, let's catch up on the project tomorrow` | ✅ NOT SPAM |

---

## 🛠️ Future Improvements

- 📩 Email file upload (.eml)
- 📊 Admin dashboard with history
- 📥 API call logs and analytics
- ☁️ Deploy on AWS / Heroku / Render

---

## 👨‍💻 Author

- **Your Name** – [Monu Kumar]([https://github.com/yourgithub](https://github.com/monukumarjha2020))

---

## ⭐️ Show Some Love

If you liked this project, consider giving it a ⭐️ and sharing it!  
Let’s stop spam together! 🚫📬💪

---
