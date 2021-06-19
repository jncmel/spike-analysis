"""
Script to plot
"""

import numpy as np
import matplotlib.pyplot as plt
import h5py


f=h5py.File('./P2_14_05_21/P2_14_05_21.result-final.hdf5','r')
cluster_ids=[0,1,3,5,7,11,13,15,20,21,25,29,33,34,37,42,48,51,54,56,60,65,70,71,73]
start_time=1367.917     #Stimulus start time
n=17                    # Number of trials

stimulus_onset_times=[]
for j in range (0,n):
    times=start_time+j*(5.5)
    stimulus_onset_times.append(times)


stimulus_onset_times=np.array(stimulus_onset_times)

bin_sizes=np.arange(0.005,1,0.005)
print(bin_sizes)

for i in cluster_ids:
    psth_trials=[]       #Array to store spike timings across trials
    array=f['spiketimes']['temp_'+str(i)]
    array_sorted=np.ravel(array)/25000  #Divide by sampling rate to get spiketimes. 

    for j in stimulus_onset_times:
#        print(j)
        times=array_sorted[(array_sorted>j) & (array_sorted<(j+4))] # Spikes between onset of stimulus
        times=np.array(times)
        times=times-j
        psth_trials.append(times)                                  # and4000ms after.
    

    cost_array=[]

    post_stimulus_times=np.concatenate(psth_trials)
    for b in bin_sizes:
        custom_bins=np.arange(0,5,b)
        counts,bin_edges=np.histogram(post_stimulus_times,custom_bins)
#    counts=(counts/10)/0.02
        counts=np.append(counts,0)
        k_avg=np.mean(counts)
        k_var=np.var(counts,ddof=0)
        cost_function= ((2*k_avg)-k_var)/((n*b)**2)
        cost_array.append(cost_function)


    plt.plot(bin_sizes,cost_array)
    plt.show()



#To convert psth_trials to one single array for plotting histogram 
#
#    print(len(psth_trials))

    





  #  print(len(post_stimulus_times))
  #  print(len(post_stimulus_times))

#    fig, ax1 = plt.subplots()
#    
#
#    ax1.plot(custom_bins,counts)
#    ax1.set_xlabel('Time (s)')
#    ax1.set_ylabel('Firing Rate (Spikes/s)')
#    ax1.set_title('Firing rate for Cluster_'+str(i)+' Control')
#    #ax1.fill_between(0,0,0,50,color='blue', alpha=0.5)
#    ax1.axvspan(0,0.5, color='g', alpha=0.5, lw=0)
#    ax1.set_xlim([0,5])
#    left, bottom, width, height = [0.70, 0.68, 0.2, 0.2]
#    ax2 = fig.add_axes([left, bottom, width, height])
#    isi=np.diff(1000*array_sorted)
#    isi_bins=np.arange(0,100,1)
#    ax2.hist(isi,bins=isi_bins)
#    ax2.set_yticks([])
#    ax2.locator_params(axis="x", nbins=2)
#    #ax2.locator_params(axis="y", nbins=2)
#    #ax2.set_xlabel('Time (ms)')
#    plt.savefig('../Plots/P2_14_05_21/Firing_rate/PSTH_Cluster_'+str(i)+'_Control_500.png', bbox_inches='tight', dpi=500)
#    plt.show()
#    plt.close()
#    psth_trials=[]      #To reset the array for the next cluster 

