brew 搜索软件
brew search nginx
brew 安装软件
brew install nginx
brew 卸载软件
brew uninstall nginx
brew 升级
sudo brew update
查看安装信息(经常用到, 比如查看安装目录等)
sudo brew info nginx
查看已经安装的软件
brew list

brew services start nginx
brew services stop nginx
nginx -s reload
nginx -s stop

正向代理和反向代理的区别是：代理的角色，正向代理代理访问外部资源，反向代理服务提供者