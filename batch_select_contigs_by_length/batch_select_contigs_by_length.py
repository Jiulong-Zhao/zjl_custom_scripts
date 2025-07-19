#!/usr/bin/env python3

import os
import argparse
from Bio import SeqIO

def parse_args():
    parser = argparse.ArgumentParser(description='Batch select contigs by length from fasta files.')
    parser.add_argument('-i', '--input_dir', required=True, help='Directory to search for fasta files')
    parser.add_argument('-l', '--length', required=True, type=int, help='Minimum contig length to keep')
    parser.add_argument('-o', '--output_dir', required=True, help='Directory to store output files')
    parser.add_argument('-k', '--keyword', default='final.contigs.fa', help='Filename keyword to match (default: final.contigs.fa)')
    return parser.parse_args()

def filter_fasta_by_length(input_fasta, output_fasta, min_length):
    """
    将长度大于等于 min_length 的序列写入新文件。
    """
    with open(input_fasta, 'r') as infile, open(output_fasta, 'w') as outfile:
        count = 0
        for record in SeqIO.parse(infile, 'fasta'):
            if len(record.seq) >= min_length:
                SeqIO.write(record, outfile, 'fasta')
                count += 1
        print(f"  -> {count} contigs written to {output_fasta}")

def main():
    args = parse_args()

    input_dir = os.path.abspath(args.input_dir)
    output_dir = os.path.abspath(args.output_dir)
    min_length = args.length
    keyword = args.keyword

    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 遍历查找匹配文件
    for dirpath, dirnames, filenames in os.walk(input_dir):
        for filename in filenames:
            if filename == keyword:
                input_path = os.path.join(dirpath, filename)

                # 获取样本名（上级目录名）
                sample_name = os.path.basename(os.path.dirname(input_path))

                # 输出文件名：如 2000+_D0B1.fa
                output_filename = f"{min_length}+_{sample_name}.fa"
                output_path = os.path.join(output_dir, output_filename)

                print(f"\nProcessing: {input_path}")
                filter_fasta_by_length(input_path, output_path, min_length)

if __name__ == '__main__':
    main()

