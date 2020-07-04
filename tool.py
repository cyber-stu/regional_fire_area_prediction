
import sys
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["figure.figsize"] = 9,5
plt.figure(figsize=(14,8))
plt.style.use('ggplot')
def plot_kde(df,target,):
    #核密度分布
    ax = sns.kdeplot(df[target],shade=True,color='g')
    plt.xticks([i for i in range(0,1200,50)])
    plt.savefig('../photo/'+sys._getframe().f_code.co_name)
    plt.show()
def plot_data_by_categorical(df,dfa,cat_columns):
    # analyzing categorical columns
    for i,col in enumerate(cat_columns,1):
        plt.subplot(2,2,i)
        sns.countplot(data=dfa,x=col)
        plt.subplot(2,2,i+2)
        df[col].value_counts(normalize=True).plot.bar()
        plt.ylabel('% distribution per category')
        plt.xlabel(col)
    plt.tight_layout()
    plt.savefig('../photo/'+sys._getframe().f_code.co_name)
    plt.show()
# for col in cat_columns:
#     plt.subplot(1,2,i)
#     cross = pd.crosstab(columns=df[col],index=df['damage_category'],normalize=1)
#     sns.heatmap(cross,cmap='YlOrRd',annot=True,cbar=tag)
#     #plt.xlabel('% distribution per category')
#     plt.title("Forestfire damage in each {}".format(col))
#     tag=True
#     i=2
# plt.tight_layout()
# plt.savefig('../photo/heatmap')
# plt.show()