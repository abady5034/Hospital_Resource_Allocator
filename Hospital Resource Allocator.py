# Data Set
patients = [
    {"id": 121, "urgency": 5, "type": "Doctor", "arrival": 1},
    {"id": 132, "urgency": 3, "type": "Room", "arrival": 2},
    {"id": 136, "urgency": 4, "type": "Equipment", "arrival": 1},
    {"id": 140, "urgency": 2, "type": "Doctor", "arrival": 4},
    {"id": 159, "urgency": 1, "type": "Room", "arrival": 5},
    {"id": 162, "urgency": 5, "type": "Equipment", "arrival": 3},
    {"id": 171, "urgency": 4, "type": "Doctor", "arrival": 2},
    {"id": 187, "urgency": 3, "type": "Room", "arrival": 2},
    {"id": 190, "urgency": 2, "type": "Equipment", "arrival": 2},
    {"id": 101, "urgency": 5, "type": "Doctor", "arrival": 5},
    {"id": 255, "urgency": 5, "type": "Doctor", "arrival": 1},
    {"id": 298, "urgency": 3, "type": "Room", "arrival": 2},
    {"id": 245, "urgency": 4, "type": "Equipment", "arrival": 1},
    {"id": 256, "urgency": 2, "type": "Doctor", "arrival": 4},
    {"id": 213, "urgency": 1, "type": "Room", "arrival": 5},
    {"id": 241, "urgency": 5, "type": "Equipment", "arrival": 9},
    {"id": 233, "urgency": 4, "type": "Doctor", "arrival": 2},
    {"id": 212, "urgency": 3, "type": "Room", "arrival": 2},
    {"id": 211, "urgency": 2, "type": "Equipment", "arrival": 2},
    {"id": 222, "urgency": 5, "type": "Doctor", "arrival": 5},
    {"id": 111, "urgency": 1, "type": "Room", "arrival": 2},
    {"id": 122, "urgency": 4, "type": "Equipment", "arrival": 1},
    {"id": 130, "urgency": 3, "type": "Doctor", "arrival": 4},
    {"id": 145, "urgency": 2, "type": "Room", "arrival": 7},
    {"id": 152, "urgency": 5, "type": "Equipment", "arrival": 4},
    {"id": 161, "urgency": 4, "type": "Doctor", "arrival": 2},
    {"id": 177, "urgency": 3, "type": "Room", "arrival": 3},
    {"id": 185, "urgency": 2, "type": "Equipment", "arrival": 4},
    {"id": 119, "urgency": 1, "type": "Doctor", "arrival": 9},
    {"id": 120, "urgency": 5, "type": "Room", "arrival": 8},
    {"id": 123, "urgency": 4, "type": "Equipment", "arrival": 5},
    {"id": 102, "urgency": 3, "type": "Doctor", "arrival": 1},
    {"id": 103, "urgency": 2, "type": "Room", "arrival": 3},
    {"id": 124, "urgency": 1, "type": "Equipment", "arrival": 6},
    {"id": 125, "urgency": 5, "type": "Doctor", "arrival": 4},
    {"id": 106, "urgency": 4, "type": "Room", "arrival": 2},
    {"id": 137, "urgency": 3, "type": "Equipment", "arrival": 1},
    {"id": 128, "urgency": 2, "type": "Doctor", "arrival": 12},
    {"id": 109, "urgency": 1, "type": "Room", "arrival": 11},
    {"id": 112, "urgency": 5, "type": "Equipment", "arrival": 6},
    {"id": 311, "urgency": 1, "type": "Room", "arrival": 2},
    {"id": 422, "urgency": 4, "type": "Equipment", "arrival": 1},
    {"id": 530, "urgency": 3, "type": "Doctor", "arrival": 4},
    {"id": 645, "urgency": 2, "type": "Room", "arrival": 7},
    {"id": 352, "urgency": 5, "type": "Equipment", "arrival": 4},
    {"id": 561, "urgency": 4, "type": "Doctor", "arrival": 2},
    {"id": 677, "urgency": 3, "type": "Room", "arrival": 3},
    {"id": 85, "urgency": 2, "type": "Equipment", "arrival": 4},
    {"id": 719, "urgency": 1, "type": "Doctor", "arrival": 9},
    {"id": 720, "urgency": 5, "type": "Room", "arrival": 8},
    {"id": 923, "urgency": 4, "type": "Equipment", "arrival": 5},
    {"id": 802, "urgency": 3, "type": "Doctor", "arrival": 1},
    {"id": 703, "urgency": 2, "type": "Room", "arrival": 3},
    {"id": 624, "urgency": 1, "type": "Equipment", "arrival": 6},
    {"id": 625, "urgency": 5, "type": "Doctor", "arrival": 4},
    {"id": 506, "urgency": 4, "type": "Room", "arrival": 2},
    {"id": 537, "urgency": 3, "type": "Equipment", "arrival": 1},
    {"id": 628, "urgency": 2, "type": "Doctor", "arrival": 1},
    {"id": 709, "urgency": 1, "type": "Room", "arrival": 1},
    {"id": 812, "urgency": 5, "type": "Equipment", "arrival": 6},
]
# Resources
resources = {"Doctor": 5, "Room": 4, "Equipment": 3}
resource_free = {
    "Doctor": [0] * 5,
    "Room": [0] * 4,
    "Equipment": [0] * 3
}
# Sorting
def sort_patients(patients):
    n=len(patients)  #عدد العناصر اللي جوا الليست
    for i in range(n):
        flag = True
        for j in range(n-i-1):
            if patients[j]["arrival"] > patients[j+1]["arrival"]:
                temp=patients[j]
                patients[j] = patients[j+1]
                patients[j+1] = temp
                flag=False
            elif patients[j]["arrival"] == patients[j+1]["arrival"]:
                if patients[j]["urgency"] < patients[j + 1]["urgency"]:
                    temp = patients[j]
                    patients[j] = patients[j + 1]
                    patients[j + 1] = temp
                    flag=False
        if flag:
            break
sort_patients(patients)
# Greedy Best First Search
def GBFS_hospital(patients):
    resource_free={
        "Doctor":[0] *5,
        "Room":[0]*4,
        "Equipment":[0]*3     
    }
    schedule = []
    wait_times = {i: [] for i in range(1, 6)}
    total_busy_time = {"Doctor": 0, "Room": 0, "Equipment": 0}
    not_tread = [] 
    treated = [False] * len(patients)
    processed_count = 0 
    current_time = 0
    while processed_count < len(patients):
        available = [(i, p) for i, p in enumerate(patients) 
        if not treated[i] and p['arrival'] <= current_time]

        if not available:
            next_arrivals = [p['arrival'] for i, p in enumerate(patients) if not treated[i]]
            if next_arrivals:
                current_time = min(next_arrivals)
                continue
            else:
                break

        target_idx, patient = max(available, key=lambda x: (x[1]['urgency'], -x[1]['arrival']))
        
        patient_type = patient["type"]
        resource_free[patient_type].sort()
        early_free = resource_free[patient_type][0]

        start_time = max(patient['arrival'], early_free)

        if start_time > 120:
            not_tread.append(patient['id'])
            treated[target_idx] = True
            processed_count += 1
            continue

        end_time = start_time + 10
        wait_time = start_time - patient['arrival']
        
        resource_free[patient_type][0] = end_time
        treated[target_idx] = True
        processed_count += 1
        
        schedule.append({
            "ID": patient['id'], "Type": patient_type,
            "Start": start_time, "End": end_time,
            "Urgency": patient['urgency']
        })
        wait_times[patient['urgency']].append(wait_time)
        total_busy_time[patient_type] += 10
        current_time = min(min(v) for v in resource_free.values())

    return schedule, wait_times, total_busy_time, not_tread
# Simulation 
results, waits, usage, ignored = GBFS_hospital(patients)
print(f"{'Patient ID':<10} | {'Type':<10} | {'Start':<6} | {'End':<6}")
print("-" * 55)
for r in results:
    print(f"{r['ID']:<10} | {r['Type']:<10} | {r['Start']:<6} | {r['End']:<6}")

untread_count = len(ignored)
print(f"\nTotal patients untread = {untread_count}")
if untread_count > 0:
    print(f"Untreated Patient IDs: {ignored}")

print("\n--- Average Wait Time ---")
for urg in range(5, 0, -1):
    avg = sum(waits[urg])/len(waits[urg]) if waits[urg] else 0
    print(f"Urgency {urg}: {avg:.1f} mins")


print("\n--- Resource Usage ---")
for r_type, busy in usage.items():
    total_available = 120 * resources[r_type]
    percent = (busy / total_available) * 100
    print(f"{r_type}: {percent:.1f}%")

#GUI   
import tkinter as tk
from tkinter import ttk

def run_simulation():
    results, waits, usage, ignored = GBFS_hospital(patients)


    for row in tree.get_children():
        tree.delete(row)
    for r in results:
        tag = f"urg{r['Urgency']}"
        tree.insert("", "end", values=(r["ID"], r["Type"], r["Start"], r["End"], r["Urgency"]), tags=(tag,))
    output_text.delete("1.0", tk.END)

    output_text.insert(tk.END, "=== Average Wait Time ===\n")
    for urg in range(5, 0, -1):
        avg = sum(waits[urg])/len(waits[urg]) if waits[urg] else 0
        output_text.insert(tk.END, f"Urgency {urg}: {avg:.1f} mins\n")

    output_text.insert(tk.END, "\n=== Resource Usage ===\n")
    for r_type, busy in usage.items():
        total_available = 120 * resources[r_type]
        percent = (busy / total_available) * 100
        output_text.insert(tk.END, f"{r_type}: {percent:.1f}%\n")

    output_text.insert(tk.END, f"\n=== Untreated Patients ===\n")
    output_text.insert(tk.END, f"Count: {len(ignored)}\nIDs: {ignored}")
root = tk.Tk()
root.title(" Hospital Resource Allocator")
root.geometry("1500x1400")
root.configure(bg="#f0f4f7")

title = tk.Label(root, text="Hospital Resource Allocator", 
                font=("Arial", 18, "bold"), bg="#f0f4f7", fg="#2c3e50")
title.pack(pady=10)
btn = tk.Button(root, text="▶ Run Simulation", command=run_simulation,
                font=("Arial", 12, "bold"),
                bg="#3498db", fg="white",
                padx=10, pady=5)
btn.pack(pady=10)
frame = tk.Frame(root)
frame.pack()

columns = ("ID", "Type", "Start", "End", "Urgency")
tree = ttk.Treeview(frame, columns=columns, show="headings", height=15)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=100)

tree.pack(pady=10,padx=20,fill="both",expand=True)
tree.tag_configure("urg5", background="#ff6b6b")  # أحمر
tree.tag_configure("urg4", background="#ffa94d")  # برتقالي
tree.tag_configure("urg3", background="#fff176")  # أصفر
tree.tag_configure("urg2", background="#69db7c")  # أخضر
tree.tag_configure("urg1", background="#74c0fc")  # أزرق

# output
output_text = tk.Text(root, height=15, width=90, font=("Consolas", 10))
output_text.pack(pady=10,padx=10)

root.mainloop()