import plotly.express as px
import numpy as np
import pandas as pd

x = np.linspace(0, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

df = pd.DataFrame({
    'x': x,
    'Sine': y_sin,
    'Cosine': y_cos
})

print(df)
fig = px.line(df, x='x', y=['Sine', 'Cosine'], labels={"value": "f(x)", "X": "x"})
fig.show()
