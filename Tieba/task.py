#
# @author haooon
# basic class task
#
import time
import os


class Task:
    name = ''
    complete_message = ''
    error_message = ''
    warning_message = ''

    def set(self, name, messages):
        self.name = name
        self.complete_message = messages['complete_message']
        self.error_message = messages['error_message']
        self.warning_message = messages['warning_message']

    def __get_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    def write_log(self, type, *args):
        f = open(os.path.dirname(os.path.realpath(__file__)) + '/mainlog.log', 'a')
        space = ' ' + '\t'
        if type == 'complete':
            f.write('complete' + space +
                  self.name + space +
                  str(self.__get_time()) + space +
                  self.complete_message.format(*args)
                    + '\n'
                  )
        if type == 'warning':
            f.write('warning' + space +
                  self.name + space +
                  str(self.__get_time()) + space +
                  self.warning_message.format(*args)
                    + '\n'
                  )
        if type == 'error':
            f.write('error' + space +
                  self.name + space +
                  str(self.__get_time()) + space +
                  self.error_message.format(*args)
                    + '\n'
                  )
