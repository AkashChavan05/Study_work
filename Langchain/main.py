from app import main ,ngrok_call
import os

ngrok_call()

command ="streamlit run /kaggle/input/lang-trial_1/app.py"

os.system(command=command)