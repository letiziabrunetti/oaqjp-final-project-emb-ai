import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        dominantEmotion = 'joy'
    elif response.status_code == 500:
        anger_score = none
        disgust_score = none
        fear_score = none
        joy_score = none
        sadness_score = none
        dominantEmotion = none

    return { 'anger_score': anger_score, 'disgust_score': disgust_score, 'fear_score': fear_score,'joy_score': joy_score, 'sadness_score': sadness_score, 'dominantEmotion': dominantEmotion }