# 0x00 前言

大雨在家找点事情做，但其实不下雨我也还是在家，只是今天想找点事情做罢了，从过年前听着老爸说想换个电脑再配个显示器，可这都六月多了还是拿着这台旧电脑上网，还好只是浏览浏览网页，旧电脑确实还是可以顶得住，当然这可能是因为我给上了Ubuntu系统，换成原本的Windows系统早就是鼠标点一下能卡两下了，话不多说我直接乘着老爸上网的时候看能不能渗透成功，要是成功那我可就帮帮老爸下这个决心了🐕

# 0x01 主机发现

首先得知道老爸的IP，虽然我可以直接走过去当着老爸的面查一下，但我这毕竟还是在模拟真正的黑客入侵，这么做不太好吧🐱，都连着一个WiFi在同一个网段

看看我的物理机IP是192.168.31.94，那么我需要扫描的就是192.168.31.0/24这个网段咯，所以需要先修改虚拟机内kali的IP，先将原本所使用的VMnet8（NAT模式）更换为VMnet0（桥接模式），然后修改kali的网卡配置文件，配置了一个静态IP为192.168.31.77

ok，进行扫描

问题：怀疑是家中的老电脑，本身没有无线适配器，是安装的无线信号接收器，关闭物理机和老电脑的防火墙还是ping不通😥



