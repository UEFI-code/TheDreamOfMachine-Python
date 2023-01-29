class theModel():
    def __init__(self, born='theChoosenZero'):
        self.born = born
        print('I born as %s' % self.born)

    def talk(self, in_text):
        response = input(in_text)
        try:
            return eval(response)
        except:
            return response
        