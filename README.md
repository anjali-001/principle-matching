# principle-matching
### A little backstory:
Not interested, [show me what did you use to build this](#built-this-using) or even the [Set up process](#follow-these-steps-to-set-it-up-locally) would work.

This is a little python script which I did to automate something I found tedious, matching which `work/feature I built/issue I resolved` matched which `princliple` at my workplace in a performance review. So I thought, this seems like a problem that should have a tool. 

Searched on google for this, could't find a tool. Then I thought, this should not be tough to build, let's try. I am anyway looking to learn ML, although using pre-built NLP model is not ML per say, however not bad for a starting point, right.

So, wrote a simple script which basically has a list of principles, and when the user inputs the work they have done, it will give you the most compatible principle it matches with and give the results on a CSV file.

But, if you have to write what you worked on, might as well manually find a principle that matches, right, what is the use for such a tool. So, I used PyAudio and the open-source library `speech-recognition` to have a speech to text input, where the user will just talk about what they worked on, rest of the work will be done by the script itself. And for some weird reason, it was unable to understand when I said "done", so the exit prompt would be saying `alright`. So, speak what you've worked on, later when you alright, the script will exit the matching loop and give the output in a csv file. 

I can think of various usecases where this can be useful, principle matching being one of them, might extend the list of usecases.

This is me trying to learn a bit more about NLP, long way to go and a lot to learn, will happily accept any contructive criticism and improvement to the code.

### Built this using: 

Used Hugging Face's `pipeline` for this, NLP technique `zero-shot-classification` and the `facebook/bart-large-mnli` model for text-classification. 


# Follow these steps to set it up locally: 

Step 1:
```
git clone https://github.com/anjali-001/principle-matching.git
```
```
cd principle-matching
```

Step 2:  Set Up a Virtual Environment
```
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```
Step 3: Activate the virtual environment
```
# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

Step 4: Install Dependencies
```
pip install -r requirements.txt
```
Step 5: Install PyAudio
```
pip install pyaudio
```
Step 6: Run script
```
 python main.py
```

Step 7: Deactivate the Virtual Environment :))
```
deactivate
```





Done! :,)
