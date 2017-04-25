#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
    possibleFortunes = [
        "Ask your mother.",
        "When in anger, sing the alphabet.",
        "One day, you will be carbon neutral.",
        "A man with brown eyes has a surprise for you.",
        "Please play again.",
        "Avoid taking unnecessary gambles.",
        "How much deeper would the ocean be without sponges?",
        "When you squeeze an orange, orange juice comes out - because that is what's inside.",
        "You could come up with better fortunes than these.",
        "Fortune Not Found: Abort, Retry, Ignore?",
        "I cannot help you, I am but a cookie.",
        "Pigeon poop burns the retina for 13 hours. You will discover this the hard way."
    ]

    return possibleFortunes[random.randint(0,int(len(possibleFortunes)-1))]


class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fortune_sentence = "Your fortune: " + fortune
        fortune_para = "<p>" + fortune_sentence + "</p>"

        luckyNumber = "<strong>" + str(random.randint(1, 100)) + "</strong>"
        number_sentence = 'Your lucky number: ' + luckyNumber
        number_para = '<p>' + number_sentence + '</p>'

        anothercookie = "<a href='.'><button>Another?</button></a>"

        content = header + fortune_para + number_para + anothercookie

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
