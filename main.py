import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world! This is edited.')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)