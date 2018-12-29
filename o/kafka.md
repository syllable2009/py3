Kafka是一个分布式的、可分区的、可复制的消息系统

Kafka将消息以topic为单位进行归纳。

将向Kafka topic发布消息的程序成为producers.

将预订topics并消费消息的程序成为consumer.

Kafka以集群的方式运行，可以由一个或多个服务组成，每个服务叫做一个broker.
![Image text](https://github.com/syllable2009/py3/raw/master/www/static/kafka-topic.png)
每个分区都由一系列有序的、不可变的消息组成，这些消息被连续的追加到分区中。分区中的每个消息都有一个连续的序列号叫做offset,用来在分区中唯一的标识这个消息。
在一个可配置的时间段内，Kafka集群保留所有发布的消息，不管这些消息有没有被消费。比如，如果消息的保存策略被设置为2天，那么在一个消息被发布的两天时间内，它都是可以被消费的。之后它将被丢弃以释放空间。
Kafka的性能是和数据量无关的常量级的，所以保留太多的数据并不是问题。

实际上每个consumer唯一需要维护的数据是消息在日志中的位置，也就是offset.这个offset由consumer来维护：一般情况下随着consumer不断的读取消息，这offset的值不断增加，
但其实consumer可以以任意的顺序读取消息，比如它可以将offset设置成为一个旧的值来重读之前的消息。

以上特点的结合，使Kafka consumers非常的轻量级：它们可以在不对集群和其他consumer造成影响的情况下读取消息。你可以使用命令行来"tail"消息而不会对其他正在消费消息的consumer造成影响。

将日志分区可以达到以下目的：首先这使得每个日志的数量不会太大，可以在单个服务上保存。另外每个分区可以单独发布和消费，为并发操作topic提供了一种可能。

mac
brew install kafka安装
brew reinstall kafka重装
安装目录：/usr/local/Cellar/kafka/0.10.2.0
安装的配置文件位置:
/usr/local/etc/kafka/server.properties
/usr/local/etc/kafka/zookeeper.properties
brew services start kafka启动
./bin/zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties 启动

需要zookeper
To have launchd start zookeeper now and restart at login:
  brew services start zookeeper
Or, if you don't want/need a background service you can just run:
  zkServer start
  配置 /usr/local/etc/zookeeper/zoo.cfg
  
创建topic:使用单个分区和只有一个副本创建一个名为“test”的topic
/usr/local/bin/kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

查看创建的topic
/usr/local/bin/kafka-topics --list --zookeeper localhost:2181

生产
/usr/local/bin/kafka-console-producer --broker-list localhost:9092 --topic test
XXX 

消费
/usr/local/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic test --from-beginning

