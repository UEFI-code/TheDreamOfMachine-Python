import random
import model

word_listA = ['What', 'How', 'Why', 'When', 'Where', 'Who']
word_listB = ['is', 'are', 'was', 'were', 'do', 'does', 'did', 'have', 'has', 'had', 'can', 'could', 'may', 'might', 'must', 'shall', 'should', 'will', 'would', 'need', 'ought', 'dare', 'need', 'used', 'use', 'using', 'used', 'like', 'liked', 'liking', 'likes', 'love', 'loved', 'loving', 'loves', 'hate', 'hated', 'hating', 'hates', 'want', 'wanted', 'wanting', 'wants', 'need', 'needed', 'needing', 'needs', 'know', 'knew', 'knowing', 'knows', 'think', 'thought', 'thinking', 'thinks', 'feel', 'felt', 'feeling', 'feels', 'believe', 'believed', 'believing', 'believes', 'understand', 'understood', 'understanding', 'understands', 'remember', 'remembered', 'remembering', 'remembers', 'forget', 'forgot', 'forgetting', 'forgets', 'see', 'saw', 'seeing', 'sees', 'look', 'looked', 'looking', 'looks', 'hear', 'heard', 'hearing', 'hears', 'listen', 'listened', 'listening', 'listens', 'smell', 'smelled', 'smelling', 'smells', 'taste', 'tasted', 'tasting', 'tastes', 'touch', 'touched', 'touching', 'touches', 'find', 'found', 'finding', 'finds', 'get', 'got', 'getting', 'gets', 'come', 'came', 'coming', 'comes', 'go', 'went', 'going', 'goes', 'walk', 'walked', 'walking', 'walks', 'run', 'ran', 'running', 'runs', 'sit', 'sat', 'sitting', 'sits', 'stand', 'stood', 'standing', 'stands', 'lie', 'lay', 'lying', 'lies', 'lay', 'laid', 'lying', 'lies', 'put', 'put', 'putting', 'puts', 'keep', 'kept', 'keeping']
word_listC = ['a', 'an', 'the', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'this', 'that', 'these', 'those', 'some', 'any', 'all', 'both', 'each', 'few', 'many', 'most', 'other', 'another', 'such', 'no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'last', 'next', 'new', 'old', 'good', 'well', 'bad', 'little', 'much', 'many', 'few', 'other', 'another', 'same', 'such', 'enough', 'long', 'short', 'large', 'high', 'far', 'near', 'right', 'left', 'big', 'small', 'large', 'great', 'small', 'young', 'old', 'early', 'late', 'first', 'last', 'long', 'short', 'late', 'early', 'hard', 'fast', 'full', 'low', 'light', 'heavy', 'strong', 'heavy', 'big', 'small', 'large', 'great', 'small', 'young', 'old', 'early', 'late', 'first', 'last', 'long', 'short', 'late', 'early', 'hard', 'fast', 'full', 'low', 'light', 'heavy', 'strong', 'heavy', 'big', 'small', 'large', 'great', 'small', 'young', 'old', 'early', 'late', 'first', 'last', 'long', 'short', 'late', 'early', 'hard', 'fast', 'full', 'low', 'light', 'heavy', 'strong', 'heavy', 'big', 'small', 'large', 'great', 'small', 'young', 'old', 'early', 'late', 'first', 'last', 'long', 'short', 'late', 'early', 'hard', 'fast', 'full', 'low', 'light', 'heavy', 'strong', 'heavy']
word_listD = ['human', 'computer', 'robot', 'room', 'ghost', 'Machine Learning', 'Deep Learning', 'Hacker']

the_model = model.theModel()

while True:
    theQuestion = random.choice(word_listA) + ' ' + random.choice(word_listB) + ' ' + random.choice(word_listC) + ' ' + random.choice(word_listD) + '?\n'
    theAnswer = the_model.talk(theQuestion)
    print('The model answered: %s' % theAnswer)



