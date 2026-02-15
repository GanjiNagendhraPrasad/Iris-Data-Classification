<h1 align="center">🌸 Iris Data Classification</h1>

<h2>📌 Project Overview</h2>
<p>
This project is a complete <b>Machine Learning Classification Web Application</b> built using Flask.
It predicts the species of an iris flower based on user input features:
</p>

<ul>
  <li>Sepal Length</li>
  <li>Sepal Width</li>
  <li>Petal Length</li>
  <li>Petal Width</li>
</ul>

<p>
The application allows users to select between two machine learning algorithms:
</p>

<ul>
  <li><b>K-Nearest Neighbors (KNN)</b></li>
  <li><b>Naive Bayes (GaussianNB)</b></li>
</ul>

<p>
After prediction, the application also displays the test performance metrics of the selected model.
</p>

<hr>

<h2>🎯 Objective</h2>
<ul>
  <li>Implement multiple classification algorithms</li>
  <li>Compare their performance</li>
  <li>Deploy using a Flask web interface</li>
  <li>Display real-time predictions along with model evaluation metrics</li>
</ul>

<hr>

<h2>📊 Dataset</h2>
<p>
The project uses the famous <b>Iris Dataset</b>, which contains:
</p>

<ul>
  <li>150 samples</li>
  <li>3 flower species:
    <ul>
      <li>Setosa</li>
      <li>Versicolor</li>
      <li>Virginica</li>
    </ul>
  </li>
  <li>4 numerical features:
    <ul>
      <li>Sepal Length (cm)</li>
      <li>Sepal Width (cm)</li>
      <li>Petal Length (cm)</li>
      <li>Petal Width (cm)</li>
    </ul>
  </li>
</ul>

<p>
Preprocessing steps:
</p>

<ul>
  <li>Removed unnecessary column (Id)</li>
  <li>Encoded species into numerical values</li>
  <li>Split data into 80% training and 20% testing</li>
</ul>

<hr>

<h2>🤖 Machine Learning Models Used</h2>

<h3>1️⃣ K-Nearest Neighbors (KNN)</h3>
<ul>
  <li>Used <code>KNeighborsClassifier</code></li>
  <li>Optimal K value selected using odd values</li>
  <li>Model trained on training data</li>
  <li>Saved using Pickle (<code>Knn.pkl</code>)</li>
</ul>

<h3>2️⃣ Naive Bayes (GaussianNB)</h3>
<ul>
  <li>Used <code>GaussianNB</code></li>
  <li>Assumes features follow Gaussian distribution</li>
  <li>Fast and efficient probabilistic classifier</li>
  <li>Saved using Pickle (<code>Nb.pkl</code>)</li>
</ul>

<hr>

<h2>📈 Model Evaluation</h2>
<p>
For both models, the following test performance metrics were calculated and saved into JSON files:
</p>

<ul>
  <li>Confusion Matrix</li>
  <li>Classification Report</li>
  <li>Accuracy Score</li>
</ul>

<p>
Performance JSON files:
</p>

<ul>
  <li><code>knn_test_performance.json</code></li>
  <li><code>nb_test_performance.json</code></li>
</ul>

<hr>

<h2>🌐 Web Application (Flask)</h2>
<p>The Flask application:</p>

<ul>
  <li>Accepts user inputs for 4 flower features</li>
  <li>Allows selection between KNN and Naive Bayes</li>
  <li>Displays predicted species</li>
  <li>Shows test performance metrics of selected model</li>
</ul>

<hr>

<h2>🛠️ Technologies Used</h2>
<ul>
  <li>Python</li>
  <li>NumPy</li>
  <li>Pandas</li>
  <li>Scikit-learn</li>
  <li>Flask</li>
  <li>HTML & CSS</li>
  <li>Pickle (Model Serialization)</li>
  <li>JSON (Performance Storage)</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>

<pre>
Iris-Data-Classification/
│
├── app.py
├── Knn.pkl
├── Nb.pkl
├── knn_test_performance.json
├── nb_test_performance.json
├── templates/
│   └── index.html
└── README.md
</pre>

<hr>

<h2>🚀 How to Run the Project</h2>

<ol>
  <li>Clone the repository:
    <pre>git clone https://github.com/GanjiNagendhraPrasad/Iris-Data-Classification.git</pre>
  </li>

  <li>Install required libraries:
    <pre>pip install flask numpy pandas scikit-learn</pre>
  </li>

  <li>Run the application:
    <pre>python app.py</pre>
  </li>

  <li>Open in browser:
    <pre>http://127.0.0.1:5000/</pre>
  </li>
</ol>

<hr>

<h2>💡 Key Learning Outcomes</h2>
<ul>
  <li>Understanding classification algorithms</li>
  <li>Comparing multiple ML models</li>
  <li>Model serialization using Pickle</li>
  <li>Saving evaluation metrics in JSON</li>
  <li>Building a Flask-based ML deployment</li>
  <li>Connecting backend ML models to frontend UI</li>
</ul>

<hr>

<h2>📌 Future Improvements</h2>
<ul>
  <li>Add model comparison graph</li>
  <li>Deploy to cloud platforms</li>
  <li>Add cross-validation metrics</li>
  <li>Add confusion matrix visualization</li>
  <li>Improve UI design</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>
<p><b>G. Nagendhra Prasad</b><br>
Machine Learning Enthusiast</p>
