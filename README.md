# Coding Camp Projects Portfolio
This repository includes a collection of final projects completed in the Coding Camp 2025 program, each focusing on practical implementation of data analysis, statistical modeling, and analytical reasoning in diverse case studies. Each project demonstrates a different analytical approach and application domain, ranging from business analytics to social impact and personalized systems.

## 1. Interactive Dashboard for Analyzing Bike Sharing Demand Trends 
This project presents an **interactive dashboard** designed to explore and analyze **bike sharing demand patterns** over time. The analysis focuses on understanding how weather conditions, seasonal variations, and temporal factors influence rental demand.

Through exploratory data analysis and time-based visualizations, the dashboard identifies peak and low-demand periods across different seasons and time intervals. The insights generated from this analysis can support data-driven decision making in operational planning and resource allocation for bike sharing services.

## 2. Bank Transaction Analysis Using Clustering and Pseudo-Label Classification
This project analyzes **bank transaction data** using a two-stage machine learning approach. First, **clustering** techniques were applied to identify underlying transaction patterns and segment customers based on behavioral similarities. The resulting clusters were then treated as **pseudo-labels** to build **classification** models capable of predicting transaction segments. This approach transforms unlabeled data into structured categories, enabling more scalable and automated classification.

The analysis demonstrates how unsupervised learning can be leveraged to generate meaningful groupings, which are subsequently used to train supervised models for improved decision support and customer segmentation strategies.

## 3. Canva User Review Sentiment Analysis Using NLP
This project applies Natural Language Processing (NLP) techniques to **analyze user sentiment from Canva reviews**. The analysis includes text preprocessing steps such as tokenization, stopword removal, and text normalization to prepare the data for modeling. eature extraction methods were used to transform textual data into numerical representations, followed by the implementation of classification models to predict sentiment categories. The results provide insights into overall user perception and highlight common themes associated with positive and negative feedback.

The findings demonstrate how unstructured textual data can be systematically processed and transformed into actionable insights for product evaluation and service improvement.

## 4. Flower Image Classification Using Transfer Learning (MobileNet)
This project implements an **image classification model** to categorize flower images using a **transfer learning** approach. Several modeling schemes were evaluated to identify the most effective configuration.

The best performance was achieved using a pre-trained MobileNet architecture combined with the SGD optimizer. By leveraging transfer learning, the model was able to utilize previously learned visual features and adapt them to the flower classification task. The selected configuration achieved a test accuracy of 91.16%, demonstrating strong generalization performance on unseen data while maintaining computational efficiency.

## 5. Predicting Student Depression Risk Using Supervised Machine Learning
This project develops a supervised machine learning model to **predict depression risk** among students using the Student Depression Dataset. The objective is to identify patterns and risk indicators that may contribute to mental health vulnerability in educational settings.

Several classification models were trained and evaluated to estimate depression risk. Model interpretability techniques, including SHAP (SHapley Additive exPlanations), were applied to understand the contribution of each feature to the prediction outcomes. The SHAP summary analysis revealed that the most significant risk factors include the presence of **suicidal thoughts, high academic pressure, and elevated financial stress**. Additional contributing factors include younger age, poor dietary habits, long study hours, low academic satisfaction, family history, and lower GPA.

These findings demonstrate how supervised learning models, combined with interpretability methods, can provide data-driven insights to support early risk identification strategies in educational environments. The model is intended for analytical and research purposes rather than clinical diagnosis.

## 6. Movie Recommendation System Using Content-Based and Collaborative Filtering
This project implements a **movie recommendation system** using two fundamental approaches: **content-based filtering** and **collaborative filtering**. Each method was developed and evaluated independently to compare their recommendation behavior.

The content-based approach generates recommendations by analyzing item features and user preferences, identifying similarities between movies based on attributes such as genre or metadata. In contrast, the collaborative filtering approach leverages user–item interaction patterns to recommend movies based on similarities among users or items.

By implementing both techniques separately, this project highlights the conceptual and practical differences between feature-driven and interaction-driven recommendation strategies. The results demonstrate how different modeling assumptions influence recommendation outcomes and personalization performance.

## Projects Directory
- [Interactive Dashboard for Analyzing Bike Sharing Demand Trends](bike-sharing-dashboard/)
- [Bank Transaction Analysis Using Clustering and Pseudo-Label Classification](bank-segmentation-classification/)
- [Canva User Review Sentiment Analysis Using NLP](canva-sentiment-analysis/)
- [Flower Image Classification Using Transfer Learning (MobileNet)](flower-image-classification/)
- [Predicting Student Depression Risk Using Supervised Machine Learning](student-depression-prediction/)
- [Movie Recommendation System Using Content-Based and Collaborative Filtering](movie-recommendation-system/)
