"""
Script to plot the firing rate of different clusters averaged over n trials. The bin size was calculated from the MSE estimation for the different clusters.

"""
import numpy as np
import matplotlib.pyplot as plt
import h5py


f=h5py.File('//path to result file//','r')
cluster_ids=[] # Cluster ids taken for further analysis
start_time=1367.917     #Stimulus start time
start=0
n=10                        # Number of trials + 1
bin_size=50

stimulus_onset_times=[]
for j in range (start,n):
    times=start_time+j*(5.5)
    stimulus_onset_times.append(times)


stimulus_onset_times=np.array(stimulus_onset_times)

custom_bins=np.arange(0,5000,bin_size)

for i in f['spiketimes']:
    psth_trials=[]       #Array to store spike timings across trials
    array=f['spiketimes'][i] # Store spiketimes of particular clusters into an array
    array_sorted=np.ravel(array)/25000  #Divide by sampling rate to get spiketimes. 

    for j in stimulus_onset_times:
        times=array_sorted[(array_sorted>j) & (array_sorted<(j+4))] # Spikes between onset of stimulus till 4s after.
        times=np.array(times)
        times=times-j                                               # Align spiketimes to the stimulus for different trials.
        psth_trials.append(times)                                   # Array of n arrays with spiketimes aligned to stimulus.


    print(len(psth_trials))        


#To convert psth_trials to one single array for plotting histogram 
    post_stimulus_times=1000*np.concatenate(psth_trials)
    counts,bin_edges=np.histogram(post_stimulus_times,custom_bins)
    counts=1000*((counts/(n-start)/bin_size)) #Firing rate from total counts
    counts=np.append(counts,0)

    fig, ax1 = plt.subplots()
    ax1.plot(custom_bins,counts,color='black')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Firing Rate (Spikes/s)')
    ax1.set_title('Firing rate for Cluster_'+str(i)+'_Control')
    ax1.axvspan(0,500, color='gray', alpha=1, lw=0)
    ax1.set_xlim([0,5000])
    #ax1.set_ylim([0,250])
    left, bottom, width, height = [0.70, 0.68, 0.2, 0.2]
    ax2 = fig.add_axes([left, bottom, width, height])
    isi=np.diff(1000*array_sorted) #Inter Spike Interval (ISI) is also plotted for the cluster
    isi_bins=np.arange(0,100,1)
    ax2.hist(isi,bins=isi_bins,color='gray')
    ax2.set_yticks([])
    ax2.locator_params(axis="x", nbins=2)
    #ax2.locator_params(axis="y", nbins=2)
    #ax2.set_xlabel('Time (ms)')
#    plt.savefig('//path to save the image//', bbox_inches='tight', dpi=500)
    plt.show()
#    plt.close()


