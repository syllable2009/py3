Zookeeper 可以被用作注册中心。
Zookeeper 是 Hadoop 生态系统的一员。
构建 Zookeeper 集群的时候，使用的服务器最好是奇数台。

ZooKeeper 是一个典型的分布式数据一致性解决方案，分布式应用程序可以基于 ZooKeeper 实现诸如数据发布/订阅、负载均衡、命名服务、分布式协调/通知、集群管理、Master 选举、分布式锁和分布式队列等功能。
ZooKeeper 一个最常用的使用场景就是用于担任服务生产者和服务消费者的注册中心。
ZooKeeper 中 Leader 选举算法采用了 Zab 协议(
只有一台leader负责处理外部客户端的事物请求(或写操作)，然后leader服务器将客户端的写操作数据同步到所有的follower节点中。
在ZAB协议中，只要超过半数follower节点反馈OK，Leader节点就会向所有的follower服务器发送commit消息。即将leader节点上的数据同步到follower节点之上。
ZAB协议中主要有两种模式，第一是消息广播模式；第二是崩溃恢复模式)。
Zab 核心思想是当多数 Server 写成功，则任务数据写成功：
如果有 3 个 Server，则最多允许 1 个 Server 挂掉。
如果有 4 个 Server，则同样最多允许 1 个 Server 挂掉。
既然 3 个或者 4 个 Server，同样最多允许 1 个 Server 挂掉，那么它们的可靠性是一样的。
所以选择奇数个 ZooKeeper Server 即可，这里选择 3 个 Server。

ZooKeeper 本身就是一个分布式程序（只要半数以上节点存活，ZooKeeper 就能正常服务）。
为了保证高可用，最好是以集群形态来部署 ZooKeeper，这样只要集群中大部分机器是可用的（能够容忍一定的机器故障），那么 ZooKeeper 本身仍然是可用的。
ZooKeeper 将数据保存在内存中，这也就保证了 高吞吐量和低延迟（但是内存限制了能够存储的容量不太大，此限制也是保持 Znode 中存储的数据量较小的进一步原因）
ZooKeeper 是高性能的。在“读”多于“写”的应用程序中尤其地高性能，因为“写”会导致所有的服务器间同步状态。（“读”多于“写”是协调服务的典型场景。）
ZooKeeper 有临时节点的概念。当创建临时节点的客户端会话一直保持活动，瞬时节点就一直存在。
而当会话终结时，瞬时节点被删除。持久节点是指一旦这个 ZNode 被创建了，除非主动进行 ZNode 的移除操作，否则这个 ZNode 将一直保存在 Zookeeper 上。
ZooKeeper 底层其实只提供了两个功能：①管理（存储、读取）用户程序提交的数据；②为用户程序提交数据节点监听服务。

Session 指的是 ZooKeeper  服务器与客户端会话。在 ZooKeeper 中，一个客户端连接是指客户端和服务器之间的一个 TCP 长连接。
客户端启动的时候，首先会与服务器建立一个 TCP 连接，从第一次连接建立开始，客户端会话的生命周期也开始了。
通过这个连接，客户端能够通过心跳检测与服务器保持有效的会话，也能够向 Zookeeper 服务器发送请求并接受响应，同时还能够通过该连接接收来自服务器的 Watch 事件通知。
Session 的 sessionTimeout 值用来设置一个客户端会话的超时时间。
当由于服务器压力太大、网络故障或是客户端主动断开连接等各种原因导致客户端连接断开时，只要在 sessionTimeout 规定的时间内能够重新连接上集群中任意一台服务器，那么之前创建的会话仍然有效。
在为客户端创建会话之前，服务端首先会为每个客户端都分配一个 sessionID。
由于 sessionID 是 Zookeeper 会话的一个重要标识，许多与会话相关的运行机制都是基于这个 sessionID 的。
因此，无论是哪台服务器为客户端分配的 sessionID，都务必保证全局唯一。

ZooKeeper 将所有数据存储在内存中，数据模型是一棵树（Znode Tree)，由斜杠（/）的进行分割的路径，就是一个 Znode，例如/foo/path1。每个上都会保存自己的数据内容，同时还会保存一系列属性信息。
在 Zookeeper 中，Node 可以分为持久节点和临时节点两类。所谓持久节点是指一旦这个 ZNode 被创建了，除非主动进行 ZNode 的移除操作，否则这个 ZNode 将一直保存在 ZooKeeper 上。
而临时节点就不一样了，它的生命周期和客户端会话绑定，一旦客户端会话失效，那么这个客户端创建的所有临时节点都会被移除。
另外，ZooKeeper 还允许用户为每个节点添加一个特殊的属性：SEQUENTIAL。
一旦节点被标记上这个属性，那么在这个节点被创建的时候，ZooKeeper 会自动在其节点名后面追加上一个整型数字，这个整型数字是一个由父节点维护的自增数字。
版本
在前面我们已经提到，Zookeeper 的每个 ZNode 上都会存储数据，对应于每个 ZNode，Zookeeper 都会为其维护一个叫作 Stat 的数据结构。
Stat 中记录了这个 ZNode 的三个数据版本，分别是：
version（当前 ZNode 的版本）
cversion（当前 ZNode 子节点的版本）
aversion（当前 ZNode 的 ACL 版本）

	stat path [watch] #stat path :获取指定节点的状态信息
	set path data [version] #set /zk shenlan211314
	ls path [watch] #ls path:查看某个节点下的所有子节点信息
	delquota [-n|-b] path
	ls2 path [watch] #列出path节点的子节点及状态信息
	setAcl path acl
	setquota -n|-b val path
	history
	redo cmdno
	printwatches on|off
	delete path [version] #创建的 znode 删除
	sync path
	listquota path
	rmr path
	get path [watch] #get /zk
	create [-s] [-e] path data acl  #使用 create -e /zk myData
	addauth scheme auth
	quit
	getAcl path
	close
	connect host:port
