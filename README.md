# 🎵 Music Recommendation System

A **Machine Learning based Music Recommendation System** built with **Flask** that recommends songs similar to the one selected by the user.

The system uses a **content-based filtering approach** where songs are compared using a **similarity matrix**. When a user selects a song, the system returns the **top 20 most similar songs**.

---

# 🚀 Repository

GitHub:
[https://github.com/mohitkumhar/music-recommendation](https://github.com/mohitkumhar/music-recommendation)

---

# 📌 Features

✔ Recommend similar songs instantly  
✔ Content-based recommendation system  
✔ Flask web interface  
✔ Precomputed similarity matrix for fast results  
✔ Returns **Top 20 similar songs**  

---

# 🧠 How the System Works

1. Load the song dataset.
2. Extract relevant song features.
3. Compute similarity between songs.
4. Store the similarity matrix using **pickle**.
5. When a user selects a song:

   * Find its index
   * Retrieve similarity scores
   * Return the most similar songs.

---

# ⚠ Important Setup Step

Before running the web application, you **must run the Jupyter Notebook**:

```
main.ipynb
```

This notebook:

* Processes the dataset
* Computes the similarity matrix
* Generates the file:

```
similarity.pkl
```

⚠ Without `similarity.pkl`, the Flask application **will not work**.

---

# 🗂 Project Structure

```
music-recommendation/
│
├── app.py                # Flask application
├── main.ipynb            # Model training & similarity creation
│
├── requirements.txt
│
├── df.pkl                # Processed dataframe
├── similarity.pkl        # Song similarity matrix (generated from notebook)
├── songdata.csv          # Original dataset
│
├── templates/
│   └── index.html        # Frontend HTML page
│
├── static/
│   └── img.png           # Static image assets
│
└── README.md
```

---

# 🛠 Tech Stack

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* Pickle
* HTML / CSS

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/mohitkumhar/music-recommendation.git
cd music-recommendation
```

Install dependencies:

```bash
pip install flask pandas numpy scikit-learn
```

---

# ▶ Step 1: Generate Similarity Matrix

Run the Jupyter notebook:

```
main.ipynb
```

This will generate:

```
similarity.pkl
```

which is required by the Flask application.

---

# ▶ Step 2: Run the Flask Application

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

# 🎯 Usage

1. Open the web application.
2. Select a song from the dropdown.
3. Click recommend.
4. The system will display **20 similar songs**.

---

# 🧪 Recommendation Logic

The recommendation function works by:

1. Finding the index of the selected song.
2. Retrieving similarity scores from the similarity matrix.
3. Sorting songs by similarity.
4. Returning the top recommendations.

---

# 🔮 Future Improvements

* Spotify API integration
* Album art previews
* Artist-based recommendations
* Deep learning embeddings
* Improved UI/UX

---

# 👨‍💻 Author

**Mohit Kumhar**

GitHub
[https://github.com/mohitkumhar](https://github.com/mohitkumhar)

---

⭐ If you found this project helpful, please **star the repository**.
