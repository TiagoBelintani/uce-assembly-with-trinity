# uce-assembly-with-trinity
Python Scripts for Assembling UCEs with Trinity: Option to the Phyluce Package 

Script Description: Trinity Assembly Wrapper Script

This Python script serves as a wrapper for Trinity, automating the assembly of UCE (Ultraconserved Element) data. The script reads sample information from a provided configuration file, runs Trinity for each sample, and generates symbolic links to the resulting contig files.

Usage:

bash
Copy code
python trinity_uce_assemblo.py --output output_directory --cores num_cores --config-file config_file
Arguments:

--output: The directory to store the assembly data.
--cores: The number of compute cores/threads to run with Trinity (default is 1).
--config-file: Path to the configuration file containing sample information.
How to Use:

Place the script (script_name.py) in the directory where you want to run the Trinity assembly.
Open a terminal in the directory containing the script.
Execute the script by providing the output directory, number of cores, and the configuration file as arguments.
Example:

bash
Copy code
python trinity_uce_assemblo.py --output /path/to/output_data --cores 4 --config-file /path/to/sample_config.ini

Script Functionality:

Parses command-line arguments, including the output directory, number of cores, and the configuration file.
Reads sample information from the provided configuration file.
Creates Trinity output directories for each sample and runs Trinity for assembly.
Creates a contigs directory if it doesn't exist and generates symbolic links to the Trinity contig files.
Provides informative print statements during the execution of the script.
This script streamlines the process of UCE data assembly using Trinity, making it convenient for handling multiple samples with varying configurations.
