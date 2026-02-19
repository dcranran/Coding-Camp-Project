import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv("https://raw.githubusercontent.com/dcranran/Bike-Sharing-Dashboard/main/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/dcranran/Bike-Sharing-Dashboard/main/hour.csv")                    

day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Title
st.title("🚴‍♂️ Dashboard Analisis Penyewaan Sepeda 🚴‍♂️")
st.write("Dashboard interaktif untuk mengeksplorasi tren penyewaan sepeda berdasarkan cuaca, musim, dan waktu.")

# Sidebar 
st.sidebar.header("📊 Pilih Visualisasi")
option = st.sidebar.selectbox("Pilih kategori:", [
    "Tren Penyewaan Sepeda",
    "Pengaruh Cuaca dan Musim",
    "Pola Penyewaan Berdasarkan Waktu",
    "Clustering Penyewaan Sepeda"
])

st.sidebar.header("🕒 Pilih Rentang Waktu")
start_date = st.sidebar.date_input("Mulai dari:", day_df["dteday"].min())
end_date = st.sidebar.date_input("Hingga:", day_df["dteday"].max())

day_df_filtered = day_df[(day_df["dteday"] >= pd.to_datetime(start_date)) & (day_df["dteday"] <= pd.to_datetime(end_date))]
hour_df_filtered = hour_df[(hour_df["dteday"] >= pd.to_datetime(start_date)) & (hour_df["dteday"] <= pd.to_datetime(end_date))]

# Tren Penyewaan Sepeda dari Waktu ke Waktu
if option == "Tren Penyewaan Sepeda":
    st.subheader("📈 Tren Penyewaan Sepeda dari Waktu ke Waktu")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x="dteday", y="cnt", data=day_df_filtered, ax=ax, color="#EB5679")
    ax.set_title("Jumlah Penyewaan Sepeda dari Waktu ke Waktu")
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Jumlah Penyewaan")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Pengaruh Cuaca dan Musim
elif option == "Pengaruh Cuaca dan Musim":
    st.subheader("🌦️ Pengaruh Cuaca dan Musim terhadap Penyewaan Sepeda")
    
    fig, axes = plt.subplots(3, 2, figsize=(14, 10))
    sns.boxplot(x="weathersit", y="cnt", data=day_df_filtered, ax=axes[0, 0], palette="Set3")
    axes[0, 0].set_title("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")
    axes[0, 0].set_xticklabels(["Cerah", "Mendung", "Hujan Ringan", "Hujan Lebat"])
    
    sns.boxplot(x="season", y="cnt", data=day_df_filtered, ax=axes[0, 1], palette="Set2")
    axes[0, 1].set_title("Pengaruh Musim terhadap Penyewaan Sepeda")
    axes[0, 1].set_xticklabels(["Spring", "Summer", "Fall", "Winter"])
    
    sns.regplot(x="temp", y="cnt", data=day_df_filtered, ax=axes[1, 0], color="#EB5679", scatter_kws={"alpha": 0.6}, line_kws={"color": "blue"})
    axes[1, 0].set_title("Pengaruh Suhu terhadap Penyewaan Sepeda")
    
    sns.regplot(x="atemp", y="cnt", data=day_df_filtered, ax=axes[1, 1], color="#EB5679", scatter_kws={"alpha": 0.6}, line_kws={"color": "blue"})
    axes[1, 1].set_title("Pengaruh Suhu Terasa terhadap Penyewaan Sepeda")
    
    sns.regplot(x="hum", y="cnt", data=day_df_filtered, ax=axes[2, 0], color="#EB5679", scatter_kws={"alpha": 0.6}, line_kws={"color": "blue"})
    axes[2, 0].set_title("Pengaruh Kelembaban terhadap Penyewaan Sepeda")
    
    sns.regplot(x="windspeed", y="cnt", data=day_df_filtered, ax=axes[2, 1], color="#EB5679", scatter_kws={"alpha": 0.6}, line_kws={"color": "blue"})
    axes[2, 1].set_title("Pengaruh Kecepatan Angin terhadap Penyewaan Sepeda")
    
    plt.tight_layout()
    st.pyplot(fig)

# Pola Penyewaan Berdasarkan Waktu
elif option == "Pola Penyewaan Berdasarkan Waktu":
    st.subheader("⏳ Pola Penyewaan Berdasarkan Bulan, Hari, dan Jam")
    
    fig, axes = plt.subplots(3, 1, figsize=(14, 10))

    colors = ["#D3D3D3"] * 12  
    min_mnth = day_df_filtered.groupby("mnth")["cnt"].sum().idxmin()
    max_mnth = day_df_filtered.groupby("mnth")["cnt"].sum().idxmax()

    colors[min_mnth - 1] = "#F189B8"  
    colors[max_mnth - 1] = "#87CEEB"  

    sns.barplot(x="mnth", y="cnt", data=day_df_filtered, ax=axes[0], order=range(1, 13), palette=colors)
    axes[0].set_title("Jumlah Penyewaan Sepeda Berdasarkan Bulan")
    axes[0].set_xticklabels(["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"])

    weekday_colors = ["#D3D3D3"] * 7
    min_day = day_df_filtered.groupby("weekday")["cnt"].sum().idxmin()
    max_day = day_df_filtered.groupby("weekday")["cnt"].sum().idxmax()
    weekday_colors[min_day] = "#F189B8"
    weekday_colors[max_day] = "#87CEEB"

    sns.barplot(x="weekday", y="cnt", data=day_df_filtered, ax=axes[1], order=range(0, 7), palette=weekday_colors)
    axes[1].set_title("Jumlah Penyewaan Sepeda Berdasarkan Hari dalam Seminggu")
    axes[1].set_xticklabels(["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"])

    hour_colors = ["#D3D3D3"] * 24
    min_hr = hour_df_filtered.groupby("hr")["cnt"].sum().idxmin()
    max_hr = hour_df_filtered.groupby("hr")["cnt"].sum().idxmax()
    hour_colors[min_hr] = "#F189B8"
    hour_colors[max_hr] = "#87CEEB"

    sns.barplot(x="hr", y="cnt", data=hour_df_filtered, ax=axes[2], order=range(0, 24), palette=hour_colors)
    axes[2].set_title("Jumlah Penyewaan Sepeda Berdasarkan Jam dalam Sehari")

    plt.tight_layout()
    st.pyplot(fig)

# Clustering Penyewaan Sepeda
elif option == "Clustering Penyewaan Sepeda":
    st.subheader("🔍 Clustering Penyewaan Sepeda")
    
    bins = [0, 2000, 4000, day_df_filtered['cnt'].max()]
    labels = ["Low Demand", "Medium Demand", "High Demand"]
    day_df_filtered["demand_category"] = pd.cut(day_df_filtered["cnt"], bins=bins, labels=labels, include_lowest=True)
    demand_distribution = day_df_filtered["demand_category"].value_counts()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(demand_distribution, labels=demand_distribution.index, autopct='%1.1f%%', colors=["lightblue", "lightyellow", "pink"])
    ax.set_title("Distribusi Clustering Penyewaan Sepeda")
    
    st.pyplot(fig)

st.sidebar.write("\n📢 **Petunjuk**: Pilih kategori visualisasi dan rentang waktu untuk melihat analisis data secara interaktif.")