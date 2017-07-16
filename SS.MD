CentOS系统更换内核教程，更好的适配锐速破解版 - 续笔记自媒体 https://xubiji.com/5505.html

下载更换内核
CentOS6 内核更换为：2.6.32-504.3.3.el6.x86_64



rpm -ivh http://soft.91zll.com/TOOLS/CentOS-Kernel/kernel-2.6.32-504.3.3.el6.x86_64.rpm
rpm -ivh http://soft.91zll.com/TOOLS/CentOS-Kernel/kernel-3.10.0-229.1.2.el7.x86_64.rpm --force

1
2
3
4
 
rpm -ivh http://soft.91zll.com/TOOLS/CentOS-Kernel/kernel-2.6.32-504.3.3.el6.x86_64.rpm
rpm -ivh http://soft.91zll.com/TOOLS/CentOS-Kernel/kernel-3.10.0-229.1.2.el7.x86_64.rpm --force
 
CentOS7 内核更换为： 3.10.0-229.1.2.el7.x86_64



rpm -ivh http://soft.91zll.com/TOOLS/CentOS-Kernel/kernel-firmware-2.6.32-504.3.3.el6.noarch.rpm --force

1
2
3
 
rpm -ivh http://soft.91zll.com/TOOLS/CentOS-Kernel/kernel-firmware-2.6.32-504.3.3.el6.noarch.rpm --force
 
查看内核是否安装成功


rpm -qa | grep kernel

1
2
3
 
rpm -qa | grep kernel

Vultr VPS安装破解版锐速提升网站/VPS主机速度 - Vultr中文网
http://www.cnvultr.com/276.html

wget -N --no-check-certificate https://raw.githubusercontent.com/91yun/serverspeeder/master/serverspeeder-all.sh && bash serverspeeder-all.sh

教你用VPS搭建自己的Shadowsock - 小狼的技术窝 - CSDN博客
http://blog.csdn.net/qq_19835843/article/details/52233111

ShadowsocksR一键安装脚本 - Shadowsocks非官方网站
https://shadowsocks.be/9.html