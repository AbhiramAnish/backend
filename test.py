import pickle

# Load both ML models safely
def load_model(path):
    try:
        with open(path, "rb") as model_file:
            return pickle.load(model_file)
    except Exception as e:
        print(f"Error loading model {path}: {e}")
        return None

model2 = load_model("mark_1_Landslide2.pkl")  # New second model
print(model2)
print(f" Model 2 Type: {type(model2)}")