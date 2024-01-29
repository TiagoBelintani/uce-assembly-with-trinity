import os
import subprocess
import argparse
import configparser

def get_args():
    parser = argparse.ArgumentParser(
        description="""Assemble UCE data using Trinity"""
    )
    parser.add_argument(
        "--output",
        required=True,
        help="The directory to store the assembly data"
    )
    parser.add_argument(
        "--cores",
        type=int,
        default=1,
        help="The number of compute cores/threads to run with Trinity"
    )
    parser.add_argument(
        "--config-file",
        required=True,
        help="Path to the configuration file containing sample information"
    )
    return parser.parse_args()

def read_config_file(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    samples = {}
    for sample, path in config['samples'].items():
        samples[sample] = path
    return samples

def run_trinity_uce(sample, sample_dir, output_dir, cores):
    left_reads = os.path.join(sample_dir, "split-adapter-quality-trimmed", f"{sample.capitalize()}-READ1.fastq.gz")
    right_reads = os.path.join(sample_dir, "split-adapter-quality-trimmed", f"{sample.capitalize()}-READ2.fastq.gz")

    print(f"Left reads: {left_reads}")
    print(f"Right reads: {right_reads}")

    trinity_output_dir = os.path.join(output_dir, f"{sample}_trinity_output")

    trinity_cmd = [
        "Trinity",
        "--seqType", "fq",
        "--max_memory", "8G",
        "--left", left_reads,
        "--right", right_reads,
        "--CPU", str(cores),
        "--output", trinity_output_dir
    ]
    
    print(f"Running Trinity with command: {' '.join(trinity_cmd)}")
    subprocess.run(trinity_cmd, check=True)

def generate_symlinks(contig_dir, sample, trinity_output_dir):
    trinity_fasta = os.path.join(trinity_output_dir, "Trinity.fasta")
    contig_link = os.path.join(contig_dir, f"{sample}.contigs.fasta")
    os.symlink(os.path.relpath(trinity_fasta, contig_dir), contig_link)

def main():
    args = get_args()
    
    # Create output directory if it doesn't exist
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    # Read sample information from the config file
    samples = read_config_file(args.config_file)

    for sample, sample_dir in samples.items():
        # Create Trinity output directory for each sample
        trinity_output_dir = os.path.join(args.output, f"{sample}_trinity_output")
        os.makedirs(trinity_output_dir)

        # Run Trinity for each sample
        run_trinity_uce(sample, sample_dir, args.output, args.cores)

        # Create contigs directory if it doesn't exist
        contig_dir = os.path.join(args.output, "contigs")
        if not os.path.exists(contig_dir):
            os.makedirs(contig_dir)

        # Generate symlinks to contigs
        generate_symlinks(contig_dir, sample, trinity_output_dir)

if __name__ == "__main__":
    main()
