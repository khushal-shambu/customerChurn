import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv(filepath_or_buffer="data/raw/telecom_churn.csv")
df.isna().sum()