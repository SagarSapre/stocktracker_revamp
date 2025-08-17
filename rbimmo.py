import pandas as pd

url="https://www.rbi.org.in/Scripts/BS_ViewMMO.aspx"


dfs=pd.read_html(url, header=0,encoding='utf-8')

#print(len(df))

# print(df[0].head())
# print(df[1].head())
# print(df[2].head())
# print(df[3].head())
# print(df[4].head())
# print(df[5].head())
dfs = [t.set_axis(range(t.shape[1]), axis=1) for t in dfs]
#pd.concat([df[0], df[1], df[2], df[3], df[4], df[5]], ignore_index=True).to_csv("rbi_mmo_data.csv", index=False)
#pd.concat([df[0], df[1], df[2], df[3], df[4], df[5]], ignore_index=True,sort=False).to_csv("rbi_mmo_data2.csv", index=False)
#pd.concat([pd.DataFrame(df[0].to_numpy()),pd.DataFrame(df[1].to_numpy()),pd.DataFrame(df[2].to_numpy()),pd.DataFrame(df[3].to_numpy()),pd.DataFrame(df[4].to_numpy()),pd.DataFrame(df[5].to_numpy())],ignore_index=True)

result = pd.concat(dfs, ignore_index=True)
print(result)
result.to_csv("rbi_mmo_data2.csv", index=False)
#df.to_csv("rbi_mmo_data.csv", index=False)
