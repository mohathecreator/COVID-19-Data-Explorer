# 🦠 COVID-19 Data Explorer  

## 📌 Project Overview  
This project provides an **interactive Python tool** for exploring and visualizing **COVID-19 data**. Users can select a **country**, a **time period**, and a **data type** (**confirmed cases, deaths, or recoveries**) to generate a visual representation of the data.  

The dataset is sourced from the **Johns Hopkins University COVID-19 repository**.

---

## 🛠️ Steps in the Project  

### 1️⃣ Data Loading & Preparation  
- Fetched **COVID-19 data** from the [Johns Hopkins GitHub Repository](https://github.com/CSSEGISandData/COVID-19).  
- Cleaned and transformed the dataset using **Pandas**.  
- Converted the dataset into a structured format with **date, country, and case numbers**.  

### 2️⃣ User Input Handling  
- Implemented a **console-based interface** where users can:  
  - Select a **country**.  
  - Choose a **data type** (**confirmed, deaths, recovered, or all**).  
  - Define a **start and end date**.  

### 3️⃣ Data Filtering  
- Applied filters based on user input to extract relevant data.  
- Handled edge cases such as **invalid country names** or **date formats**.  

### 4️⃣ Data Visualization with Plotly  
- Created **interactive line charts** to display COVID-19 trends.  
- Customized the **plot titles** dynamically based on user selection.  

---

## 📌 Key Features  
✅ Fetches **live COVID-19 data** directly from the Johns Hopkins repository.  
✅ **Interactive selection** of country, time period, and case type.  
✅ **Dynamic plots** using **Plotly** for better visualization.   

---

## 🚀 Future Enhancements  
- **Advanced analytics**: Implement **moving averages** and **growth rate calculations**.  
- **Multi-country comparison**: Allow users to compare multiple countries in a single chart.  

---

## 📂 Installation & Usage  
To run this project locally, follow these steps:  

### 🔹 Install dependencies  
```bash
pip install pandas plotly requests
```

### 🔹 Run the script
```bash
python covid_data_explorer.py
```

---

## 📊 Dataset Information
The dataset is maintained by Johns Hopkins University and contains:
- Global COVID-19 case data since January 2020.
- Confirmed cases, deaths, and recoveries by country and date.

For more details, visit the [COVID-19 Data Repository](https://github.com/CSSEGISandData/COVID-19).

## 🤝 Contributing

Feel free to contribute by:
- Enhancing the visualization options.
- Improving the user input system.
- Adding support for real-time API data sources.

---

## ⭐ If you find this project useful, consider giving it a star on GitHub!

