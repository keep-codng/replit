from gtts import gTTS
import os

text = "Om Namah Shivay"
language = "hi"  # replaced en with hi

speech = gTTS(text=text, lang=language, slow=False)
speech.save("output.mp3")
os.system("start output.mp3")
