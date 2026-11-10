# youtube analytics Dashboard
 🛠️ Tech Stack
* **Python** (Core programming)
* **Pandas** (Data cleaning and manipulation)
* **Streamlit** (Interactive web app framework)
* **Plotly Express** (Interactive data visualization)

## 🚀 Key Features
* **Data Cleaning:** Standardized column names, converted numeric fields, removed duplicates, and filled missing values with the median.
* **KPI Cards:** Quick overview of Total Views, Likes, Comments, and Average Engagement.
* **Visualizations:** Bar, pie, line, and scatter charts analyzing performance by category, country, and year.
* **Engagement Metric:** Calculated a custom engagement rate `((Likes + Comments) / Views) * 100` and analyzed its correlation with total views.
* **Interactivity:** Fully functional filters for Category, Country, and Year, plus a video/channel search bar.
* **Data Export:** Users can upload their own CSV datasets and download filtered results.
##  📁 How to Run Locally
1. Clone this repository.
2. Install the required libraries: `pip install streamlit pandas numpy plotly`
3. Run the app: `streamlit run app.py`
```
