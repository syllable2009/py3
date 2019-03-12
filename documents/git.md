Linus的作者创建了开源的Linux，02年以前代码管理都依赖手动合并，后来管理不了了，拒绝SVN和CVS这些中央式版本控制的工具(原因如下表格)，
采用免费授权给Linux社区的BitKeeper工具，再后来05年社区的大牛要破解BitKeeper被人家公司发现要收回BitKeeper对Linux的免费的使用权，
Linus一口气两周内用C写了一个分布式的版本控制系统——Git。接着08年GitHub问世，利用Git为无数开源项目提供代码的托管存储

分布式版本控制系统：Git,BitKeeper

集中式版本控制系统：CVS,SVN


集中式（SVN）	分布式（Git）

#clone远程仓库、创建本地仓库
git clone https://github.com/****.git
clone项目到本地之后，我们可以看到目录下有一个叫.git的隐藏文件，
这个.git文件夹就是我们的本地仓库（Local Repository）.git文件夹所在的根目录就是我们的工作目录（Working Directory）
clone下来的项目我们就可以正常开发了，当然我们也可以在本地直接创建一个本地仓库，之后再与远程创建的仓库进行关联，先执行
git init
命令执行的目录下就有了一个.git文件夹，我们在创建了一个本地仓库，接着与远程仓库进行关联
git remote add origin https://github.com/****.git

新创建的文件要添加到暂存区——git add
暂存区（index/staging area）是指储存了所有待提交的改动的地方，只有在暂存区存在的文件，本地仓库才会追踪到它的变化。
把文件从暂存区提交到本地的版本库中——git commit
