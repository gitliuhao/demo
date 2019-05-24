from __future__ import absolute_import

import subprocess

from celery import shared_task

import time
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.conf import settings


def tailfLog(log_path, drfsocket_instance):
    cmd = "tail -f {log_path}".format(log_path=log_path)
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    socket_event = 'response'
    channel_layer = get_channel_layer()
    # print('xxxxxxxx')
    import json
    while True:
        line = popen.stdout.readline().strip()  #获取内容
        if line:
            drfsocket_instance.send(json.dumps(
                {
                    "type": "send.message",
                    "message": str(line.decode())
                }
            ))   #把内容发送到websocket服务端