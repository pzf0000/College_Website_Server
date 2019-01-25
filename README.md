# 计算机学院院网
## 序言
本项目是中南大学计算机学院院网。  
在该项目中使用的主要技术有：
- Django：一个基于python的web开发框架
- Nameko：一种基于python的微服务开发框架  
- PostgreSQL：一种开源数据库，适用于高并发，同时支持NoSQL特性

该项目使用的python 3.6版本应该在3.6及以上。  
该项目使用的Django版本应该为2.0，
截至目前为止，Django Filters模块暂时不支持Django2.1版本，
因此不建议使用最新版本的Django.
## 项目的目录结构说明
- apps：由于要使用微服务架构，所以必然会产生很多的app，为方便管理，统一存放到此目录
- CollegeWebsiteServer：Django工程根目录，[其中settings文件夹是针对不同场景下的配置文件](CollegeWebsiteServer/settings/README.md)
- docs：项目文档，文件夹中包括[技术学习教程](docs/TechnicalLearningCourse/Catalog.md)、各个模块的设计文档，在各个模块的代码内部也会有必要的文档
- templates：模板文件，包含整个项目所需要的模板文件，各个ap也有自己的模板文件夹
## 项目开发目的
- 制作一个新的学院院网
- 为软件学院科协成员提升技能的项目
- 为高校二级学院门户网站提供样板
## 本项目的其他特点
- 该项目也可以用于其他高校其他学院的二级学院门户网站，本项目允许非商业性使用，但使用时请注明来源
- 虽然本项目的主题是Django，但实际上绝大部分的功能都将采用微服务架构，因此可以根据实际需要进行拓展
## 其他的重要说明
本项目采用python作为主要开发语言
## 使用mysql
如果你需要使用mysql，在配置完mysql之后，还需要安装mysqlclient，
这个模块的安装经常失败，因此请按照一下方法完成：  
首先，访问[网站](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python)，
然后，你需要根据自己python的版本下载相应的whl文件，使用命令行手工进入下载目录，执行`pip install`命令完成安装。
## 最后的特别提醒
python是一个灵活的语言，但是这也给他的架构设计带来了不小的挑战。
我们通过多次的论证，得到了当前的项目，因此，如果你没有阅读过python底层源码，
或不熟悉python的运行特点，不建议你修改本项目的基本架构。  
若你已经对python了如指掌，我们欢迎你提出更好的架构设计建议，并对该项目进行重构。

