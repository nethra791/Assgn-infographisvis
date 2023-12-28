import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def getlabel(x):
    """
    Generates a label for a pie chart segment based on the given income group.

    Parameters:
    - x (str): The income group for which the label is generated.

    Returns:
    str: A formatted label including the income group and its percentage.

    """
    percentage = data_piechart.iloc[:, 1][data_piechart['Income Group'] 
                                          == x].values[0]
    return f"{x} ({percentage:.1f}%)"


# Setting the default font globally
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.weight'] = 'bold'

# fetching the datasets from the CSV files
data_lineplot = pd.read_csv('LinePlot.csv')
data_piechart = pd.read_csv('Piechart.csv')
data_vbargraph = pd.read_csv('VBarGraph.csv')
data_hbargraph = pd.read_csv('HBarGraph.csv')

# Setting up the plot dimensions
fig = plt.figure(figsize=(20, 24), facecolor='#E6E6FA')
gs = gridspec.GridSpec(5, 2, height_ratios=[2, 2, 2, 2, 0.5])

# Adding the main title for the Plot
plt.suptitle(
    "Global Trends in Cereal Production: A 1960-2020 Overview", 
    fontsize=30, y=0.96, fontweight='bold'
)

# Plot 1: Line Plot for Region-wise Cereal Production
plot1 = plt.subplot(gs[1, 1])
plot1.plot(
    data_lineplot.columns[2:], 
    data_lineplot.iloc[:, 2:].T, 
    linewidth=4
)
plot1.set_title(
    'Region-wise Cereal Production (1960-2020)', 
    fontsize=16, fontweight='bold', pad=20
)
plot1.set_xlabel('Years', fontsize=14, fontweight='bold')
plot1.set_ylabel('Cereal Production (in tons)', fontsize=14, fontweight='bold')
plot1.tick_params(axis='both', which='major', labelsize=12)

# Plot 2: Donut Chart for Cereal Production by Income Group in 2020
plot2 = plt.subplot(gs[1, 0])
pie_labels = data_piechart['Income Group'].apply(getlabel)

plot2.pie(
    data_piechart.iloc[:, 1], 
    labels=pie_labels, 
    startangle=90
)
donut_hole = plt.Circle((0, 0), 0.4, color='white')
plot2.add_artist(donut_hole)
plot2.set_title(
    'Cereal Production by Income Group in 2020', 
    fontsize=16, fontweight='bold', pad=20
)

# Plot 3: Vertical Bar Graph for Worldwide Cereal Production
plot3 = plt.subplot(gs[0, :])
years = range(len(data_vbargraph.columns[1:]))
bar_width = 0.5
for i, region in enumerate(data_vbargraph['Region']):
    plot3.bar(
        [x + i * bar_width for x in years], 
        data_vbargraph.iloc[i, 1:], 
        width=bar_width
    )
plot3.set_xticks(
    [x + bar_width * (len(data_vbargraph['Region']) / 2 - 0.5) for x in years]
)
plot3.set_xticklabels(data_vbargraph.columns[1:], fontsize=12)
plot3.set_title(
    'Worldwide Cereal Production (1960-2020)', 
    fontsize=16, fontweight='bold', pad=20
)
plot3.set_xlabel('Years', fontsize=14, fontweight='bold')
plot3.set_ylabel('Cereal Production (in tons)', fontsize=14, fontweight='bold')
plot3.tick_params(axis='both', which='major', labelsize=12)

# Plot 4: Horizontal Bar Graph for Region-wise Cereal Production in 2020
plot4 = plt.subplot(gs[2, :])
bars = plot4.barh(
    data_hbargraph.iloc[:, 0], 
    data_hbargraph.iloc[:, 2], 
    color='skyblue'
)
plot4.set_xlabel('Cereal Production (in tons)', fontsize=14, fontweight='bold')
plot4.set_ylabel('Regions', fontsize=14, fontweight='bold')
plot4.set_title(
    'Region-wise Cereal Production in 2020', 
    fontsize=16, fontweight='bold', pad=20
)
plot4.tick_params(axis='both', which='major', labelsize=12)

# Adding labels to the bars
for bar in bars:
    yval = bar.get_y() + bar.get_height() / 2
    xval = bar.get_width()
    plot4.text(xval, yval, f'{xval:.2f}', va='center')

# Setting up Text block
plot5 = plt.subplot(gs[3, :])
plot5.axis('off')
blockcontent = (
    "- Global cereal production increased by approximately "
    "305.5% from 1960 to 2020.\n"
    "- In 2020, Upper Middle-Income countries produced 42% of the cereal, "
    "High-Income countries 28%, Lower Middle-Income countries 27%, "
    "and Low-Income countries 3%.\n"
    "- Asia's cereal production increased by about 41.3% from 2000 to 2020.\n"
    "- In 2020, High-Income and Lower Middle-Income countries were nearly "
    "equal in cereal production, contributing 28% and 27%, respectively.\n"
    "- Climate change and technological advancements have played a "
    "significant role in shaping cereal production trends over the last "
    "six decades.\n"
    "- The increasing global population has driven the demand for higher "
    "cereal production, influencing agricultural practices and policies "
    "worldwide.\n"
    "- Sustainability and food security challenges are increasingly "
    "prominent, highlighting the need for equitable and efficient cereal "
    "production and distribution systems."
)

plot5.text(
    0, 0.5, blockcontent, 
    ha='left', va='center', 
    fontsize=20, color='black', wrap=True
)

# Add the name and ID in the last row of the grid
plot6 = plt.subplot(gs[4, :])  # This is the new row for name and ID
plot6.axis('off')
plot6.text(
    0.95, 0.5, "Student Name:Nethravathi Shivachar Gurumallesh\n ID:22089836 ", 
    ha="right", fontsize=18, color='black'
)

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
