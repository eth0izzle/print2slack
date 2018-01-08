import os, sys, json, urllib2
import threading

_stdout, _stderr = sys.stdout, sys.stderr


class SlackPrinter:
    def __init__(self):
        try:
            self.url = os.environ["SLACK_WH"]
        except KeyError:
            _stdout.write("SLACK_WH is not set!")

    def write(self, text):
        threading.Thread(target=self.__send, kwargs=dict(text=text)).start()

    def __send(self, text):
        req = urllib2.Request(self.url, json.dumps({"text": text}), headers={"Content-Type": "application/json"})
        urllib2.urlopen(req)


sys.stdout = SlackPrinter()
