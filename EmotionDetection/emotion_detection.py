import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotion['anger']
        disgust_score = emotion['disgust']
        fear_score = emotion['fear']
        joy_score = emotion['joy']
        sadness_score = emotion['sadness']
        dominant_emotion_score = float('-inf')
        dominant_emotion_name = None
        for key, value in emotion.items():
            if(dominant_emotion_score < value):
                dominant_emotion_name = key
                dominant_emotion_score = value
    elif response.status_code == 500 or response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion_name = None

    return { 'anger_score': anger_score, 'disgust_score': disgust_score, 'fear_score': fear_score,'joy_score': joy_score, 'sadness_score': sadness_score, 'dominantEmotion': dominant_emotion_name }