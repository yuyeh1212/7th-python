import pandas as pd

name = ['Tony', 'Amy', 'Joe']
followers = ['77', '45', '12']
serie = pd.Series(followers, index=name)

print(serie)
