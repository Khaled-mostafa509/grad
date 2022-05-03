import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import psycopg2


df_ahmed = pd.read_excel(r'E:\khaled\db\recommendation_system\ahmed.xlsx')
df_yahia = pd.read_excel(r'E:\khaled\db\recommendation_system\yahia.xlsx')
df_bola = pd.read_excel(r'E:\khaled\db\recommendation_system\bola.xlsx')
df_total = pd.concat([df_ahmed, df_yahia, df_bola])
google_drive_data = pd.read_excel(r'E:\khaled\db\recommendation_system\google_drive_data.xlsx')
important_columns = df_total[['Category', 'Machine Name', 'Description', 'Production country']]
all_supplies = pd.concat([google_drive_data, important_columns])
all_supplies.columns[all_supplies.isna().any()]
all_supplies['Production country'].isna().sum()
all_supplies.dropna(inplace=True)
all_supplies.columns[all_supplies.isna().any()]
all_supplies.duplicated().sum()
all_supplies['Category'] = all_supplies['Category'].apply(lambda x:x.split()) 
all_supplies['Machine Name'] = all_supplies['Machine Name'].apply(lambda x:x.split())
all_supplies['Description'] = all_supplies['Description'].apply(lambda x:x.split())
all_supplies['combination_column'] = all_supplies.Description + all_supplies.Category + all_supplies['Machine Name']
final_df = all_supplies[['Machine Name', 'combination_column']]
final_df['Machine Name'] = final_df['Machine Name'].apply(lambda x:' '.join(x))
final_df['combination_column'] = final_df['combination_column'].apply(lambda x:' '.join(x))
final_df = final_df.reset_index().drop('index', axis=1)
final_df['combination_column'][0]
transformer = CountVectorizer(max_features=5000,stop_words='english')
vector = transformer.fit_transform(final_df['combination_column'])
vectors = vector.toarray()
similarity = cosine_similarity(vectors, vectors)

def recommend_machine(machine):
    machine_index = final_df[final_df['Machine Name'] == machine].index[0]
    distances = similarity[machine_index]
    machines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:10]
    reco_list = []
    for i in machines_list:
        # print(final_df.iloc[i[0]]['Machine Name'])
        reco_list.append(final_df.iloc[i[0]]['Machine Name'])
    return reco_list
tst = recommend_machine('CPAP Non-Invasive Infant Breathing Bubble CPAP Nlf-200d Hospital Equipment')
