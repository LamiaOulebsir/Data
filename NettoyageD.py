import pandas as pd
import os


# Change le répertoire de travail pour celui du script
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Nouveau répertoire de travail:", os.getcwd())

dat = pd.read_csv("Apprentissage.csv")
print(dat)


