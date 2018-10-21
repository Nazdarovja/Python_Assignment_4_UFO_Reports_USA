# from textblob import TextBlob

# def sentiment_calc(text):
#     """
#     Help method that creates sentiment analasys on a textline, or sets the values to neutral if values are malformed
#     """
#     try:
#         return TextBlob(text).sentiment
#     except:
#         #If string is malformed or empty, we change it to neutral.
#         return (0.0,0.0)