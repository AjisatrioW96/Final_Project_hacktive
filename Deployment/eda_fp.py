import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(
    page_title = 'Churn customer',
    page_icon="🧊",
    
    initial_sidebar_state='expanded',
        menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
            

    }
)


colors = sns.color_palette('PuBu')
colors_1 = sns.color_palette('PuBu')[4:7]
colors_2 = sns.color_palette('PuBu')[2:7]
colors_3 = sns.color_palette('PuBu')[1:7]
colors_4 = ['#7209B7', '#4895EF', '#560BAD', '#480CA8', '#4361EE' ]
colors_5 = sns.color_palette('crest')




def eda_countplot(x, y, data):
    feat = x
    hue = y
    hue_type = data[hue].dtype.type
    groups = data[feat].dropna().unique()
    data_cleaned = data.dropna(subset=[hue])
    proportions = data_cleaned.groupby(feat)[hue].value_counts(normalize=True).unstack()
    sns.set(style="whitegrid", rc={'figure.figsize': (10, 6)})
    color_palette = sns.color_palette('crest')
    ax = sns.countplot(x=feat, hue=hue, data=data_cleaned, palette=color_palette)
    for c in ax.containers:
        labels = [f'{proportions.loc[g, hue_type(c.get_label())]:.1%}' for g in groups]
        ax.bar_label(c, labels)

    plt.xlabel(x)
    plt.ylabel('Count')
    plt.title(f'Count Plot: {hue} by {x}')
    plt.legend(title=hue)
    ax.legend(title=hue, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=30, ha='right')
    plt.show()
    st.pyplot(plt)

def eda_hisplot(x, y, data):
    plt.figure(figsize=(10, 6))
    ax = sns.histplot(data=data, x=x, hue=y, multiple="stack", palette='crest', alpha=0.7)
    plt.title(f'{x} Distribution with {y}')
    plt.xlabel(x)
    plt.ylabel('Frequency')
    mode_number = data[data[y] == 'Attrited Customer'][x].value_counts().idxmax()
    plt.text(0.7, 0.6, f'Mode {x}: {mode_number:.2f}', transform=plt.gca().transAxes)
    st.pyplot(plt)

def bar_plot_1 (x , y ,  data) :
    yy2 = data.groupby(x)[y].value_counts(normalize=True).unstack()
    palette = 'crest'
    colors = sns.color_palette(palette, n_colors=len(yy2.columns))
    ax = yy2.plot(kind='bar', stacked=True, color=colors)
    ax.set_xlabel(x)
    ax.set_ylabel('Proportion')
    ax.set_title(f'Proportion of Attrition Flag for Each {x}')
    ax.legend(title='Attrition Flag', bbox_to_anchor=(1.05, 1), loc='upper left')
    for p in ax.patches:
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy()
        ax.annotate(f'{height:.2%}', (x + width / 2, y + height), ha='center', fontsize=10, weight='bold')
    plt.tight_layout()
    st.pyplot(plt)




def run(): 

    #Membuat Title
    st.title('Churn Credit Card Customer')

    #Membuat sub header
    st.subheader('Exploratory Data Credit Card Customer')

    image = Image.open('credit_card_1.jpg')
    st.image(image, caption = 'credit card')


    c1, c2 = st.columns((5, 5))
    with c1: 
        st.write("Dengan meningkatnya persaingan banking, memahami perilaku pelanggan yang berpotensi berpindah atau churn menjadi semakin penting. Churn pelanggan terjadi ketika pelanggan memutuskan untuk tidak lagi menggunakan layanan kartu kredit dari suatu bank. Fenomena ini dapat memiliki dampak signifikan pada lini bisnis bank termasuk pendapatan dan reputasi.")
    with c2:
        st.write("Namun, mengidentifikasi pelanggan yang berpotensi churn bukanlah tugas yang mudah. Dalam industri yang kompetitif, bank perlu mengenali tanda-tanda perilaku pelanggan yang menunjukkan kemungkinan churn. Ini termasuk pola penggunaan kartu yang berubah, penurunan frekuensi transaksi, dan peningkatan keluhan atau ketidakpuasan pelanggan.")

    st.write("Oleh karena itu, penting untuk melakukan analisis mendalam terhadap data pelanggan dan menerapkan model prediktif untuk mengidentifikasi pelanggan yang berisiko churn. Dengan pemahaman yang lebih baik tentang faktor-faktor yang mempengaruhi churn, perusahaan kartu kredit dapat mengambil tindakan pencegahan yang tepat, seperti mengembangkan strategi retensi yang efektif")

    st.markdown("##")
    st.markdown("##")   
        

    st.write("Dibawah ini merupakan data dari dataframe customer ")

    st.write('<h3 style="text-align: center;">Dataframe of Customer </h3>', unsafe_allow_html=True)

    data = pd.read_csv('credit_card_churn_clean.csv')
    st.dataframe(data)


    st.write('<h3 style="text-align: center;"> Exploratory Data of Customer </h3>', unsafe_allow_html= True )

    st.markdown("##")

    image = Image.open('churn_1.png')
    st.image(image, caption = 'Churn')
    st.write("Di halaman ini, kita dapat menjelajahi grafik berdasarkan konten dataset. Insight yang diperoleh di bawah ini berasal dari sudut pandang penulis")
    st.markdown("##")


    column_1 = ["Gender" ,'Education_Level', 'Marital_Status','Income_Category','Card_Category', 'Total_Relationship_Count']

    selected_plot = st.selectbox("Select plot to Show", ["Gender"  ,'Education_Level', 'Marital_Status','Income_Category','Card_Category', 'Total_Relationship_Count'])
    y = 'Attrition_Flag'
    if selected_plot == 'Gender':
        eda_countplot(selected_plot, y, data=data)
        st.write("Berdasarkan plot target terhadap gendere pelanggan, dapat dilihat baik secara total ataupun secara persentase pelanggan dengan gender perempuan cenderung untuk meninggalkan layanan kartu kredit.")
    elif selected_plot == 'Education_Level':
        eda_countplot(selected_plot, y, data=data)
        st.write("Berdasarkan plot target terhadap tingkat edukasi pelanggan dapat terlihat bahwa jumlah pelanggan dengan tingkat pendidikan graduate memiliki jumlah pelanggan churn yang paling banyak. Namun jika kita melihat dari persentase terhadap masing masing kategorinya, pelanggan dengan tingkat pendidikan doctorate memiliki churn yang paling besar.")
    elif selected_plot == 'Marital_Status':
        eda_countplot(selected_plot, y, data=data)
        st.write("Berdasarkan plot target terhadap status perkawinann pelanggan dapat terlihat jumlah pelanggan dengan status perkawinan sudah menikah memiliki jumlah pelanggan churn yang paling tinggi. Namun jika melihat secara persentase pelanggan yang lebih memiliki menyembunyikan status hubungannya memiliki persentase churn lebih tinggi.")
    elif selected_plot == 'Income_Category':
        eda_countplot(selected_plot, y, data=data)
        st.write("Berdasarkan plot target terhadap tingkat pendapatan pelanggan dapat terlihat pelanggan dengan pendapatan dibawah $40K mempuyai jumlah pelanggan churn yang lebih banyak, namun secara persentase seorang yang memiliki tingkat pendapatan >$120k memiliki % churn yang lebih tinggi")
    elif selected_plot == 'Card_Category':
        eda_countplot(selected_plot, y, data=data)
        st.write("Berdasarkan plot target terhadap tingkat kartu yang dimiliki pelanggan dapat terlihat pelanggan yang memiliki kartu kredit blue memiliki jumlah pelanggan churn yang paling tinggi, namun secara persentase seorang yang memiliki kartu platinum memiliki % churn yang lebih tinggi")
    elif selected_plot == 'Total_Relationship_Count':
        eda_countplot(selected_plot, y, data=data)
        st.write(" Berdasarkan plot target  terhadap pelanggan berdasarkan produk yang telah dipegang oleh pelanggan, dapat dilihat bahwa jumlah pelanggan yang memiliki 3 produk memiliki total pelanggan yang churn paling banyak dalam jumlah. Namun, jika kita melihat dari persentase terhadap total pelanggan pada setiap kategori jumlah produk, ternyata pelanggan yang memiliki jumlah produk antara 5 hingga 6 memiliki persentase churn yang paling tinggi.")

    st.markdown("##")


    column_2 = ['Dependent_count','Total_Relationship_Count', 'Months_Inactive_12_mon' , 'Contacts_Count_12_mon']
    y = 'Attrition_Flag'
    selected_plot = st.selectbox("Select barplot to Show", column_2)
    if selected_plot == column_2[0]: 
        bar_plot_1(selected_plot, y, data=data)
        st.write(" Dari plot target terhadap jumlah dependent pelanggan dapat terlihat , pelanggan dengan jumlah dependent sebanyak 3 orang memiliki tingkat % churn yang lebih tinggi dibanding yang lainnya") 
    elif selected_plot == column_2[1]:  
        bar_plot_1(selected_plot, y, data=data) 
        st.write("Dari plot target terhadap total jumlah produk yang dimiliki pelanggan dapat terlihat, pelanggan yang memiliki total produk yang lebih sedikit memiliki % churn yang lebih tinggi dibandingkan yang lainnya.") 
    elif selected_plot == column_2[2]: 
        bar_plot_1(selected_plot, y, data=data) 
        st.write("Dari plot target terhadap jumlah bulan yang tidak aktif setelah 12 bulan, pelanggan yang sudah tidak aktif lebih dari 4 bulan memiliki tingkat churn yang lebih tinggi") 
    elif selected_plot == column_2[3]:
        bar_plot_1(selected_plot, y, data=data) 
        st.write("Dari plot target terhadap jumlah pelanggan yang dihubungi oleh bank, pelanggan yang sudah dikontak lebih dari 5 kali atau dalam hal ini jumlahnya 6 kali memiliki tingkat persentase churn 100% ") 

    
    st.markdown("##")

    exclude = ['CLIENTNUM', 'Attrition_Flag']
    column_3 = [col for col in data.columns if col not in column_1 and col not in exclude and col not in column_2]
    selected_plot = st.selectbox("Select hisplot to Show", column_3)
    if selected_plot == column_3[0]: 
        eda_hisplot(selected_plot, y, data=data)
        st.write("Berdasrkan plot histogram, customer dengan umur 48 tahun memiliki tingkat churn yang lebih tinggi") 
    elif selected_plot == column_3[1]:
        eda_hisplot(selected_plot, y, data=data) 
        st.write("Berdasarkan Months on booknya , customer yang sudah bersama dengan bank selama 36 bulan memiliki tingkat churn yang lebih tinggi")
    elif selected_plot == column_3[2]: 
        eda_hisplot(selected_plot, y, data=data) 
        st.write("Berdarkan credit card limitnya , customer dengan credit limit yang rendah memiliki tingkat churn yang lebih tinggi")
    elif selected_plot == column_3[3]: 
        eda_hisplot(selected_plot, y, data=data) 
        st.write("Berdasarkan total revolving balancenya, customer dengan total revolving yang rendah memiliki tingkat churn yang lebih tinggi")
    elif selected_plot == column_3[4]: 
        eda_hisplot(selected_plot, y, data=data) 
        st.write("Berdasarkan rata rata open to buy , customer dengan rata rata yang rendah memiliki tingkat churn yang lebih tinggi")
    elif selected_plot == column_3[5]: 
        eda_hisplot(selected_plot, y, data=data) 
        st.write("Berdasarkan rate total balance yang berubah dari Q4 ke Q1 , customer yang memiliki rate 0.6 memiliki tingkat churn yang lebih tinggi")
    elif selected_plot == column_3[6]:
        eda_hisplot(selected_plot, y, data=data) 
        st.write("Berdasarkan total transaksinya , customer yang melakukan total transaksi sebesar 2216 memiliki tingkat churn yang lebih tinggi")
    elif selected_plot == column_3[7]: 
        eda_hisplot(selected_plot, y, data=data) 
        st.write("Berdasarkan jumlah total transaksi selama 12 bulan, pelanggan dengan total transaksi sebesar 43 memiliki tingkat churn yang lebih tinggi")
    elif selected_plot == column_3[8]: 
        eda_hisplot(selected_plot, y, data=data) 
        st.write("Berdasarkan jumlah total change dari Q4 ke Q1 , customer yang memiliki nilia 0.5 memiliki tingkat churn yang lebih tinggi")
    elif selected_plot == column_3[9]: 
        eda_hisplot(selected_plot, y, data=data) 
        st.write("Berdasarkan avg utilization ratio, pelanggan yang memiliki ratio 0 memiliki tingkat churn yang lebih tinggi diantara yang lainnya")

    st.markdown("##")
    st.write("Selain dari plot yang ditampilkan diatas, diperoleh analisis korelasi dari feature terhadap target yaitu customer yang churn atau tidak churn")
    st.markdown("##")


    fs_num = data[column_2]
    plt.figure(figsize=(10, 6))
    corr_matrix = fs_num.corr()
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    sns.heatmap(corr_matrix, annot=True, mask=mask, cmap ='crest' )
    plt.title('Correlation Test')
    plt.show()
    st.pyplot(plt)
    st.write("Dari hasil test correlation dapat dilihat beberapa insight, feature Avg_Open_To_Buy mempunyai korelasi yang kuat terhadap Credit_limit. Ini artinya sebenarnya nilai dari avg_open_to_buy dengan nilai credit_limit mempunyai relevansi yang kuat. Dari hasil lainnya ternyata Avg_Open_To_Buy mempunyai korelasi yang rendah terhadap target. ")
    st.markdown("##")


if __name__ == '__main__':
    run()