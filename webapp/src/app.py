# -*- coding: utf-8 -*-
# @Time    : 18-6-12 下午9:00
# @Author  : unicoe
# @Email   : unicoe@163.com
# @File    : app.py
# @Software: PyCharm Community Edition


# python3.6 -m pip install aiohttp

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time

from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>welcome</h1>')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started!')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()