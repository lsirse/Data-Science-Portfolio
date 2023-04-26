# Automatic Generation of Image Descriptions
---

## Overview
Automatically describing the content of an image is a fundamental problem in artificial intelligence that connects computer vision and natural language processing. In this project, a generative model based on a CNN + RNN is developed that combines advances in computer vision and machine translation and that can be used to generate natural sentences describing an image. The model is trained to maximize the likelihood of the target description sentence given the training image. Initial experiments show that even after relatively little amount of training, the model is able to produce pretty reasonable results. 


## Use Cases


Image caption generation offers a plethora of significant use cases across various domains. It may aid visually impaired individuals by providing accurate textual descriptions of images, enhance their browsing experience. For social media platforms and content management systems, it could streamline content organization through automated metadata generation, improving searchability and content discovery. In the field of education, for example, it may enrich learning materials with contextual explanations, promoting better understanding for students. Another industry where image captioning could be applied is marketing. For example, ad targeting could be optimized by analyzing and captioning images with relevant keywords. There are many more use cases and industries where image captioning could make a significant impact and improve the lives of millions of human beings.

## Dataset

Dataset used is the COCO data set designed by Microsoft, it includes a large dataset of images and their descriptions.

![Coco](https://raw.githubusercontent.com/lsirse/Data-Science-Portfolio/deca408a2f9a5a01e46c021e1811fbcf4b35a4a3/image_caption/images/coco-examples.jpg)

You can read more about the dataset on the [website](http://cocodataset.org/#home) or in the [research paper](https://arxiv.org/pdf/1405.0312.pdf).

## Results

Here is an example with a relatively accurate caption:
![Example Image](https://github.com/lsirse/Data-Science-Portfolio/raw/master/image_caption/images/great_example.png)

Here is an example where model with accurate training could have performed better:
![Example Image](https://github.com/lsirse/Data-Science-Portfolio/raw/master/image_caption/images/bad_example.png)


## References

- [https://arxiv.org/pdf/1411.4555.pdf](https://arxiv.org/pdf/1411.4555.pdf)
- [https://arxiv.org/pdf/1502.03044.pdf](https://arxiv.org/pdf/1502.03044.pdf)

This project is part of Udacity's Computer Vision Nanodegree.
