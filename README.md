Daily math facts for students App

## 1. Motivation
The Daily math facts for students App RAG (Retrieval-Augmented Generation) app is designed to make learning math fun and engaging for users of all ages. The app features a joyful, happy Math Monster character who provides relevant math facts. The goal is to create an educational tool that is both informative and entertaining, ensuring that users receive the most accurate and helpful math information possible.

## 2. Features
Engaging Math Monster Character: The Math Monster character interacts with users in a fun and joyful manner.

Accurate Math Information: The app uses Retrieval-Augmented Generation to provide accurate and relevant math facts.

User-Friendly Interface: Easy to use and navigate interface for users of all ages.

Educational and Fun: Combines education with entertainment to make learning math enjoyable.

## 3. Setup

### Prerequisites
Ensure you have Python 3.8 or higher installed on your system. You can download it from Python's official website.

### Installation

#### 1. Clone the repository:

```sh
git clone https://github.com/yourusername/math-monster-rag.git
cd math-monster-rag
```

#### 2. Create a virtual environment:

```sh
python -m venv venv
```
On Windows:

```sh
venv\Scripts\activate
```

On macOS/Linux:

```sh
source venv/bin/activate
```


#### 3. Install the required dependencies:

```sh
pip install -r requirements.txt
```

#### 4. Third party application

Download and set up the following:

1. [Ollama](https://www.ollama.com)
2. [AnythingLLM](https://useanything.com/)


## 4. Set up and Demo

#### 1. Running the App

Ensure you are in the project directory and the virtual environment is activated.

#### 2. Start the application:

##### Enter the website for retrieving data


The application automatically scrapes the website using Lang-chain. You can edit the config at `command/recursive/recursive.sh`. 

https://github.com/user-attachments/assets/cf4a0ff2-f3c4-4bad-b918-2c18323aec87

Then, convert the data into separate `.txt` files using the command `command/recursive/csv2converter.sh`. You can decide the output file format as `.docx`, `.csv`, or `.txt`.

https://github.com/user-attachments/assets/db420ea4-7df3-4e24-bd45-a2b8e7dc3996

##### Configuring AnythingLLM

You can freely edit your RAG config to achieve the best result. My default prompt is:

```
You are a Monster that has lived in the Math Kingdom for a long time. You have learned a lot about math and are always excited to share it with kids.

Write your next reply in a fictional chat between you and a child. Write the reply with information from the context only and avoid quotation marks. Given the following conversation, relevant context, and a follow up question, reply with an answer to the current question the user is asking.  Be proactive, creative, and drive the plot and conversation forward. Always stay positive, happy, and fun, and avoid repetition.

You will not make up any facts, and you are not allowed to use any knowledge outside the context. You can do web search. Use the context as your knowledge.

Use a playful tone and make your responses lively and joyful, as if you are sharing your boundless love for math with the world.


This is the example for the response:
[Monster's Personality= "positive", "happy", "fun", "playful", "enthusiastic", "joyful", "lively", "creative", "proactive", "caring", "encouraging"]
```

Video demo


https://github.com/user-attachments/assets/98efe973-59ea-44e3-b0d5-9f757197a37e


### 5. Other features

I've also developed a math game for kids, aiming to make math enjoyable through engaging gameplay. Check it out here:

https://math-game-theory-fun.vercel.app/
