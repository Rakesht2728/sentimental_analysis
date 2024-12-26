from django.shortcuts import render
from textblob import TextBlob

def index(request):
    sentiment = ''
    polarity = 0.0
    subjectivity = 0.0

    if request.method == 'POST':
        user_text = request.POST.get('text')
        if user_text:
            analysis = TextBlob(user_text)
            polarity = analysis.polarity
            subjectivity = analysis.subjectivity
            if polarity > 0:
                sentiment = 'Positive'
            elif polarity < 0:
                sentiment = 'Negative'
            else:
                sentiment = 'Neutral'

    return render(request, 'analyzer/index.html', {
        'sentiment': sentiment,
        'polarity': polarity,
        'subjectivity': subjectivity
    })
