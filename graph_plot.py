import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def graph():
    dataset = pd.read_csv(r'C:\Users\Lohit\Desktop\Algo Project\time_data.csv')
    algorithms=np.unique(dataset.iloc[:,0])
    for i in range(len(algorithms)):
        indexes=[index for (index, item) in enumerate(dataset.iloc[:,0]) if item == algorithms[i]]
        no_inputs=[dataset.iloc[i,1] for i in indexes ]
        time=[dataset.iloc[i,2] for i in indexes ]
        no_inputs.append(0)
        time.append(0)
        res = {no_inputs[j]: time[j] for j in range(len(time))}
        res={key: value for key, value in sorted(res.items(), key=lambda item: item[0])}
        plt.plot( res.keys(),res.values(), label =algorithms[i],marker= 'X')
    plt.xlabel("Number Of Inputs")
    plt.ylabel("Time")
    plt.legend()
    plt.title('Algorithm Comparision')
    plt.show()
    




