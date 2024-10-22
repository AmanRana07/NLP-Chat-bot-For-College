# Helping New Students Access University Information Using NLP

This project focuses on developing a chatbot solution to assist new university students in accessing essential information like course details, hostel facilities, and event schedules. The chatbot leverages Natural Language Processing (NLP) to provide immediate and accurate responses to student queries, improving the overall onboarding experience.

## Abstract

New university students often face challenges in finding critical information necessary for their academic and social integration. This project presents a chatbot-based solution using NLP to address these issues. Multiple machine learning models, including Support Vector Machines (SVM), Naive Bayes, and Random Forest, were evaluated to optimize query intent classification, with Random Forest proving the most effective.

## Problem Statement

The main goal of this research is to develop an intelligent chatbot system that helps students access university-related information such as academic details, administrative procedures, and campus resources. The chatbot uses NLP to classify user queries and deliver accurate, timely responses.

## Features

- **Chat Interface**: A real-time chat system built with HTML, CSS, and JavaScript. It uses AJAX for smooth communication without page reloads.
- **Intent Recognition**: Utilizes machine learning models like Random Forest to predict user intent based on input.
- **Backend Integration**: A Django-based web application serves as the chatbot’s backend.
- **Admin Interface**: Allows dynamic updates to chatbot responses without the need for retraining.

## Technologies Used

- **Django Framework**: For backend web development and admin interface.
- **AJAX**: For real-time chat functionality.
- **SQLite Database**: To store intents and user interactions.
- **Python**: For model integration and backend scripting.
- **Natural Language Toolkit (NLTK)**: For text pre-processing, tokenization, and stopword removal.
- **TF-IDF Vectorization**: For transforming text into numerical vectors.
- **Machine Learning Models**: Implemented Support Vector Machines (SVM), Naive Bayes, and Random Forest for intent classification.

## Data Collection

- **Student Surveys**: Gathered frequently asked questions from new students.
- **Web Scraping**: Extracted relevant data from university websites, such as course catalogs and event schedules.
- **Manual Annotation**: Labeled common queries and their corresponding responses for training the chatbot.

## Dataset

The dataset consists of predefined intents such as:
- **Greeting**
- **Farewell**
- **College Timings**
- **Courses Offered**
- **Fees**
- **Location**
- **Hostel Facilities**
- **Admission Requirements for International Students**
- **Transportation Options**

Each intent has a set of patterns (user queries) and corresponding responses.

## Results and Discussion

The Random Forest model outperformed others, achieving:
- **Accuracy**: 92.5%
- **Precision**: 92.3%
- **Recall**: 92.5%
- **F1-Score**: 92.4%

Although Random Forest performed well, some misclassifications occurred due to ambiguous intents and misspellings.

## Future Enhancements

- **Mobile Compatibility**: Optimizing the chatbot for mobile platforms.
- **Advanced NLP Models**: Integrating transformer-based models like BERT or GPT for improved performance.
- **Real-Time Analytics**: Implementing query tracking to enhance responses over time.
- **Multi-Language Support**: Expanding the chatbot's capabilities to support multiple languages.

## Conclusion

This project successfully developed an NLP-based chatbot for university students, significantly improving the ease of accessing important information. The Random Forest model's strong performance in intent classification made it the optimal choice for this application.

## Authors

- **Aman Singh** (23122105)
- **Dipanwita Das** (23122046)
