import csv
import pandas as pd

arr = []
with open("information_history.csv", newline="") as csvfile:
    rdr = csv.DictReader(csvfile)
    for i in rdr:
        if i.get("information_type") == "experiment_information":
            is_feature_flag = False
            if i.get("is_feature_flag") == "1":
                is_feature_flag = True
            arr.append({"experiment_key": i.get("experiment_key"),
                        "description": i.get("description"),
                        "is_feature_flag": is_feature_flag,
                        "first_triggered_at": i.get("first_triggered_at"),
                        "updated_at":  i.get("created_at")})

arr.sort(key=lambda k:k["experiment_key"])
df = pd.DataFrame(arr)
df.to_csv("history.csv", encoding="utf-8-sig")