# Subretinal Polymer Repository 

Repository for the results of the spike sorting and custom scripts used for the analysis post sorting.
The recordings were done on different days(E14-E18) of the developing chick retina with a 60 electrode MEA with 30&mu;m  electrodes and an interelctrode distance of 200&mu;m. Using a MEA-1060-Inv-BC fom Multi Channel Systems.

<!--![plot](https://github.com/jncmel/spike-analysis/blob/main/Filtered_data.png | width=100)-->
<img src="https://github.com/jncmel/spike-analysis/blob/main/Filtered_data.png" width="700"> 


https://user-images.githubusercontent.com/43720482/122711261-8640b800-d27f-11eb-9a5a-55c1be4606f6.mp4 

*Short video showing light evoked activity from multiple electrodes in an E16 chick retina with the polymer in the subretinal side for two successive full field flashes of 500ms separated by a duration of 10s.*
<br/>
- The spike sorting was done using Spyking-Circus [https://github.com/spyking-circus/spyking-circus]. Spyking-Circus can be installed using conda, detailed instructions can be found in the website.
- The link to the relevant recordings can be found @

## Contents of the repository
- Recording_Details.xlsx : Excel sheet containing the details of the different recordings. 
- mea_recent.prb : Probe file containing the electrode mapping which is required for spike sorting.
- Stimulus_times.pdf : Table of stimulus times for different recordings under different conditions.
### Spike_sorting

Contains the folders corresponding to different recordings with the .params and deadtimes files needed for checking the sorting using Spyking-Circus. Additionally, the path to the .prb file for the eletrode array (here: mea_recent.prb) has to be mentioned in the .params file. The raw data has to be copied into the relevant folder and the sorting can be done after installing Spyking-Circus via the command: <br/>
`spyking-circus path/mydata.raw`<br/> <br/>
After the sorting is done, a result file will get generated in `path/mydata/mydata.result.hdf5`. This file contains the spiketimes of differerent templats stored in .hdf5 format. More details of the generated files can be found in the Spyking-Circus website.


### Results
Contains the final templates and their spiketimes for different recordings which were used for plotting the raster across trials and firing rates.

### Scripts
Custom python code used for plotting the raster across trials and firing rate of different templates from the result files of different recordings. <br/>The stimulus time for different conditions (Control, CNQX addition, etc...) is required for recreating the plots. This can be found in **Stimulus_times.pdf**
- The scripts used for plotting the raster and firing rate requires [h5py](https://docs.h5py.org/en/stable/#), which can be installed as <br/> `pip install h5py`


