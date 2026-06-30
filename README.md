# Data Science Internals

Welcome to my academic evaluation log for Data Science. This repository is structured to align with the course marks distribution and evaluation metrics of the course, encompassing course certifications, the capstone project source code, and weekly laboratory evaluation notebooks.

---

## Academic Evaluation Matrix

| Metric | Max Marks | Status | Repository Folder |
| :--- | :---: | :---: | :--- |
| **1. MOOCs Review** | **40 Marks** | `[ Verified - 2 Course Certificates ]` | [`/1. Moocs Review`](./1.%20Moocs%20Review/) |
| **2. Mini / Capstone Project** | **40 Marks** | `[ Completed - GLYCOS.ai ]` | [`/2. Mini or capstone project`](./2.%20Mini%20or%20capstone%20project/) |
| **3. Lab Continuous Evaluation** | **50 Marks** | `[ Completed - Weeks 1 to 13 ]` | [`/3. Lab Continuous Evaluation`](./3.%20Lab%20Continuous%20Evaluation/) |

---

## Repository Structure Map

```text
.
├── 1. Moocs Review/
│   ├── Explore Machine Learning using Python.pdf
│   ├── Explore Machine Learning using Python.png
│   ├── Python for Data Science.pdf
│   └── Python for Data Science.png
│
├── 2. Mini or capstone project/
│   └── GLYCOS.ai/                                # Capstone project source code
│
└── 3. Lab Continuous Evaluation/                 # Weekly continuous evaluation log
    ├── Week 01/
    ├── Week 02/
    ├── Week 03/
    ├── Week 04/
    ├── Week 05/
    ├── Week 06/
    ├── Week 07/
    ├── Week 08/
    ├── Week 09/
    ├── Week 10/
    ├── Week 11/
    ├── Week 12/
    └── Week 13/
```

---

## 1. MOOCs Review (Max 40 Marks)

*Verification Status: Checked & Approved (20 Marks per course)*

1. **Course 1: Explore Machine Learning using Python**
   - **Platform:** Coursera (Google AI Partner)
   - **Credentials:** [Certificate PDF](./1.%20Moocs%20Review/Explore%20Machine%20Learning%20using%20Python.pdf) | [Certificate Image](./1.%20Moocs%20Review/Explore%20Machine%20Learning%20using%20Python.png)
2. **Course 2: Python for Data Science**
   - **Platform:** NPTEL (IBM Collaboration)
   - **Credentials:** [Certificate PDF](./1.%20Moocs%20Review/Python%20for%20Data%20Science.pdf) | [Certificate Image](./1.%20Moocs%20Review/Python%20for%20Data%20Science.png)

---

## 2. Capstone Project (Max 40 Marks)

### **GLYCOS.ai — Clinical Metabolic Susceptibility Engine**
An interactive machine learning dashboard designed to model and visualize susceptibility curves using multivariate logistic regression directly inside the browser.

* **Live Deployment Link:** [https://glycos-ai.vercel.app/](https://glycos-ai.vercel.app/)
* **Project Folder:** [`/2. Mini or capstone project/GLYCOS.ai`](./2.%20Mini%20or%20capstone%20project/GLYCOS.ai/)
* **Technology Stack:** Vite + React JS, Framer Motion, GSAP, Tailwind CSS, Recharts.

---

## 3. Lab Continuous Evaluation (Max 50 Marks)

Below is the complete weekly breakdown of laboratory experiments, implementations, and algorithms covered in this repository.

| Week | Folder Link | Primary Notebook | Core Algorithms & Topics Covered | Libraries Used |
| :---: | :--- | :--- | :--- | :--- |
| **01** | [`Week 01`](./3.%20Lab%20Continuous%20Evaluation/Week%2001/week-1/) | [`Introduction to Data Science Tools.ipynb`](./3.%20Lab%20Continuous%20Evaluation/Week%2001/week-1/Introduction%20to%20Data%20Science%20Tools.ipynb) | Google Colab, Anaconda setup, Jupyter Notebook, NumPy Arrays, Matrix Operations | NumPy |
| **02** | [`Week 02`](./3.%20Lab%20Continuous%20Evaluation/Week%2002/week-2/) | [`Data Cleaning Techniques.ipynb`](./3.%20Lab%20Continuous%20Evaluation/Week%2002/week-2/Data%20Cleaning%20Techniques.ipynb) | Handling missing values (mean imputation), handling duplicates, basic data wrangling | Pandas |
| **03** | [`Week 03`](./3.%20Lab%20Continuous%20Evaluation/Week%2003/week-3/) | [`Similarity and Dissimilarity Measures.ipynb`](./3.%20Lab%20Continuous%20Evaluation/Week%2003/week-3/Similarity%20and%20Dissimilarity%20Measures.ipynb) | Distance Measures (Euclidean, Manhattan, Minkowski, Cosine), Jaccard Similarity | NumPy, SciPy |
| **04** | [`Week 04`](./3.%20Lab%20Continuous%20Evaluation/Week%2004/week-4/) | [`Data Science Workflow.ipynb`](./3.%20Lab%20Continuous%20Evaluation/Week%2004/week-4/Data%20Science%20Workflow.ipynb) | Complete pipeline: ingestion, cleaning (imputation), scaling, correlation, and basic linear regression | NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn |
| **05** | [`Week 05`](./3.%20Lab%20Continuous%20Evaluation/Week%2005/week-5/) | [`Data Transformation and Dimensionality Reduction.ipynb`](./3.%20Lab%20Continuous%20Evaluation/Week%2005/week-5/Data%20Transformation%20and%20Dimensionality%20Reduction.ipynb) | Normalization (Min-Max), Standardization (Z-score), Label Encoding, One-Hot Encoding, PCA, LDA, t-SNE | Pandas, Seaborn, Scikit-learn, Matplotlib |
| **06** | [`Week 06`](./3.%20Lab%20Continuous%20Evaluation/Week%2006/week-6/) | [`Exploratory Data Analysis.ipynb`](./3.%20Lab%20Continuous%20Evaluation/Week%2006/week-6/Exploratory%20Data%20Analysis.ipynb) | Central Tendency (Mean, Median, Mode), Dispersion (Range, Variance, SD, IQR), Skewness, Kurtosis | Pandas, Scikit-learn |
| **07** | [`Week 07`](./3.%20Lab%20Continuous%20Evaluation/Week%2007/week-7/) | [`Data Visualization Techniques.ipynb`](./3.%20Lab%20Continuous%20Evaluation/Week%2007/week-7/Data%20Visualization%20Techniques.ipynb) | Univariate (Histogram, Boxplot, Pie), Bivariate (Scatter, Line, Bar), Multivariate (Heatmap, Bubble, Pairplot), Advanced (Violin, Joint, KDE) | Pandas, Seaborn, Matplotlib, Scikit-learn |
| **08** | [`Week 08`](./3.%20Lab%20Continuous%20Evaluation/Week%2008/week-8/) | [`Linear Algebra and Matrix Decomposition.ipynb`](./3.%20Lab%20Continuous%20Evaluation/Week%2008/week-8/Linear%20Algebra%20and%20Matrix%20Decomposition.ipynb) | LU Decomposition (Doolittle method) with forward/backward substitution, QR Decomposition (Gram-Schmidt method) | NumPy |
| **09** | [`Week 09`](./3.%20Lab%20Continuous%20Evaluation/Week%2009/week-9/) | [`Probability Distributions and Statistical Tests.ipynb`](./3.%20Lab%20Continuous%20Evaluation/Week%2009/week-9/Probability%20Distributions%20and%20Statistical%20Tests.ipynb) | Bernoulli, Binomial, Poisson, Geometric, Normal, Exponential, Z-Test, Independent t-test, Parametric & Non-Parametric tests | NumPy, SciPy, Matplotlib, statsmodels |
| **10** | [`Week 10`](./3.%20Lab%20Continuous%20Evaluation/Week%2010/week-10/) | [`Regression Models.ipynb`](./3.%20Lab%20Continuous%20Evaluation/Week%2010/week-10/Regression%20Models.ipynb) | Linear Regression (House Price Prediction), Logistic Regression (House Purchase Classification) | NumPy, Scikit-learn |
| **11** | [`Week 11`](./3.%20Lab%20Continuous%20Evaluation/Week%2011/week-11/) | [`Classification Algorithms.ipynb`](./3.%20Lab%20Continuous%20Evaluation/Week%2011/week-11/Classification%20Algorithms.ipynb) | Student Pass/Fail Prediction, Decision Tree (GridSearchCV, Cross-Validation, visualization), KNN classification, and multi-model benchmark | NumPy, Pandas, Scikit-learn, Matplotlib |
| **12** | [`Week 12`](./3.%20Lab%20Continuous%20Evaluation/Week%2012/week-12/) | [`K-Means Clustering + Hierarchical Clustering.ipynb`](./3.%20Lab%20Continuous%20Evaluation/Week%2012/week-12/K-Means%20Clustering%20+%20Hierarchical%20Clustering.ipynb) | Customer segmentation (K-Means, Hierarchical/Dendrogram), multi-clustering comparison (8 models), Elbow and Silhouette parameter tuning | NumPy, Pandas, Scikit-learn, Matplotlib, SciPy |
| **13** | [`Week 13`](./3.%20Lab%20Continuous%20Evaluation/Week%2013/week-13/) | [`Text Preprocessing and Recommendation.ipynb`](./3.%20Lab%20Continuous%20Evaluation/Week%2013/week-13/Text%20Preprocessing%20and%20Recommendation.ipynb) | Tokenization, Stopword removal, Stemming, TF-IDF Text Analytics, Naive Bayes Classifier, Cosine similarity, Collaborative filtering | Pandas, Matplotlib, Scikit-learn, NLTK |
