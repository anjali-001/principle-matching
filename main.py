import speech_recognition as sr
from transformers import pipeline
import pandas as pd

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

principles = ["Build Fast, Fail Fast", "Customer First", "Collaboration", "Continuous Improvement"]

# Function to map the description to the best principle
def map_to_principle(description):
    result = classifier(description, principles)
    best_match = result['labels'][0] 
    score = result['scores'][0]
    return best_match, score

# Function to generate a detailed explanation
def generate_explanation(description, principle):
    explanations = {
        "Build Fast, Fail Fast": "Your work shows that you prioritize speed in delivering features, even if it means iterating quickly on failures.",
        "Customer First": "Your work indicates that you place customer needs at the forefront, focusing on delivering features that add value to the end-user.",
        "Collaboration": "Your contributions demonstrate effective teamwork and collaboration, working closely with others to deliver high-quality work.",
        "Continuous Improvement": "Your work reflects a mindset of continuous improvement, focusing on refining and optimizing features or processes."
    }
    return explanations.get(principle, "No explanation available.")

# Process multiple inputs (multiple feature descriptions)
def process_performance_review(features):
    performance_report = []
    
    for feature in features:
       
        best_principle, score = map_to_principle(feature)
    
        explanation = generate_explanation(feature, best_principle)
        
        performance_report.append({
            "Feature Description": feature,
            "Best Principle Match": best_principle,
            "Confidence Score": round(score * 100, 2),  # Convert score to percentage
            "Explanation": explanation
        })
    
    return performance_report

# Function to capture speech input for employee features
def get_employee_features_by_speech():
    employee_features = []
    recognizer = sr.Recognizer()
    
    print("Please speak the employee's features one at a time (say 'alright' when finished):")

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            try:
                # Recognize speech using Google Web Speech API
                feature = recognizer.recognize_google(audio)
                print(f"You said: {feature}")

                if feature.lower() == "alright":
                    break
                
                employee_features.append(feature)
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError:
                print("Sorry, the service is down or unavailable.")

    return employee_features

employee_features = get_employee_features_by_speech()


performance_review = process_performance_review(employee_features)

df = pd.DataFrame(performance_review)

df.to_csv('performance_review.csv', index=False)

print("Performance review saved to 'performance_review.csv'.")
