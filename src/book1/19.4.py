import seaborn as sns
import matplotlib.pyplot as plt

iris_df = sns.load_dataset("iris")
fig, ax = plt.subplots(figsize=(5, 9))
sns.heatmap(iris_df.iloc[:, :4], cmap='RdYlBu_r',vmax=8, vmin=0,cbar_kws={'orientation': 'vertical'}, annot=False, fmt=".2f", ax=ax)
fig.show()
