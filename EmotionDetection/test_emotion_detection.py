from emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase): 
    def test_emotion_detector(self):
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominantEmotion'], 'joy')
        result_1 = emotion_detector("I am really mad about this")
        self.assertEqual(result_1['dominantEmotion'], 'anger')
        result_1 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_1['dominantEmotion'], 'disgust')
        result_1 = emotion_detector("I am so sad about this")
        self.assertEqual(result_1['dominantEmotion'], 'sadness')
        result_1 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_1['dominantEmotion'], 'fear')

unittest.main()