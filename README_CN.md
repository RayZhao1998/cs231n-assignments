<h1 align="center">CS231n Assignments</h1>
<p align="center"><b>Deep Learning for Computer Vision</b></p>
<p align="center"><i>Stanford - Spring 2025</i></p>

[English README](./README.md) | 中文版 README

---

## 资源

- [课程首页](https://cs231n.stanford.edu/index.html)
- [Assignment 介绍](https://cs231n.stanford.edu/assignments.html)
- [mantasu's cs224n assignment solutions](https://github.com/mantasu/cs231n)

## 启动

assignments 的默认配置是在 Google Colab 上执行，你也可以本地运行

```shell
$ uv venv --python 3.11
$ source .venv/bin/activate
$ python -m pip install -r requirements.txt
```

## Notebook 清理

安装并启用 `pre-commit` 钩子，在提交前自动清理 notebook 的输出内容。

```shell
$ python -m pip install pre-commit
$ pre-commit install
```

## 状态

- [ ] Assignment 1
    - [ ] Q1: k-Nearest Neighbor classifier
    - [ ] Q2: Implement a Softmax classifier
    - [ ] Q3: Two-Layer Neural Network
    - [ ] Q4: Higher Level Representations: Image Features
    - [ ] Q5: Training a fully connected network
- [ ] Assignment 2
    - [x] Q1: Batch Normalization
    - [ ] Q2: Dropout
    - [ ] Q3: Convolutional Neural Networks
    - [ ] Q4: PyTorch on CIFAR-10
    - [ ] Q5: Image Captioning with Vanilla RNNs
- [ ] Assignment 3
    - [ ] Q1: Image Captioning with Transformers
    - [ ] Q2: Self-Supervised Learning for Image Classification
    - [ ] Q3: Denoising Diffusion Probabilistic Models
    - [ ] Q4: CLIP and Dino
