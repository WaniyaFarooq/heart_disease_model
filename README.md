# Assignment 2 — Heart Disease Prediction

## Files
- `Assignment_2_Heart_Disease_Solution.ipynb`: notebook workflow and explanations.
- `app.py`: Streamlit interface for deployment.
- `requirements.txt`: packages required by the web app.

## Run locally
1. Run all notebook cells to download the dataset, train the model, and create `heart_disease_model.joblib`.
2. Install dependencies: `python -m pip install -r requirements.txt`
3. Start app: `streamlit run app.py`

## Deploy
Commit `app.py`, `requirements.txt`, and the generated `heart_disease_model.joblib` to a GitHub repository. Deploy `app.py` using Streamlit Community Cloud. Add the actual public URL to the top of your notebook. Never invent a deployment URL.

Educational project only; not for medical diagnosis.
