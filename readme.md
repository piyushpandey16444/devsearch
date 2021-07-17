1). create notification app. 2) create two new files - consumers.py and routing.py
3). Since went to use django channels and web sockets - need to with from wsgi to asgi..

> built in django server -- wsgi.(doesn't support channels.)
> asgi servers like :- daphne, uvicorn.

4). dor switching from wsgi to asgi, install channels.
5). pip install channels --- ll install daphne.
6). add channels inside settings.py > installed apps add channels
7). Add channel layer also in settings.py.

> It is used to control or govern channels, stores details of groups and channels. --> Need reddis for this.
