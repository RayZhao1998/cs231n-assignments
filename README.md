<h1 align="center">CS231n Assignments</h1>
<p align="center"><b>Deep Learning for Computer Vision</b></p>
<p align="center"><i>Stanford - Spring 2025</i></p>

[中文 README](./README_CN.md) | English README

---

## Resources

- [Course Homepage](https://cs231n.stanford.edu/index.html)
- [Assignment Introduction](https://cs231n.stanford.edu/assignments.html)
- [mantasu's cs231n assignment solutions](https://github.com/mantasu/cs231n)

## Getting Started

The assignments are configured to run on Google Colab by default, but you can also run them locally.

```shell
$ uv venv --python 3.11
$ source .venv/bin/activate
$ python -m pip install -r requirements.txt
```

## Notebook Hygiene

Set up the `pre-commit` hook to automatically clear notebook outputs before every commit.

```shell
$ python -m pip install pre-commit
$ pre-commit install
```

## Status

- [ ] Assignment 1
    - [ ] Q1: k-Nearest Neighbor classifier
    - [ ] Q2: Implement a Softmax classifier
    - [ ] Q3: Two-Layer Neural Network
    - [ ] Q4: Higher Level Representations: Image Features
    - [ ] Q5: Training a fully connected network
- [ ] Assignment 2
    - [ ] Q1: Batch Normalization
    - [ ] Q2: Dropout
    - [ ] Q3: Convolutional Neural Networks
    - [ ] Q4: PyTorch on CIFAR-10
    - [ ] Q5: Image Captioning with Vanilla RNNs
- [ ] Assignment 3
    - [ ] Q1: Image Captioning with Transformers
    - [ ] Q2: Self-Supervised Learning for Image Classification
    - [ ] Q3: Denoising Diffusion Probabilistic Models
    - [ ] Q4: CLIP and Dino
