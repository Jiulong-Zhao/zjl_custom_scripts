# 🧬 batch_select_contigs.py

### 批量筛选FASTA序列长度脚本 | Batch Filtering of FASTA Contigs by Length

---

## 📖 项目简介 | Project Overview

**中文：**

本脚本用于批量查找指定目录下的目标FASTA文件（如 `final.contigs.fa`），筛选出长度大于等于指定阈值的contig序列，并将其分别输出为独立的FASTA文件。特别适用于高通量测序组装结果的自动化处理。

**English:**

This script recursively searches a directory for target FASTA files (e.g., `final.contigs.fa`), filters contigs longer than or equal to a given threshold, and writes each sample's filtered results to a separate FASTA file. It is ideal for high-throughput genome assembly post-processing.

---

## 📦 依赖环境 | Requirements

- Python ≥ 3.7
- [Biopython](https://biopython.org/)  
  安装方法 / Install via pip:

```bash
pip install biopython

🚀 使用方法 | Usage
python batch_select_contigs.py \
  -i <搜索目录> \
  -l <最小长度> \
  -o <输出目录> \
  -k <关键词文件名>
🧩 参数说明 | Arguments
参数 / Argument	必须 / Required	说明 / Description
-i, --input_dir	是 / Yes	要递归搜索的根目录
-l, --length	是 / Yes	保留contig的最小长度（如 2000）
-o, --output_dir	是 / Yes	输出FASTA文件的保存目录
-k, --keyword	否 / No	精确匹配的目标文件名（默认：final.contigs.fa）

🧪 示例 | Example
python batch_select_contigs.py \
  -i ../../2.megahit_assembly/ \
  -l 2000 \
  -o ./2k_filtered_output/ \
  -k final.contigs.fa
该命令将查找 ../../2.megahit_assembly/ 中所有名为 final.contigs.fa 的文件，
筛选其中长度≥2000 bp的contigs，并将结果输出到 ./2k_filtered_output/，每个样本一个文件。

📂 输出说明 | Output
每个样本将生成一个FASTA文件，命名格式如下：
<length>+_<sample_name>.fa
例如：
2000+_D0B1.fa
2000+_D0B2.fa
...
每个输出文件中仅保留通过长度筛选的 contigs。

📜 许可协议 | License
本脚本为内部科研用途设计，可自由修改和使用。如用于公开项目，请注明作者与出处。

🙋 联系与反馈 | Contact
如有问题，欢迎提交 Issue 或联系作者。