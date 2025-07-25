from sense_hat import SenseHat

bot = SenseHat()

# [245, 224, 220]  # Rosewater
# [205, 214, 244] # Text
O = [30, 30, 46] # Base
X = [180, 190, 254]  # Lavender

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

bot.set_rotation(180)
bot.set_pixels(question_mark)
