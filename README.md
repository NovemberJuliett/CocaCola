# Mentions VK

This script helps to receive statistics by some word or words mention in social network VKontakte (for example how often
people talk about Coca-Cola. 
You can choose the period for what you need the statistics.

## How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
## How to use

Firstly you should receive the service key following the instruction
[on this site](https://dev.vk.com/en/api/getting-started). Then you should create .env file in your project directory
(or in the root of your project).

Create new variable in the same .env file and put your service key here. For example:

```python 
SERVICE_KEY ="put_your_key_here"
```
## Run

Open a new terminal window and run the script:

```python
python3 main.py
```