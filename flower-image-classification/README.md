# Flower Image Classification Using Transfer Learning (MobileNet)

## Description
This project aims to build an image classification model using a flower dataset obtained from [Kaggle: Flower Classification Dataset](https://www.kaggle.com/datasets/marquis03/flower-classification). The model applies a **transfer learning** approach with a **pre-trained model** to improve accuracy and reduce overfitting.

### Dataset
The dataset consists of 13,740 flower images categorized into 14 classes. It can be downloaded from [Kaggle: Flower Classification Dataset](https://www.kaggle.com/datasets/marquis03/flower-classification).

### Project Objectives
1. Train an image classification model using transfer learning with a pre-trained architecture.
2. Reduce overfitting by applying techniques such as Dropout, Early Stopping, and fine-tuning of the pre-trained model.
3. Export the trained model in three different formats:
   - **SavedModel** format for TensorFlow
   - **TensorFlow.js** format for web applications
   - **TensorFlow Lite** format for mobile or embedded applications
