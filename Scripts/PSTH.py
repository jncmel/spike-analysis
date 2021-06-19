import numpy as np
import matplotlib.pyplot as plt
import h5py


f=h5py.File('./P2_14_05_21/P2_14_05_21.result-final.hdf5','r')
cluster_ids=[0,1,3,5,7,11,13,15,20,21,25,29,33,34,37,42,48,51,54,56,60,65,70,71,73]
start_time=1367.917     #Stimulus start time

stimulus_onset_times=[]
for j in range (0,10):
    times=start_time+j*(5.5)
    stimulus_onset_times.append(times)


stimulus_onset_times=np.array(stimulus_onset_times)

psth_trials=[]       #Array to store spike timings across trials
custom_bins=np.arange(0,5000,20)

for i in cluster_ids:
    array=f['spiketimes']['temp_'+str(i)]
    array_sorted=np.ravel(array)/25000  #Divide by sampling rate to get spiketimes. 

    for j in stimulus_onset_times:
#        print(j)
        times=array_sorted[(array_sorted>j) & (array_sorted<(j+4))] # Spikes between onset of stimulus
        times=np.array(times)
        times=times-j
        psth_trials.append(times)                                  # and 1000ms after.


#To convert psth_trials to one single array for plotting histogram 


    post_stimulus_times=1000*np.concatenate(psth_trials)
  #  print(len(post_stimulus_times))
  #  print(len(post_stimulus_times))

    fig, ax1 = plt.subplots()
    

    ax1.hist(post_stimulus_times, bins=custom_bins)
    ax1.set_xlabel('Time (ms)')
    ax1.set_ylabel('Counts')
    ax1.set_title('PSTH for Cluster_'+str(i)+' Control')
    #ax1.fill_between(0,0,0,50,color='blue', alpha=0.5)
    ax1.axvspan(0,500, color='g', alpha=0.5, lw=0)
    ax1.set_xlim([0,5000])
    left, bottom, width, height = [0.70, 0.68, 0.2, 0.2]
    ax2 = fig.add_axes([left, bottom, width, height])
    isi=np.diff(1000*array_sorted)
    isi_bins=np.arange(0,100,1)
    ax2.hist(isi,bins=isi_bins)
    ax2.set_yticks([])
    ax2.locator_params(axis="x", nbins=2)
    #ax2.locator_params(axis="y", nbins=2)
    #ax2.set_xlabel('Time (ms)')
    plt.savefig('../Plots/P2_14_05_21/PSTH_Cluster_'+str(i)+'_Control_500.png', bbox_inches='tight', dpi=500)
   # plt.show()
    plt.close()
    psth_trials=[]      #To reset the array for the next cluster 

