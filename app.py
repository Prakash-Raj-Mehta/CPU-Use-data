import psutil
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib.animation import FuncAnimation
plt.ion()
st.title("Welcome to My App")
st.set_page_config(
    page_title="Real-Time System Monitor",
    layout="wide" 
)
st.markdown("""
<style>
    /* Hide Streamlit default header */
    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* Button container - fixed top right */
    .dev-profile-btn {
        margin-top: 80px;
        position: fixed;
        top: 18px;
        right: 28px;
        z-index: 9999;
    }

    .dev-profile-btn a {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 10px 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        text-decoration: none !important;
        font-family: 'Segoe UI', system-ui, sans-serif;
        font-size: 14px;
        font-weight: 600;
        
        border-radius: 50px;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        letter-spacing: 0.3px;
    }

    .dev-profile-btn a:hover {
        cursor: pointer;
        transform: translateY(-3px) scale(1.03);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.55);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }

    .dev-profile-btn a:active {
        transform: translateY(-1px) scale(0.98);
    }

    /* Optional subtle pulse animation on load */
    @keyframes softPulse {
        0% { box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4); }
        50% { box-shadow: 0 4px 22px rgba(102, 126, 234, 0.6); }
        100% { box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4); }
    }

    .dev-profile-btn a {
        animation: softPulse 2.5s ease-in-out infinite;
    }

    .dev-profile-btn a:hover {
        animation: none;
    }
</style>

<div class="dev-profile-btn">
    <a href="https://prakash-raj-mehta.github.io/portfolio/" target="_blank">
        👨‍💻 View Developer Profile
    </a>
</div>
""", unsafe_allow_html=True)

# st.set_page_config(page_layout="wide")
placeholder = st.empty()
st.title("Welcome to My App")

















fig,ax=plt.subplots(nrows=3,ncols=2,figsize=(20,20))
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

    with placeholder.container():
        st.pyplot(fig, clear_figure=False)
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