<h1 align="center"> LSTM </h1> <br>
<p align="center">
  <!--<a href="https://gitpoint.co/"> -->
    <img alt="Init" title="Presentation" src="https://i.imgur.com/jBfTlan.png" width="450">
  </a>
</p>

<p align="center">
  Facial recognition system using neural networks
</p>

<!-- 
<p align="center">
  <a href="https://itunes.apple.com/us/app/gitpoint/id1251245162?mt=8">
    <img alt="Download on the App Store" title="App Store" src="http://i.imgur.com/0n2zqHD.png" width="140">
  </a>

  <a href="https://play.google.com/store/apps/details?id=com.gitpoint">
    <img alt="Get it on Google Play" title="Google Play" src="http://i.imgur.com/mtGRPuM.png" width="140">
  </a>
</p> 
-->

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

-----

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Feedback](#feedback)
- [Build Process](#build-process)
- [Backers](#backers-)
- [Sponsors](#sponsors-)
- [Acknowledgments](#acknowledgments)

<!-- [Contributors](#contributors) -->
<!-- END doctoc generated TOC please keep comment here to allow auto update -->

-----

## Introduction

Facial recognition systems have become ubiquitous in our every lives. When the iPhone X was first unveiledin 2017, Apple boasted that their new state-of-the-art face ID system was able to instantaneously recognize and authenticate users with just a single glance. Today, almost all smartphones have a facial recognition security system.

A face recognition problem can be broken down into the following smaller subproblems:

- **Face detection**: Detect and isolate faces in the image. In an image with multiple face, we need to detect each of them separately. 
- **Face recognition**: For each detected face in the image, we run it through a neural network to classify the subject.

### Face detection

Face detecion can be implemented by the OpenCV library in Python. OpenCV is an open source computer vision librery for computer vision task.

## Face recognition

Intuitively, humans recognize faces by comparing their key features. For example, humans use features such as the shape of eyes, the thickness of the eyebrows, the sizse of the nose, the overall shape of the face, and so on to recognize a person. This ability comes naturally to us, and we are seldom affected by varations in angles and lighting. For facial recognition, researchers have found that when convolutional layers are applied to human faces, they extract spatial features, such as eyes and noses. 

This insight forms the core of our algorithm for one-shot learning:

- Use convolutional layers to extract identifying features from faces. 
- Using the euclidan distance, measure the difference of the two lower-dimension vectors output from the convolutional layers. The Euclidian distance is inversely proportional to the simalirity between the two images

**All project is in the folder *Notebook*.**

<p align="center">
  <img src = "https://i.imgur.com/ZwhaYns.png", width="600">
</p>

-----

## Features

Principal's model feactures:

- Siamese Neural Network
- Database of Faces created by AT&T Laboratories, Cambridge.
- CNN and Euclidan distance.



<p align="center">
  <img src = "https://i.imgur.com/Px8pWP9.png" width=400>
</p>

> Model schematic
-----

## Feedback

Feel free to send us feedback on [Twitter](https://twitter.com/dionicio_98) or [file an issue](https://github.com/dionicio-alberto/Sentiment-Analysis-of-Movie-Reviews-Using-LSTM/issues/new). Feature requests are always welcome. If you wish to contribute, please take a quick look at the [guidelines](./CONTRIBUTING.md)!

<!-- If there's anything you'd like to chat about, please feel free to join our [Gitter chat](https://gitter.im/git-point)! -->

-----

<!-- ## Contributors

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification and is brought to you by these [awesome contributors](./CONTRIBUTORS.md).

----- -->


## Build Process

- Follow the guide in the book [Nerual Network Projects with Python](https://www.amazon.com/Neural-Network-Projects-Python-ultimate/dp/1789138906) for getting started building a project with native code.
- Use the follows libreries:
  - Numpy
  - Matplotlib
  - Seaborn
  - Keras
  - TensorFlow
  - CV2
- Data Analysis and Exploration
- Data Preprocessing
- Modeling Neural Network
- Training Neural Network
- Evaluating Neural

For Model Training use Google Colab Resources.

Please take a look at the [contributing guidelines](./CONTRIBUTING.md) for a detailed about the results

-----

## Results Analysis

The models with RMSprop has the best accuracy.

![results](https://i.imgur.com/9T1AHXP.png)

<!--  ## Backers [![Backers on Open Collective](https://opencollective.com/git-point/backers/badge.svg)](#backers)

Thank you to all our backers! 🙏 [[Become a backer](https://opencollective.com/git-point#backer)]

<a href="https://opencollective.com/git-point#backers" target="_blank"><img src="https://opencollective.com/git-point/backers.svg?width=890"></a> -->


## Sponsors <!-- [![Sponsors on Open Collective](https://opencollective.com/git-point/sponsors/badge.svg)](#sponsors) -->

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://www.linkedin.com/in/dionicio-perez-landero-446605170/)]

<a href="https://www.linkedin.com/in/dionicio-perez-landero-446605170/" target="_blank"><img src="https://opencollective.com/git-point/sponsor/0/avatar.svg"></a>
<a href="https://www.linkedin.com/in/dionicio-perez-landero-446605170/" target="_blank"><img src="https://opencollective.com/git-point/sponsor/1/avatar.svg"></a>

## Acknowledgments

Thanks to my parents for all them love.
