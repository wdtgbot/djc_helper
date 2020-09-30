import datetime
import threading

import win32con
import win32gui

from log import logger, color


def uin2qq(uin):
    return str(uin)[1:].lstrip('0')


def maximize_console():
    threading.Thread(target=maximize_console_sync, daemon=True).start()


def maximize_console_sync():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)


def printed_width(msg):
    return sum([1 if ord(c) < 128 else 2 for c in msg])


def padLeftRight(msg, target_size, pad_char=" "):
    msg = str(msg)
    msg_len = printed_width(msg)
    pad_left_len, pad_right_len = 0, 0
    if msg_len < target_size:
        total = target_size - msg_len
        pad_left_len = total // 2
        pad_right_len = total - pad_left_len

    return pad_char * pad_left_len + msg + pad_char * pad_right_len


def tableify(cols, colSizes, delimiter=' '):
    return delimiter.join([padLeftRight(col, colSizes[idx]) for idx, col in enumerate(cols)])


def show_head_line(msg, msg_color=None):
    char = "+"
    line_length = 80

    # 按照下列格式打印
    # +++++++++++
    # +  test   +
    # +++++++++++
    if msg_color is None:
        msg_color = color("fg_bold_green")
    logger.warning(char * line_length)
    logger.warning(char + msg_color + padLeftRight(msg, line_length - 2) + color("WARNING") + char)
    logger.warning(char * line_length)


def get_this_week_monday():
    now = datetime.datetime.now()
    monday = now - datetime.timedelta(days=now.weekday())
    return monday.strftime("%Y%m%d")


def get_today():
    now = datetime.datetime.now()
    return now.strftime("%Y%m%d")


if __name__ == '__main__':
    print(get_today())
