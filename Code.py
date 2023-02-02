import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# Create a dataset
df = pd.read_csv (r'SNP3.csv')
print (df)
# Create a grid : initialize it
g = sns.FacetGrid(df, col='Chr', hue='Chr', col_wrap=10, )

# Add the line over the area with the plot function
g = g.map(plt.plot, 'Position', 'NBS')
# Fill the area with fill_between
g = g.map(plt.fill_between, 'Position', 'NBS', alpha=0.2).set_titles("{col_name} Chr")
# Control the title of each facet
g = g.set_titles("{col_name}")
# Add a title for the whole plot
plt.subplots_adjust(top=0.8)
g = g.fig.suptitle('Density of NBS genes across the A and C genomes')
plt.show()

