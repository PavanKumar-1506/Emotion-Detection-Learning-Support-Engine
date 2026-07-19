# Emotion keywords

emotion_keywords = {

    "Confident": [
        "confident", "easy", "understand",
        "completed", "good", "excellent",
        "learned", "success"
    ],

    "Confused": [
        "confused", "don't understand",
        "unclear", "difficult",
        "question", "help", "why"
    ],

    "Curious": [
        "curious", "interesting",
        "want to know", "explore",
        "learn more", "how"
    ],

    "Frustrated": [
    "frustrated",
    "angry",
    "failed",
    "hard",
    "stress",
    "stressed",
    "problem",
    "problems",
    "worried",
    "error",
    "errors",
    "bug",
    "bugs",
    "issue",
    "issues",
    "stuck",
    "doesn't work",
    "not working",
    "unable",
    "can't",
    "cannot"
],

    "Bored": [
        "bored",
        "boring",
        "sleepy",
        "tired",
        "not interested"
    ]
}


def detect_emotion(text):

    text = text.lower()

    scores = {}

    for emotion, words in emotion_keywords.items():

        score = 0

        for word in words:

            if word in text:

                score += 1

        scores[emotion] = score

    best = max(scores, key=scores.get)

    if scores[best] == 0:

        return "Neutral"

    return best