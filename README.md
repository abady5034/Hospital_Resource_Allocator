
## 📌 Project Description

This project is a **Hospital Resource Management System** implemented using  
a **Greedy Best‑First Search (GBFS) Scheduling Algorithm**.

The goal of this project is to simulate real-life hospital resource allocation  
while efficiently assigning limited resources such as:

- Doctors 👨‍⚕️  
- Rooms 🛏️  
- Equipment ⚙️  

Patients are scheduled based on:

- Arrival Time  
- Urgency Level  

to ensure optimal resource utilization and reduced waiting time.

---

## ✨ Features

- Allocate patients based on urgency level (1 → 5)
- Dynamic assignment of Doctor / Room / Equipment
- Efficient scheduling of incoming patients
- Reduced waiting time for critical cases
- Resource utilization tracking
- Untreated patients detection
- Average waiting time calculation
- GUI Visualization using Tkinter

---

## 🧠 Dataset Used

Each patient record includes:

- Patient ID
- Urgency Level
- Required Resource Type
- Arrival Time

Simulation includes:

- 60 patients
- Different urgency levels
- Different arrival times

Which helps simulate:

- Waiting queues
- Resource competition
- Priority‑based scheduling

---

## 🏨 Hospital Resources

The hospital contains limited resources:

| Resource | Quantity |
|----------|----------|
| Doctors  | 5 |
| Rooms    | 4 |
| Equipment| 3 |


---

## ⚙️ Algorithm Used

### 🟥 Greedy Best‑First Search (GBFS)

The system follows these steps:

1. Sort patients by arrival time
2. If arrival time equal → prioritize higher urgency
3. Select highest urgency arrived patient
4. Find earliest available required resource
5. Assign treatment slot
6. Update resource availability
7. Calculate waiting time
8. Track untreated patients

---

## 🔢 Sorting Method

Patients are sorted using:

✅ Optimized **Bubble Sort Algorithm**

Sorting Priority:

1. Arrival Time → Ascending  
2. Urgency Level → Descending  

---

## 📊 Simulation Output

After running the simulation, the system generates:

- Treatment Schedule
- Waiting Time per Urgency Level
- Resource Utilization Percentage
- Untreated Patients List

---

## 🖥️ GUI Interface

Tkinter GUI provides:

- ▶️ Run Simulation Button
- 📊 Allocation Schedule Table
- 📝 Summary Results Panel
- 🎨 Color‑coded rows based on urgency level
