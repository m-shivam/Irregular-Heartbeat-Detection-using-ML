#File to save images of beats in a specified directory

import os 
import wfdb
import signal_info
import directory_structure
import annotation_data_interface as ADI
import natsort  # module used to sort file names


if __name__ == '__main__':

	#find directory where data is
	signal_dir = directory_structure.getReadDirectory('mit-bih_waveform')

	#get all .hea and .dat files (respectively)
	signal_files = directory_structure.filesInDirectory('.hea', signal_dir)

	# sort file names in ascending order in list
	signal_files = natsort.natsorted(signal_files)

	#extract and save beats from file provided
	for signal_file in signal_files:
		# get annotation data frame of signal file
		ann_df = ADI.getAnnotationDataFrame(directory_structure.removeFileExtension(signal_file))

		# uncomment to save images of beats
		signal_info.extractBeatsFromPatient(signal_dir + '/' + directory_structure.removeFileExtension(signal_file), ann_df)