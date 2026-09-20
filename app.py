import psutil
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.ion()

fig,ax=plt.subplots(nrows=3,ncols=2,figsize=(8,6))
b =8
cpuu = [20,2,29,34,20,2,29,34]
cpu_per =[20,2,29,34,20,2,29,34]
ram_used=[20,2,29,34,20,2,29,34]
ram_total =[20,2,29,34,20,2,29,34]
disk_per =[20,2,29,34,20,2,29,34]
h = [1,2,3,4,5,6,7,8]
while True:
    
    
    
        
      

    for a in ax.flat:
        a.clear()
    cpuu.append(psutil.cpu_percent(interval = 1))
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("C:")
            
                
    cpu_per.append(ram.percent)
    ram_used.append(ram.used /(1024**3))
    ram_total.append(ram.total / (1024**3))
    disk_per.append(disk.percent)
    
    h.append(h[-1] + 1)
    data ={"cpu":cpuu,"cpu_percent":cpu_per,"ram_used":ram_used,"ram_total":ram_total,"disk_percent":disk_per,"h":h}
    df = pd.DataFrame(data)
            
                
    ax[0,0].set_xlabel('h lavel of chart')
    ax[0,1].scatter(
                    df['h'],
                    df['cpu'],
                    
                    color='red')
    ax[1,0].hist(df['cpu'],color='green')
    ax[1,1].plot(df['h'],df['cpu']
                #  ,df['ram_used'],df['disk_percent']
                 )
    # ax[2,1].bar(x=df['h'],height=df['cpu_percent'],color='green',width=5,edgecolor='black')
    ax[2,1].bar(df['h'],df['cpu'],color='orange',edgecolor='black')
    sns.kdeplot(data=df[['cpu',
                        #  'cpu_percent'
                         ]],
                    fill=True,ax=ax[2, 0])
    # sns.heatmap(
    #     df.corr(),
    #     annot=True,
    #     ax=ax[2, 0]
         
    # )

    



    
    ax[0,0].set_ylabel('y lavel of graph')
    ax[0,0].pie(df['cpu'],labels=df['h'],autopct='%0.1f%%')
    ax[0,0].set_title('main title data se')


    
    #for i in range(sample_df.shape[0]):
        #plt.text(sample_df['avg'].values[i],sample_df['strike_rate'].values[i],sample_df['batter'].values[i],color='green')
    ax[0,1].set_xlabel('x lavel of chart')
    ax[0,1].set_ylabel('y lavel of graph')
    ax[0,1].set_title('main title data se')

    
    ax[1,0].set_xlabel('x lavel of chart')
    ax[1,0].set_ylabel('y lavel of graph')
    ax[1,0].set_title('main title data se')

    
    ax[1,1].set_xlabel('x lavel of chart')
    ax[1,1].set_ylabel('y lavel of graph')
    ax[1,1].set_title('main title data se')

    
    ax[2,1].set_xlabel('x lavel of chart')
    ax[2,1].set_ylabel('y lavel of graph')
    ax[2,1].set_title('main title data se')

    
    ax[2,0].set_xlabel('x lavel of chart')
    ax[2,0].set_ylabel('y lavel of graph')
    ax[2,0].set_title('main title data se')

            
    plt.tight_layout()
    # plt.title(f"Iteration {k+1}")
    plt.draw()
    # plt.clf()
    plt.pause(0.001)
    print(df)
    cpuu.pop(0)
    cpu_per.pop(0) 
    ram_used.pop(0)
    ram_total.pop(0) 
    disk_per.pop(0) 
    h.pop(0)
            
    time.sleep(0.001)
    

    # sns.heatmap(df.corr(),
    #                 annot=True)
    # sns.kdeplot(data=df[['my_array','your_array']],
    #             fill=True)

    # sns.scatterplot(data=df,
    #                 x='my_array',
    #                 y='your_array',
    #                 style='bool'
    #                 ,size='my_array')

    # corr = df.corr()
    
    #             sns.heatmap(corr,
    #             cmap='coolwarm',
    #             annot=True)

    # sns.lineplot(data=df, x='my_array', y='your_array')

    # plt.bar(x=df['my_array'],height=df['your_array'],color='green',width=5,edgecolor='black')