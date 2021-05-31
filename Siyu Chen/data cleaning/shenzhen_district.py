import geopandas
import matplotlib.pyplot as plt

district1 = geopandas.read_file('../material/440303.json')
district2 = geopandas.read_file('../material/440304.json')
district3 = geopandas.read_file('../material/440305.json')
district4 = geopandas.read_file('../material/440306.json')
district5 = geopandas.read_file('../material/440307.json')
district6 = geopandas.read_file('../material/440308.json')

# generate shenzhen_district figure
fig,ax = plt.subplots()
district1.plot(ax=ax,color="#FDECD2",alpha=1)
district2.plot(ax=ax,color="#FADCE8",alpha=0.8)
district3.plot(ax=ax,color="#DFE2F3",alpha=0.9)
district4.plot(ax=ax,color="#E0ECDF",alpha=0.7)
district5.plot(ax=ax,color="#7DB9DE",alpha=0.6)
district6.plot(ax=ax,color="#FB9966",alpha=0.7)
plt.savefig('shenzhen_district.png')
plt.show()