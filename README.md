# 📊 Investigating Netflix Movies from the 1990s

This project explores movie data from Netflix, focusing specifically on films released during the 1990s. The goal was to analyze movie durations, identify patterns in film lengths, and determine how short movies (under 90 minutes) compared to longer ones during the decade.

This project was completed as part of a data exploration and analysis exercise using **Python**, **Pandas**, and **Matplotlib**.

---

## 🎯 Objectives

1. **Determine the most common movie duration** among films released in the 1990s.
2. **Count how many short movies** (duration < 90 minutes) were released during the same decade.

---

## 🗂 Dataset

The dataset used in this project was provided in a CSV format (`netflix_data.csv`). Key columns in the dataset:

| Column        | Description                                |
|---------------|--------------------------------------------|
| type          | Type of show (Movie or TV Show)            |
| title         | Title of the movie                         |
| director      | Director of the movie                      |
| cast          | Actors in the movie                        |
| country       | Country of origin                          |
| release_year  | Year the movie was released                |
| duration      | Duration of the movie in minutes           |
| genre         | Movie genre                                |

---

## 🔍 Analysis Summary

- The dataset was filtered to include only **movies** (not TV shows).
- From those movies, we selected only those **released in the 1990s**.
- We visualized the distribution of movie durations using a histogram.
- Based on the frequency distribution, the **most common movie duration** was approximately **100 minutes**.
- We also counted how many movies from the 1990s had a duration of **less than 90 minutes**.

---

## 📈 Visualization Example

A histogram was used to show the distribution of film durations

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Jupyter Notebook

---

## 📦 Project Structure

```
├── netflix_data.csv
├── project.py
└── README.md
```

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/k-aghakhani/netflix-80s-analysis.git
   ```
2. Navigate into the project folder:
   ```bash
   cd netflix-80s-analysis
   ```
3. Open and run the Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

---

## ✨ Author

**Kiarash Aghakhani**  
Email: kiarash1988@gmail.com

---

If you'd like to suggest improvements or collaborate, feel free to open an issue or submit a pull request! 🎬
