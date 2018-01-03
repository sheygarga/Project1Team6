import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pubmed_module as pm

def clean_df(df):
    #remove headers and duplicates, remove rows without Description
    df=df.loc[df['Title']!='Title',:]
    df=df.loc[df['Description'].notnull(),:]
    df['Title']=df['Title'].str.strip('[].?')
    df=df.loc[:,['Title','Description','Details']]
    df=df.drop_duplicates()
    return df

def add_journal(df):
    #add Journal column
    df['Journal']=df['Details'].str.split('.').str[0].str.strip()
    df['Journal']=df['Journal'].str.split(';').str[0].str.strip()
    return df

def add_author(df):
    #add PI and First_A column, and remove 'et al'
    authors_series=df['Description'].str.strip('.').str.split(',') 
    pi=[]
    first=[]
    for author_list in authors_series:
        authors=[i.strip() for i in author_list]
        pi.append(authors[-1])
        first.append(authors[0])
    df['PI']=pi
    df['First_A']=first
    df=df.loc[df['PI']!='et al',:]
    return df


#clean the raw csv (do it only once and then comment it out)
input_file='2017.csv'
output_file='2017_clean.csv'
sample='2017_sample.csv'

df=pd.read_csv(input_file,index_col=False)
df=clean_df(df)
df=add_journal(df)
df=add_author(df)
df=df.loc[:,['Title','Description','Journal','PI','First_A']]
df_sample=df.head(1000)

df.to_csv(output_file)
df_sample.to_csv(sample)


#read data
input_file='2017_clean.csv'
df=pd.read_csv(input_file,index_col=0)


#count total papers per journal
df_c=pm.count_paper(df)

total_paper=df_c['Count'].sum()
total_j=df_c.shape[0]
avg=round(total_paper/total_j, 2)
median_j=df_c['Count'].median()

fig,ax=plt.subplots(figsize=(8,10))
ax.boxplot(df_c['Count'],'.')

ax.set_title('Papers per Journal')
ax.set_xlabel('year')
ax.set_ylabel('Number of Papers')
ax.set_xticklabels(['2017'])
str_median='Median'+'='+str(int(median_j))
ax.annotate(str_median,xy=(1.1,median_j))
str0=df_c.loc[0,'Journal']+': '+str(df_c.loc[0,'Count'])
ax.annotate(str0,xy=(1.1,df_c.loc[0,'Count']))
str1=df_c.loc[1,'Journal']+': '+str(df_c.loc[1,'Count'])
ax.annotate(str1,xy=(1.1,df_c.loc[1,'Count']))
str2=df_c.loc[2,'Journal']+': '+str(df_c.loc[2,'Count'])
ax.annotate(str2,xy=(1.1,df_c.loc[2,'Count']))

top=df_c.loc[0,'Count']
space=(df_c.loc[0,'Count'])/35
ax.annotate('Total Papers:'+' '+str(total_paper),xy=(0.52,top))
ax.annotate('Total Journals:'+' '+str(total_j),xy=(0.52,top-space))
ax.annotate('Average per Journal:'+' '+str(avg),xy=(0.52,top-space-space))
plt.savefig('paper_per_j_total.png')
plt.clf()


# check papers related to different tissues
heart=['cardiac','heart']
bone=['bone','skeleton','cartilage','chondrogenesis']
liver=['liver','hepatocyte','cirrhosis','hepatitis']
lung=['lung']
colon=['colon','colorectal']
blood=['blood', 'hemoglobin','aorta','artery']
brain=['brain','nervous']
stomach=['stomach']
intestine=['intestine']
muscle=['muscle', 'muscular']
spleen=['spleen']
pancreas=['pancreas']
rectum=['rectum']
kidney=['kidney']

keywords=[heart,bone,liver,lung,colon,blood,brain,stomach,intestine,muscle,
         spleen,pancreas,rectum,kidney]
labels=['heart','bone','liver','lung','colon','blood','brain','stomach',
       'intestine','muscle','spleen','pancreas','rectum','kidney']

df_k=pm.count_keywords(df,keywords,labels)

fig,ax=plt.subplots(figsize=(10,10))
ax.bar(np.arange(len(labels)),df_k['Count'])
ax.set_title('Paper Number of Different Tissues')
ax.set_xticks(np.arange(0,len(labels),1))
ax.set_xticklabels(labels, rotation=45)
ax.set_ylabel('Paper Number')
plt.savefig('Tissue_Rank.png')
plt.clf()

df_top=pm.get_topj(df)
df_k=pm.count_keywords(df_top,keywords,labels)

fig,ax=plt.subplots(figsize=(10,10))
ax.bar(np.arange(len(labels)),df_k['Count'])
ax.set_title('Paper Number of Different Tissues in Top Journals')
ax.set_xticks(np.arange(0,len(labels),1))
ax.set_xticklabels(labels, rotation=45)
ax.set_ylabel('Paper Number')
plt.savefig('Tissue_Rank_Top.png')
plt.clf()


# check papers related to different diseases
cancer=['cancer','tumor']
diabetes=['diabetes','diabete']
alzheimer=['alzheimer']
arthristis=['arthritis']
asthma=['asthma']
autism=['autism']
allergy=['allergy']
hiv=['hiv','aids']

keywords=[cancer,diabetes,alzheimer,arthristis,asthma,autism,allergy,hiv]
labels=['cancer','diabetes','alzheimer','arthristis','asthma','autism',
       'allergy','hiv']

df_k=pm.count_keywords(df,keywords,labels)

fig,ax=plt.subplots(figsize=(10,10))
ax.bar(np.arange(len(labels)),df_k['Count'])
ax.set_title('Paper Number of Different Diseases')
ax.set_xticks(np.arange(0,len(labels),1))
ax.set_xticklabels(labels, rotation=45)
ax.set_ylabel('Paper Number')
plt.savefig('Disease_Rank.png')
plt.clf()

df_top=pm.get_topj(df)
df_k=pm.count_keywords(df_top,keywords,labels)

fig,ax=plt.subplots(figsize=(10,10))
ax.bar(np.arange(len(labels)),df_k['Count'])
ax.set_title('Paper Number of Different Diseases')
ax.set_xticks(np.arange(0,len(labels),1))
ax.set_xticklabels(labels, rotation=45)
ax.set_ylabel('Paper Number')
plt.savefig('Disease_Rank_Top.png')
plt.clf()


# chinese pi pub ratio in all journals
df_cn=pm.is_chinese(df)

total=df_cn.shape[0]
chinese_count=df_cn['PI_is_Chinese'].sum()
other=total-chinese_count
size=[chinese_count,other]
label=['Chinese','Not Chinese']

fig,ax=plt.subplots(figsize=(10,10))
ax.pie(size,labels=label,autopct='%1.1f%%', startangle=90,explode=(0.1,0))
ax.set_title('Chinese PI Ratio in All Journals')
plt.savefig('Chinese_PI_Ratio.png')
plt.clf()


# chinese pi pub ratio in top journals
df_cn_top=pm.get_topj(df_cn)

total=df_cn_top.shape[0]
chinese_count=df_cn_top['PI_is_Chinese'].sum()
other=total-chinese_count
size=[chinese_count,other]
label=['Chinese','Not Chinese']

fig,ax=plt.subplots(figsize=(10,10))
ax.pie(size,labels=label,autopct='%1.1f%%', startangle=90,explode=(0.1,0))
ax.set_title('Chinese PI Ratio in Top Journals')
plt.savefig('Chinese_PI_Ratio_Top.png')
plt.clf()

# chinese pi publications in journals
df_cn=pm.is_chinese(df)
df_cn=df_cn.loc[df_cn['PI_is_Chinese'],:]

df_cn_count=pm.count_paper(df_cn)

total_paper=df_cn_count['Count'].sum()
total_j=df_cn_count.shape[0]
avg=round(total_paper/total_j, 2)
median_j=df_cn_count['Count'].median()

fig,ax=plt.subplots(figsize=(8,10))
ax.boxplot(df_cn_count['Count'],'.')

ax.set_title('Publication Number in Journals')
ax.set_xlabel('year')
ax.set_ylabel('Number of Publications')
ax.set_xticklabels(['2017'])
str_median='Median'+'='+str(int(median_j))
ax.annotate(str_median,xy=(1.1,median_j))
str0=df_cn_count.loc[0,'Journal']+': '+str(df_cn_count.loc[0,'Count'])
ax.annotate(str0,xy=(1.1,df_cn_count.loc[0,'Count']))
str1=df_cn_count.loc[1,'Journal']+': '+str(df_cn_count.loc[1,'Count'])
ax.annotate(str1,xy=(1.1,df_cn_count.loc[1,'Count']))
str2=df_cn_count.loc[2,'Journal']+': '+str(df_cn_count.loc[2,'Count'])
ax.annotate(str2,xy=(1.1,df_cn_count.loc[2,'Count']))

top=df_cn_count.loc[0,'Count']
space=(df_cn_count.loc[0,'Count'])/35
ax.annotate('Total Papers:'+' '+str(total_paper),xy=(0.52,top))
ax.annotate('Total Journals:'+' '+str(total_j),xy=(0.52,top-space))
ax.annotate('Average per Journal:'+' '+str(avg),xy=(0.52,top-space-space))
plt.savefig('Chinese_paper_per_j_total.png')
plt.clf()


# chinese pi normalized journal rank
df_cn=pm.is_chinese(df)
df_cn=df_cn.loc[df_cn['PI_is_Chinese'],:]

df_norm=pm.norm_paper(df,df_cn)

df_norm=df_norm.loc[df_norm['Total_Count']>30,:]
df_norm=df_norm.loc[df_norm['Ratio']<0.85,:]
df_n=df_norm.head(10).sort_values('Ratio')

label=df_n['Journal']
y=np.arange(0,10,1)
x=df_n['Ratio']

fig,ax=plt.subplots(figsize=(20,10))
ax.barh(y,x,align='center',color='blue')
ax.set_title('Normalized Publication (Ratio<85%)')
ax.set_xticks(np.arange(0,1.1,0.1))
ax.set_xticklabels(['0%','10%','20%','30%','40%','50%','60%','70%','80%',
                        '90%','100%'])
ax.set_yticks(y)
ax.set_yticklabels(label)
plt.margins(x=0.1, y=0.1)
plt.savefig('Norm_Chinese_Pub.png')
plt.clf()


#keyword rank
df_wordrank=pm.sort_keyword(df)
df_n=df_wordrank.head(30).sort_values('Count')

label=df_n['Keyword']
y=np.arange(0,30,1)
x=df_n['Count']

fig,ax=plt.subplots(figsize=(20,10))
ax.barh(y,x,align='center',color='blue')
ax.set_title('Word Frequency in Publication Titles')
ax.set_yticks(y)
ax.set_yticklabels(label)
plt.margins(x=0.1, y=0.1)
plt.savefig('Word_Fre.png')
plt.clf()



