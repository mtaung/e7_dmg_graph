import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np 
from char import Character

# Stats
bonus_vector = np.round(np.linspace(1, 4, 300), 2)

ken = Character('Ken', 966, 7323, 657, 150, 102)
ken_atk = bonus_vector * ken.atk + 500
ken_hp = bonus_vector * ken.hp + 2700

# Skills
ken_s1 = (ken_atk*1+ken_hp*0.10)*1.871
ken_s2 = (ken_atk*1.2+ken_hp*0.10)*1.871
ken_s3 = (ken_atk*1.5+ken_hp*0.30)*1.6839

# Create vectors for graphing space
y_s1 = ken_s1
y_s2 = ken_s2
y_s3 = ken_s3

sns.lineplot(x=bonus_vector*100, y=y_s1)
plt.show()