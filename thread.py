from PyQt4 import QtGui
import sys
import design
import urllib2
import json
import time

class ThreadingTutorial(QtGui.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.btn_start.clicked.connect(self.start_getting_top_posts)

    def _get_top_post(self, subreddit):
        url = "https://www.reddit.com/r/{}.json?limit=1".format(subreddit)
        headers = {'User-Agent': 'nikolak@outlook.com tutorial code'}
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        data = json.load(response)
        top_post = data['data']['children'][0]['data']
        return "'{title}' by {author} in {subreddit}".format(**top_post)

    def _get_top_from_subreddits(self,subreddits):
        for subreddit in subreddits:
            yield self._get_top_post(subreddit)
            time.sleep(2)

    def start_getting_top_posts(self):
        subreddit_list = str(self.edit_subreddits.text()).split(',')
        if subreddit_list == ['']:
            QtGui.QMessageBox.critical(self, "No subreddits",
                                       "You didn't enter any subreddits.",
                                       QtGui.QMessageBox.Ok)
            return

        self.progress_bar.setMaximum(len(subreddit_list))
        self.progress_bar.setValue(0)
        for top_post in self._get_top_from_subreddits(subreddit_list):
            self.list_submissions.addItem(top_post)
            self.progress_bar.setValue(self.progress_bar.value()+1)


def main():
    app = QtGui.QApplication(sys.argv)
    form = ThreadingTutorial()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()