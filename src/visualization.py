import matplotlib.pyplot as plt
import seaborn as sns

def plot_cancellation_rates(df):
    plt.figure(figsize=(8,6))
    sns.countplot(x='is_canceled', data=df, palette='viridis')
    plt.title('Distribution of Cancellations')
    plt.show()

def plot_lead_time_distribution(df):
    plt.figure(figsize=(10,6))
    sns.histplot(data=df, x='lead_time', hue='is_canceled', kde=True, element='step')
    plt.title('Lead Time Distribution by Cancellation Status')
    plt.show()

def plot_monthly_arrivals(df):
    plt.figure(figsize=(12,6))
    sns.countplot(x='arrival_date_month', hue='hotel', data=df)
    plt.title('Monthly Arrivals: City Hotel vs Resort Hotel')
    plt.xticks(rotation=45)
    plt.show()
