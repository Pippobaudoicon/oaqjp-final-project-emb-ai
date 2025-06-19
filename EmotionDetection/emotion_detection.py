import json
import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    try:
        response = requests.post(url, headers=headers, json=input_json, timeout=10)
        response.raise_for_status()
        response_json = response.json()

        emotion_predictions = response_json.get('emotionPredictions')
        if emotion_predictions and isinstance(emotion_predictions, list) and len(emotion_predictions) > 0:
            emotions = emotion_predictions[0].get('emotion', {})
        else:
            emotions = {}
        
        anger_score = emotions.get('anger', 0.0)
        disgust_score = emotions.get('disgust', 0.0)
        fear_score = emotions.get('fear', 0.0)
        joy_score = emotions.get('joy', 0.0)
        sadness_score = emotions.get('sadness', 0.0)

        emotion_values = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
        
        if not emotions or all(score == 0.0 for score in emotion_values):
            dominant_emotion = None
        else:
            emotion_scores_for_max = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            dominant_emotion = max(emotion_scores_for_max, key=emotion_scores_for_max.get)

        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None
