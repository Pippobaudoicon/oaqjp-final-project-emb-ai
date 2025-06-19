import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy_emotion(self):
        statement = "I am glad this happened"
        expected_dominant_emotion = "joy"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)

    def test_anger_emotion(self):
        statement = "I am really mad about this"
        expected_dominant_emotion = "anger"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)

    def test_disgust_emotion(self):
        statement = "I feel disgusted just hearing about this"
        expected_dominant_emotion = "disgust"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)

    def test_sadness_emotion(self):
        statement = "I am so sad about this"
        expected_dominant_emotion = "sadness"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)

    def test_fear_emotion(self):
        statement = "I am really afraid that this will happen"
        expected_dominant_emotion = "fear"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)

if __name__ == '__main__':
    unittest.main()
