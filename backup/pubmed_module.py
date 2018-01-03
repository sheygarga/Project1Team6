import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

surname_set=set(['Zhao','Qian','Sun','Li','Zhou','Wu','Zheng','Wang','Feng',
                 'Chen','Chu','Wei','Jiang','Shen','Han','Yang','Zhu','Qin',
                 'You','Xu','He','Lu','Shi','Zhang','Kong','Cao','Yan','Hua',
                 'Jin','Wei','Tao','Qi','Xie','Zou','Yu','Bai','Shui','Dou',
                 'Yun','Su','Pan','Ge','Xi','Fan','Peng','Lang','Lu','Chang',
                 'Ma','Miao','Feng','Fang','Ren','Yuan','Liu','Bao','Tang',
                 'Fei','Lian','Cen','Xue','Lei','Ni','Teng','Yin','Luo','Bi',
                 'Hao','Wu','An','Chang','Yue','Yu','Fu','Pi','Bian','Qi','Kang',
                 'Bu','Gu','Meng','Ping','Huang','Mu','Xiao','Yao','Shao','Zhan',
                 'Wang','Mao','Di','Mi','Bei','Ming','Zang','Ji','Cheng','Dai',
                 'Tan','Song','Pang','Xiong','Shu','Qu','Xiang','Dong','Liang',
                 'Du','Ruan','Lan','Min','Qiang','Jia','Lu','Jiang','Tong',
                 'Guo','Mei','Sheng','Lin','Diao','Zhong','Xu','Qiu','Gao',
                 'Xia','Cai','Tian','Fan','Hu','Ling','Huo','Wan','Zhi','Ke',
                 'Zan','Guan','Mo','Jing','Gan','Ying','Zong','Ding','Xuan',
                 'Ben','Deng','Shan','Hang','Hong','Bao','Zuo','Cui','Niu',
                 'Gong','Xing','Pei','Rong','Weng','Xun','Yang','Hui','Zhen',
                 'Qu','Jia','Rui','Yi','Bing','Duan','Jiao','Ba','Mu','Kui',
                 'Shan','Che','Hou','Quan','Ban','Ning','Zu','Fu','Jing','Zhan',
                 'Shu','Long','Ye','Si','Bo','Huai','Bai','Pu','Tai','Cong',
                 'E','Suo','Xian','Lai','Zhuo','Tu','Chi','Qiao','Nai','Cang',
                 'Shuang','Wen','Dang','Zhai','Lao','Pang','Du','Ran','Zai',
                 'Yong','Qu','Sang','Shou','Bian','Hu','Yan','Jia','Shang',
                 'Nong','Wen','Bie','Zhuang','Chai','Chong','Lian','Ru','Xi',
                 'Huan','Ai','Xiang','Yi','Liao','Heng','Geng','Man','Kuang',
                 'Kou','Guang','Que', 'Dugu', 'Ouyang', 'Dongfang','Ximen',
                 'Zeng','Sui','Dai', 'Gou','Upur','Chinese'])

top_j=['Cell','Nature','Science','Nat Methods','Nat Cell Biol','Neuron',
       'Nat Immunol','Nat Genet','Nat Biotechnol', 'Nat Med','Nat Nanotechnol',
       'N Engl J Med','Lancet','Nat Mater','Cancer Cell','Cell Stem Cell',
       'Immunity']

black_list=['of','in','and','the','a','for','with','to','on','by',
            'from','an','as','using','study','after','analysis',
            'is','effect','effects','between','risk',
            'among','care','during','associated','at',
            '-','or','role','case','use','factors','impact','based','assesment',
            'association','type','via','are','its','through','report','their',
            'results','two','2','research','into','levels','can',
            'multiple','single','time','be','does','we','do',
            'without','b','under','towards','group','cases','dose','left','over',
            't','level','three','but','it','about','i','ii','one','right','c',
            'de','work','our','not']

def is_chinese(df,col='PI'):
    #check whether author in col is Chinese
    check=df[col].str.split('\s').str[0].isin(surname_set)
    col_name=col+'_is_Chinese'
    df[col_name]=check
    return df

def all_chinese(df,col='Description'):
    #check whether all authors are Chinese
    check=[]
    for i in df[col]:
        t=i.split(',')
        t=[i.strip().split() for i in t]
        t=[i[0] for i in t if i]
        t=[(name in surname_set) for name in t]
        check.append(all(t))
    df['All_Chinese']=check
    return df

'''
# debug of all_chinese function, find the error row

for i in df['Description']:
    try:
        t=i.split(',')
        t=[i.strip().split()[0] for i in t]
        t=[(name in surname_set) for name in t]
    except Exception:
        print(row)
    row+=1
'''

def get_topj(df,col='Journal'):
    df=df.loc[df[col].isin(top_j),:]
    return df

def count_paper(df, col='Journal'):
    #count papers in individual journal, return new df with journal and count
    df['Count']=df[col].copy()
    df_new=df.groupby('Journal').agg({'Count':'count'}).sort_values('Count',
                                                        ascending=False)
    df_new=df_new.reset_index().loc[:,[col,'Count']]
    return df_new

def norm_paper(df_total,df,col='Journal'):
    #count papers in individual journal, return new df with journal and
    #normalized count (percentage)
    df_total['Total_Count']=df_total[col].copy()
    df_norm=df_total.groupby(col).agg({'Total_Count':'count'}).\
             reset_index()
    df['Count']=df[col].copy()
    df=df.groupby(col).agg({'Count':'count'}).reset_index()
    df_merge=df.merge(df_norm,on=col,how='inner')
    df_merge['Ratio']=round(df_merge['Count']/df_merge['Total_Count'],2)
    df_merge=df_merge.sort_values(by='Ratio',ascending=False)
    df_merge=df_merge.loc[:,[col,'Count','Total_Count','Ratio']]
    return df_merge

def count_keyword(df,keyword,col='Title'):
    #check whether any keyword (list of lower case words) in col
    #return counts 
    for i in keyword:
        df[i]=df[col].str.lower().str.contains(i)
    df_k=df.loc[:,keyword]
    df['keyword']=df_k.sum(axis=1)
    df=df.loc[df['keyword']>0,:]
    return df.shape[0]

def count_keywords(df,keywords,labels,col='Title'):
    #check a list of keywords_list, return df with keywords and counts
    #labels are list of keywords_list label
    #keywords and label should be in same order
    key_count=[]
    for keyword in keywords:
        count=count_keyword(df,keyword)
        key_count.append(count)
    df_new=pd.DataFrame({'Keyword':labels,'Count':key_count})
    df_new=df_new.sort_values('Count',ascending=False)
    df_new=df_new.reset_index().loc[:,['Keyword','Count']]
    return df_new

def sort_keyword(df,col='Title',blacklist=True):
    #sort most frequent keyword in all titles, with blacklist words removed
    words=[]
    for title in df[col]:
        if isinstance(title,str):
            title=[i.strip('[].:').lower() for i in title.split()]
            title_s=set(title)
            words.extend(title_s)
    word_uniq=set(words)
    keyword=[]
    count=[]
    for word in word_uniq:
        keyword.append(word)
        count.append(words.count(word))
    df_new=pd.DataFrame({'Keyword':keyword,'Count':count}).\
            sort_values('Count', ascending=False)
    if blacklist:
        df_new=df_new.loc[df_new['Keyword'].isin(black_list)==False,:]
    df_new=df_new.reset_index().loc[:,['Keyword','Count']]
    return df_new




