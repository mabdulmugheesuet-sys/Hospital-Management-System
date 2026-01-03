
# Hospital Management System
# Admin View + Patient View
# Core Python Only (No Libraries)
# ==============================

patients = {}

# ---------- FILE HANDLING ----------

def load_data():
    try:
        file = open("hospital_data.txt", "r")
        for line in file:
            line = line.strip()
            if line == "":
                continue

            parts = line.split("|")

            # SAFETY CHECK (PERMANENT FIX)
            if len(parts) != 8:
                continue

            pid = parts[0]
            name = parts[1]
            age = parts[2]
            gender = parts[3]
            disease = parts[4]
            doctor = parts[5]

            history = []
            if parts[6] != "":
                history = parts[6].split(",")

            bill = []
            if parts[7] != "":
                for b in parts[7].split(","):
                    bill.append(int(b))

            patients[pid] = {
                "name": name,
                "age": age,
                "gender": gender,
                "disease": disease,
                "doctor": doctor,
                "history": history,
                "bill": bill
            }
        file.close()
    except FileNotFoundError:
        pass
