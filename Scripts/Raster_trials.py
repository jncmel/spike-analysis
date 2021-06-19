"""
Script to plot the raster across n(usually 10) trials for different clusters (putative cells) obtained from spike sorting using Spyking-Circus. The result file contains the spiketimes and cluster ids of the different clusters. Spiktimes 4s after the stimulus was taken as part of the response.     
"""
import numpy as np
import matplotlib.pyplot as plt
import h5py


f=h5py.File('//result file path here//','r')
cluster_ids=[] #Ids of the clusters which will be used for further analysis 
n=20     # Number of trials
start_time=1367.917     #Stimulus start time

stimulus_onset_times=[]  #Array to store the stimulus times


for j in range (0,n):                       
    times=start_time+j*(5.5)
    stimulus_onset_times.append(times)


stimulus_onset_times=np.array(stimulus_onset_times)


for i in cluster_ids:
    array=f['spiketimes']['temp_'+str(i)]  #Reading spiketimes of particular cluster into an array
    array_sorted=np.ravel(array)/25000  #Divide by sampling rate to get spiketimes. 
    psth_trials=[]       #Array to store spike timings across trials

    for j in stimulus_onset_times:
        times=array_sorted[(array_sorted>j) & (array_sorted<(j+4))] # Spikes between onset of stimulus and 4s after.
        times=np.array(times)
        times=times-j                                               #Align the spiketimes to the stimulus onset time for each trial
        psth_trials.append(times)                                  #Array of n (number of trials) arrays of stimulus response across trials 


    


    fig, ax1 = plt.subplots()
    ax1.eventplot(psth_trials,linelengths=0.5)
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Trials')
    ax1.set_title('Raster across trials for Cluster_'+str(i)+'_Control')
    ax1.axvspan(0,0.5, color='g', alpha=0.5, lw=0) 
    ax1.set_xlim([0,5])
#    ax1.set_ylim([-1,10])
    left, bottom, width, height = [0.70, 0.68, 0.2, 0.2]
    ax2 = fig.add_axes([left, bottom, width, height])
    isi=np.diff(1000*array_sorted)   #Inter Spike Interval (ISI) of the clusters is also plotted 
    isi_bins=np.arange(0,100,1)
    ax2.hist(isi,bins=isi_bins)
    ax2.set_yticks([])
    ax2.locator_params(axis="x", nbins=2)
    #ax2.locator_params(axis="y", nbins=2)
    #ax2.set_xlabel('Time (ms)')
    plt.savefig('../Plots/P2_14_05_21/Raster_Trials/Control/Raster_trials_Cluster_'+str(i)+'_Control_500.png', bbox_inches='tight', dpi=500)
#    plt.show()
    plt.close()

