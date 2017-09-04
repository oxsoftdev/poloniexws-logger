import logging.config
import tornado
from poloniexws import Client as Websocket

import lib.configs.logging
from lib.subscribers import SimpleLoggerSubscriber


logging.config.dictConfig(lib.configs.logging.d)


if __name__ == '__main__':
    channels = ['BTC_ETC']
    with Websocket(channels) as client:
        with SimpleLoggerSubscriber(client):
            client.connect()
            try:
                tornado.ioloop.IOLoop.instance().start()
            except KeyboardInterrupt:
                client.close()

