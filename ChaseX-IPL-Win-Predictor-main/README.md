# 🏏 ChaseX - IPL Win Predictor

## 📌 Project Overview

**ChaseX- IPL Win Predictor** is a machine learning project that predicts the probability of the chasing team winning an IPL match.

It provides real-time win probability predictions based on match conditions such as:

- Batting team
- Bowling team
- Venue (city)
- Target score
- Current score
- Overs Completed
- Wickets Fallen

The project uses a trained **ML pipeline (`pipe.pkl`)** and an interactive **Streamlit web app (`app.py`)** to make predictions.

---

## 🚀 Features

- Select **batting & bowling teams** from IPL franchises
- Choose the **city/venue**
- Input **target score, current score, overs, and wickets fallen**
- Get **instant win probability** for both teams
- Clean and user-friendly **Streamlit interface**

---

## 🧠 Model Training

The model is trained in the Jupyter Notebook [`model.ipynb`](./model.ipynb).  
Steps include:

1. **Data Preprocessing** – handling match data, encoding teams & cities, feature engineering
2. **Feature Engineering** – runs left, balls left, wickets left, current & required run rates
3. **Model Training** – Machine learning classification pipeline built and saved as `pipe.pkl`
4. **Evaluation** – Evaluated performance using accuracy and probability calibration

The trained pipeline is serialized using **Pickle** and used in the Streamlit app for predictions.

---

## 📂 Project Structure

```
📦 IPL-Win-Predictor
 ┣ 📜 app.py            # Streamlit web app
 ┣ 📜 model.ipynb       # Jupyter notebook for training & evaluation
 ┣ 📜 pipe.pkl          # Trained ML pipeline
 ┣ 📜 README.md         # Project documentation
 ┗ 📜 requirements.txt  # Dependencies
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/IPL-Win-Predictor.git
cd IPL-Win-Predictor
```

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies

Create a `requirements.txt` file with:

```
streamlit
pandas
scikit-learn
numpy
```

Then run:

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🎮 Usage

1. Run the app using Streamlit
2. Select batting/bowling teams and venue
3. Enter the match details (target, current score, overs, wickets)
4. Click **Predict Win Probability**
5. View the **win percentage** for both teams in real-time

---

## 🔮 Future Improvements

- Add support for **first innings win predictions**
- Use **live data scraping** from cricket APIs
- Enhance model with **player-specific stats (strike rate, economy)**
- Deploy on **Streamlit Cloud / Heroku / Render** for public access

---

## 👨‍💻 Author

Made with ❤️ by **Gauraang Rajvanshi**  
© 2025 ChaseX
