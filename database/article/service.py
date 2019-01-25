import easy.database.urls
from models import models as dependences
from easy.database.service.rpc import RPCServiceModel


class ArticleService(RPCServiceModel):
    name = "article"
    __dependence__ = dependences.Article


if __name__ == '__main__':
    import os
    os.system("nameko run service")
