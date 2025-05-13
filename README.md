Corona_ChatBot_Project
A simple chatbot built using Python and TensorFlow to answer COVID-19 related queries.

🤖 Corona ChatBot Project

A simple AI chatbot built using TensorFlow and Keras that can interact with users based on predefined intents and responses. This project demonstrates how Natural Language Processing (NLP) can be used to build a rule-based chatbot.

---
📁 Project Structure

| File                                           | Purpose |
|------                                          |---------|
| `intents.json`                                 | Defines the chatbot’s patterns, tags, and responses |
| `Corona_ChatBot.py`                            | Preprocesses data and trains the chatbot model |
| `chatbot_model.h5`                             | Trained model saved after training |
| `words.pkl`, `classes.pkl`                     | Pickled vocabulary and intent classes |
| `chatbot_interface.py` / `gui_bot.py`          | Interface to interact with the chatbot |
| `train_chatbot.py`                             | (Optional) Refactored training script |
| `model.tflearn.*`, `data.pickle`, `checkpoint` | Old files from previous training methods (can be ignored) |

---

🛠️ Features

- Predefined intent-based rule-driven responses
- NLP tokenization and lemmatization using NLTK
- Intent classification using a simple neural network (TensorFlow/Keras)
- Easy to retrain with custom `intents.json`
- Basic CLI or GUI interface to chat

---

🚀 Getting Started

1. Clone the Repository

```bash
git clone https://github.com/ShreeVinaya123/Corona_ChatBot_Project.git
cd Corona_ChatBot_Project
```

2. Install Dependencies

Create and activate a virtual environment (optional but recommended), then install packages:

```bash
pip install -r requirements.txt
```

3. Train the Chatbot

```bash
python Corona_ChatBot.py
```

4. Chat with the Bot

```bash
python chatbot_interface.py
```

---

🧠 How It Works

1. **Data Preprocessing:** Load data from `intents.json`, tokenize, lemmatize, and vectorize patterns.
2. **Model Training:** Train a neural network model to classify input text into one of the predefined intents.
3. **Response Generation:** Once the model predicts the intent, a random response from that tag is returned.

---

📦 Files to Include

- `intents.json`
- `Corona_ChatBot.py`
- `chatbot_interface.py` or `gui_bot.py`
- `chatbot_model.h5`
- `words.pkl`, `classes.pkl`
- `README.md`
- `requirements.txt`

❌ Do **NOT** include: `.venv`, `__pycache__`, `*.tflearn.*` (if unused)

---

📄 License

This project is shared for educational purposes and personal learning. Free to use and modify.

---

🙏 Acknowledgements

- TensorFlow & Keras
- NLTK for NLP
- Inspired by chatbot training tutorials and educational datasets
