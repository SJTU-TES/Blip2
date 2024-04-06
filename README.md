# Blip2
Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models, BLIP-2 beats Flamingo on zero-shot VQAv2 (65.0 vs 56.3), establishing new state-of-the-art on zero-shot captioning (on NoCaps 121.6 CIDEr score vs previous best 113.2). Equipped with powerful LLMs (e.g. OPT, FlanT5), BLIP-2 also unlocks the new zero-shot instructed vision-to-language generation capabilities for various interesting applications!

## 1. Install helper

**Please check your nvcc version and cuda version >= 11.7**
```bash
nvcc -V
nvidia-smi
```

**environment building**
```bash
# create a new conda environment
conda activate --name blip2 python=3.9
conda activate blip2

# Install the following packages in order
pip install peft==0.9.0
pip install Pillow==10.3.0
pip install Requests==2.31.0
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
pip install tqdm==4.66.2
pip install transformers==4.39.0

```

## 2. How to use

### 2.1 Download Pre-trained Files

Download Blip2's pre-trained files [here](https://huggingface.co/Salesforce/blip2-opt-2.7b).

### 2.2 Just try it!

Modify the text prompts and image in ``example.py`` and then run the following command.

```bash
CUDA_VISIBLE_DEVICES=0 python example.py
```

### 2.3 Reproducibility

<img src="https://ts1.cn.mm.bing.net/th/id/R-C.75eb2f4b2ba18ad45bef900cb84f1afa?rik=0ypFQ%2fHNlRZomQ&riu=http%3a%2f%2fyouimg1.c-ctrip.com%2ftarget%2ftg%2f551%2f901%2f988%2fb6c0b42fab064d0ba93e6d8160b8a799.jpg&ehk=1vNUtkCQznGRxCgjJrxgSZtOO7xgpxHCQviI9GNSuiQ%3d&risl=&pid=ImgRaw&r=0" width=80% height=100%>

- "Question: what is the main elements in the picture? "

- "Answer: the eiffel tower"