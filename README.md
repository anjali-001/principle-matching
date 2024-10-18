# principle-matching
This is a little python script which I did to automate something I did not particularly enjoy, matching which `work/feature I built/issue I resolved` matched which `princliple` at my workplace in a performance review. So I thought, this seems like a problem that should have a tool. 

Searched on google for this, could't find a tool. Then I thought, this should not be tough to build, let's try. I am anyway looking to learn ML, although using pre-built NLP model is not ML per say, however not bad for a starting point, right.

So, wrote a simple script which basically has a list of principles, and when the user inputs the work they have done, it will give you the most compatible principle it matches with and give the results on a CSV file.

But, if you are writing what you did, might as well find a principle that matches, right, what is the use for that. So, I used PyAudio to have a speech to text input, where the user will just talk about what they works on, rest of the work will be done by the script itself. And for some weird reason, it was unable to understand when I said "done", so the exit prompt would be saying alright. So, speak what you've worked on, later when you alright, the script will cease the exit the matching loop and give the output in a csv file. 

I can think of various usecases where this can be useful, principle matching being on of them, might extend the list of usecases.

Used Hugging Face's `pipeline` for this, NLP technique `zero-shot-classification` and the `facebook/bart-large-mnli` model for text-classification. 

Done! :,)
