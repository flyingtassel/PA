# vultr牌梯子搭建手记

---
>本文阅读需要一定的耐心和基础网络知识，以及不找作者帮忙的觉悟。建议初级学徒在周末用甜食配合下肚，以免脑细胞缺乏糖分大量罢工。

这年头想找一个合适的梯子并不容易，尤其对于我这样只为了看个速度OK的油管汤不热之类的需求，买现成的服务商产品往往要被QoS限速，有经验的老司机都知道，SS这玩意跟网游SF也差不太多，只要主机数量固定，随着用户越来越多，姿势再多也没用，高峰期翻起来肯定不爽。更别提如今大多数还有流量限制了。
在这样的情况下，使用一些现代魔法塑造梯子自用或者和小伙伴共享就成了有追求的老司机方案。你要做的就是准备好信用卡或者paypal，用脸或者肤色选一个和你使用的ISP相性较高的主机提供商，再怼几行前辈写好的咒文，就能召唤出一只不错的梯子，顺带还可以获得不少初、中级现代魔法经验值，何乐而不为呢。

* 注意：本文采用当前（2017年7月）口碑和体验都比较出众的老牌厂商[Vultr](http://www.vultr.com/?ref=7186807)作为基础施法材料。其他厂家出品的材料也类似，请自行摸索。

* 本文需要一定的PC网络和软件基础知识，实现环境为windows。自己搞不定请千万不要找作者吐槽，找个阿宅男朋友什么的比较快。

[TOC]

## 1.开始搭梯子前的准备工作

### 理解SS的工作原理

```mermaid

graph LR
    你的墙内设备-->B["梯子(装好shadowsocks的VPS)"];
    B["梯子(装好shadowsocks的VPS)"]-->墙外网站;
    墙外网站-->B["梯子(装好shadowsocks的VPS)"];
    B["梯子(装好shadowsocks的VPS)"]-->你的墙内设备;
```

简单来说就是这样，所以你在召唤梯子的时候，首先要有一个身处墙外的VPS（Virtual Private Server 虚拟专用服务器）作为施法材料。所以一般来说这个时候就只有找老外买买买了。

### 软件准备

* 现代化浏览器，推荐chrome系的各种国产非国产，建议还是找个有按钮能直接点开应用商店的，方便翻墙安装SwitchyOmega这样的扩展插件测试翻墙效果。
* 一个能用SSH连接远程主机的客户端软件，方便操作VPS。如果你不知道这是什么东西又没有听说过Putty什么的，那么我建议你还是点击链接下一个本文中使用的[Xshell](https://www.portablesoft.org/xshell/)。
* [Shadowsocks windows](https://github.com/shadowsocks/shadowsocks-windows/releases)，基于C#，目前最新版本4.04。翻墙用PC客户端。也有同学可能已经用上了SSR（~~并不是金闪闪的那种卡片~~），但本文并没有采用SSR的服务器端。
* [安卓](https://github.com/shadowsocks/shadowsocks-android)或者[IOS](https://github.com/herzmut/shadowsocks-iOS)客户端，请自行研究。

### 购物准备

* 有效的信用卡或者paypal
* 不随便傲娇吞噬外网邮件的邮箱

[Vultr](http://www.vultr.com/?ref=7186807)前段时间的新用户优惠力度还是很大的，不过本文没赶上，如果有兴趣可以自行放狗找一找优惠码之类，比如[Vultr中文网](http://www.cnvultr.com/youhui/)，据说曾经有新用户薅羊毛薅出100刀……

### 注册Vultr帐号

看过优惠之后无论是薅到了更多的羊毛，还是感觉身体被掏空感觉错过了几个亿，你都可以在捂住自己钱包的同时[点击为本文多续一秒](http://www.vultr.com/?ref=7186807)，让本文作者获得$10的额外魔力。Vultr的注册简单至极，主页上那两个框框填上邮箱和密码一按按钮，再去邮箱确认就完事了，相比国内动不动就要你交出手机号来省事得多。唯一需要注意的是，账户密码必须至少10个字符，并包含至少1个小写字母，1个大写字母和1个数字。

以下图片摘自[板瓦工Vultr介绍](http://www.bawagon.com/vultrvps/)，如果不太熟悉此类流程建议直接看这篇文章。
![借用图片](http://img.bawagon.com/uploads/2016/06/2016629.png)

### 支付相关

验证完成后，登录网站会直接进到billing页面，填写支付信息扣款。
**神马**！你说这老外网站居然不给试用帐号也没有**屠龙宝刀点击就送**？那还是抬头看墙头草是不是又长了比较合适。
其实我觉得vultr这种老牌商家国内客户那么多，完全可以学某蒸汽把支付宝银联微信都搞起来啊。但是现在没有，所以担心信用卡安全问题的还是选paypal吧。有关paypal的问题请自行搜索解决。

![借用图片](http://img.bawagon.com/uploads/2016/04/4701-1.png)

目前图中的优惠已经没有了。另外建议充值金额$10起，防止你羊毛没有薅到反被误判恶意使用……

## 2.搭建VPS环境

**给了钱之后就是大爷了！** 快快创建一个自己的~~Servant~~服务器来玩玩吧

登录vultr后，点击所有页面右上角都有的那个圆圆的蓝色“+”号![按钮](http://img.bawagon.com/uploads/2015/06/3206.png)即可开始召唤：

本文试验后的服务器配置为tokyo机房效果最好，但是现在没有$2.5/M的配置了……无奈选了1T流量的版本，系统选了比较流行的CentOS，6.x和7.x均可，单单用于搭梯子差别不大。其他选项的勾都可以不点，最后一行起个好听的名就行，比如Saber、Lancer什么的。
选好之后点击Deploy Now，等待一两分钟让vultr把大爷您定制的服务器调教好即可开始奇幻之旅。

![借用](http://img.bawagon.com/uploads/2015/06/3207.jpg)
![借用](http://img.bawagon.com/uploads/2015/06/3208.png)
![借用](http://img.bawagon.com/uploads/2015/06/3211.png)

当servers这一页上显示你刚刚设定的服务器status已经从installing变成running之后，就可以尝试和这只Saber沟通了。

点击服务器名字进入详情页面，需要你记录的是IP、username和password。password点那个眼睛图标才会显示，其实不用看，只要点右边的copy图标就会进入剪贴板了。到此vultr网站上的操作基本完成。
![借用](http://img.bawagon.com/uploads/2015/06/3210.png)

### 连接VPS

打开Xshell，新建会话，名称就决定是**Saber**了！
![2017718153213](http://obkip5m5x.bkt.clouddn.com/2017718153213.png)

然后是用户身份验证，填上用户名密码。

![201771815367](http://obkip5m5x.bkt.clouddn.com/201771815367.png)

连接成功的话，就会出现你可以开始操作的#号。

![2017718153829](http://obkip5m5x.bkt.clouddn.com/2017718153829.png)

接下来的部分虽然是用了一键部署这种无脑操作，不过可能对新手还是有些难度了，请时不时的参考秋水逸冰大大的[这篇文章](https://teddysun.com/342.html)。

### 安装SS服务端

复制以下代码，然后在Xshell中按`Shift+Ins`后回车。

```centos

wget --no-check-certificate -O shadowsocks.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh
chmod +x shadowsocks.sh
./shadowsocks.sh 2>&1 | tee shadowsocks.log

```

接下来屏幕会翻滚一些你根本看不懂的玩意，然后会让你依次输入PC客户端用到的自定义端口号和密码，我想能看到这里的人大概都知道port和password两个英文单词啥意思。新手需要注意的是，输密码请一气呵成，不然就要准备学linux基础操作了，详见后文。
成功后大概如下图：

![2017718155333](http://obkip5m5x.bkt.clouddn.com/2017718155333.png)

这时候，你就可以点开SS windows客户端实验了。有关客户端的使用方法本文不在赘述，总之我们现在搞出来的是单用户系统，有IP、端口号和密码，加密方法默认是`aes-256-cfb`，你现在应该可以尝试着上梯子了。

---

**要求不高的用户请看到这里为止**

---

啊？你问接下来服务器还要干啥？当然是不眠不休的为你工作了，只要你vultr账户里还有美刀，它就会每个小时扣一次钱。所以能用就用吧，不要和美刀过不去。

### VPS加速

vultr东京机房速度还是不错的，基本上不采取特殊姿势直接翻起来youtube也能有几百K/s的下载速度，720p随便拖动无压力，但是1080p就容易缓冲了。所以还需要给服务器装个更加能搞事的东西来加快连接速度。实现的方法也很有几种，本文选取了同样有一键部署命令的锐速，个人（ISP：帝都联通）使用后效果拔群，youtube视频流速度提升一倍有余。

* 阅读接下来的部分时，请随时参考[这篇文章](https://www.91yun.org/archives/683) 以及[这篇文章](https://www.91yun.co/archives/795)

尤其是后面一篇，因为当你选择vultr服务器时，无论是CentOS6.x还是7.x，内核都已经比我们接下来要用的脚本新了，需要想办法换成能脚本能接受的版本才行。具体操作文内很详细，不赘述了。

CentOS版本都记不得了的，请看下图自寻，忘记圈出来了。
![2017718203248](http://obkip5m5x.bkt.clouddn.com/2017718203248.png)

如果你按照说明一路换完内核也`reboot`了，应该就会断开和VPS的连接，站起来上个厕所或者倒杯咖啡，用`Xshell`重新连接上之后运行`uname -r`，对比版本符合文中要求了，就可以直接复制以下代码，然后在Xshell中按`Shift+Ins`后回车运行即可，`Xshell`关了的就回头看看当初是用什么手段进入Saber酱的身体的吧。

```Linux
wget -N --no-check-certificate https://raw.githubusercontent.com/91yun/serverspeeder/master/serverspeeder-all.sh && bash serverspeeder-all.sh
```

这个脚本里用的是破解版锐速，没有什么需要设置的部分，耐心等待即可。由于两者版本实际上不是完全对应的，最后一般会给你2-3个贴近的可运行版本选择，输入对应数字即可。

最终成功的话，应该是这样的：
![2017718161940](http://obkip5m5x.bkt.clouddn.com/2017718161940.png)

是不是觉得少了些什么？对！你之前把VPS重启了，我们用的脚本又没有设定它开机自启动，SS服务端自然也就休息了，参考下面的部分，再来条命令把它怼回来。

#### 常用SS服务端命令

启动：`/etc/init.d/shadowsocks start`
停止：`/etc/init.d/shadowsocks stop`
重启：`/etc/init.d/shadowsocks restart`
状态：`/etc/init.d/shadowsocks status`

#### 常用锐速服务端命令

启动锐速：`/serverspeeder/bin/serverSpeeder.sh start`
停止锐速：`/serverspeeder/bin/serverSpeeder.sh stop`
卸载：`./serverSpeederInstaller.sh uninstall`
状态：`service serverSpeeder status`
更新锐速授权：`/serverspeeder/bin/serverSpeeder.sh renewLic`
最后一条一般用不上，因为装好之后一般都有效期十几年。

