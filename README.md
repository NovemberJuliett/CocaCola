# VK Mentions 

This script extracts VKontakte statistics for specified keywords, enabling you to monitor discussions.
You can customize the time period for analysis.

## How to install

Python3 should be already installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
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

Open a new terminal window and run the script with a desirable number of days. For example:

```python
python main.py --number_of_days 8
```