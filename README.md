# Subretinal Polymer Repository 

Repository for the results of the spike sorting and custom scripts used for the analysis post sorting.
The recordings were done on different days(E14-E18) of the developing chick retina with a 60 electrode MEA with 30&mu;m  electrodes and an interelctrode distance of 200&mu;m. Using a MEA-1060-Inv-BC fom Multi Channel Systems.

<!--![plot](https://github.com/jncmel/spike-analysis/blob/main/Filtered_data.png | width=100)-->
<img src="https://github.com/jncmel/spike-analysis/blob/main/Filtered_data.png" width="700"> 


https://user-images.githubusercontent.com/43720482/122711261-8640b800-d27f-11eb-9a5a-55c1be4606f6.mp4

The spike sorting was done using Spyking-Circus [https://github.com/spyking-circus/spyking-circus]. The link to the relevant recordings to be used with the paramter files si @. 

## Contents of the repository

- mea_recent.prb : Probe file containing the electrode mapping which is required for spike sorting.
## Spike_sorting

Contains the .params and deadtimes files needed for checking the sorting using Spyking-Circus for different recordings.



## Results
Contains the spiketimes of the different clusters in .hdf5 format, obtained from spike sorting. 




## Scripts
Custom code used for plotting the raster across trials and firing rate of different clusters from the .hdf5 files of different recordings

- Cluster_ids: File containing the cluster_ids taken of different recodings used for the plots.

## Instructions
- Spyking-Circus can be installed by conda. Detailed instructions can be found in the website.
- The scripts used for plotting the raster and firing rate requires h5py, which can be installed as `pip install h5py`

