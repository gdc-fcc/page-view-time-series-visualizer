import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import numpy as np
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df['date'] = pd.to_datetime(df['date'])

# Clean data
df = df.loc[
    (df['value'] <= df['value'].quantile(0.975)) &
    (df['value'] >= df['value'].quantile(0.025))
]

def draw_line_plot():
    # Draw line plot
    #plt.plot(df['date'], df['value'])
    #fig = plt.figure() 
    fig = plt.figure(figsize=(20,6))

    plt.plot(df['date'], df['value'], "r")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.strftime('%B') for d in df_bar.date]
    df_bar['new'] = [d.strftime('%m') for d in df_bar.date]

    fig, ax = plt.subplots(figsize=(10, 10))
    df_bar3 = df_bar.groupby(['month', 'year', 'new'], as_index=False).agg({'value': 'mean'})
    df_bar3=df_bar3.sort_values('new')
    sns.barplot(data = df_bar3, x = 'year', y = 'value', hue = 'month')
    ax.legend(loc='upper left', title='Months')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')

    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['new'] = [d.strftime('%m') for d in df_box.date]
    df_box=df_box.sort_values('new')

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2)

    sns.boxplot(ax=ax1, x = df_box["year"], y = df_box["value"]).set(
        title='Year-wise Box Plot (Trend)', xlabel="Year", ylabel="Page Views")
    sns.boxplot(ax=ax2, data=df_box, x = "month", y = "value").set(
        title='Month-wise Box Plot (Seasonality)', xlabel="Month", ylabel="Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

