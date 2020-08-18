
import re

str = '''
<!doctype html>
<html class="expanded">
<head>

<!--STATUS OK-->
<meta http-equiv=Content-Type content="text/html;charset=utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">
<link rel="icon" href="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/img/favicon.ico" mce_href="../static/img/favicon.ico" type="image/x-icon">

<title>百度新闻——海量中文资讯平台</title>
<meta name="description" content="百度新闻是包含海量资讯的新闻服务平台，真实反映每时每刻的新闻热点。您可以搜索新闻事件、热点话题、人物动态、产品资讯等，快速了解它们的最新进展。" >
<script type="text/javascript">
		document.write("<script  type='text/javascript' src='//news-bos.cdn.bcebos.com/mvideo/pcconf_2019.js?"+new Date().getTime()+"'><\/script>");
	</script>
<script type="text/javascript"> window.NEWSLOGURL = 'https://log.news.baidu.com/v.gif'; window.HUNTERLOGURL = '//log.news.baidu.com/u.gif'; window._hmt = window._hmt || [];</script>
<script type="text/javascript" src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/resource/js/usermonitor_88a158c.js?v=1.2"></script>

<script src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/yule/js/jquery-1.8.3.min_a6ffa58.js" type="text/javascript"></script>

<link rel="stylesheet" type="text/css" href="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/module_static_include/module_static_include_6cb6a04.css"/><link rel="stylesheet" type="text/css" href="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/yule/yule/yule_392d506.css"/></head>
<body>
<div id="header-wrapper" class="clearfix">
<div id="usrbar" alog-group="userbar" alog-alias="hunter-userbar-start"></div>
<ul id="header-link-wrapper" class="clearfix">
<li><a href="https://www.baidu.com/" data-path="s?wd=">网页</a></li>
<li style="margin-left:21px;"><span>新闻</span></li>
<li><a href="http://tieba.baidu.com/" data-path="f?kw=">贴吧</a></li>
<li><a href="https://zhidao.baidu.com/" data-path="search?ct=17&pn=0&tn=ikaslist&rn=10&lm=0&word=">知道</a></li>
<li><a href="http://music.baidu.com/" data-path="search?fr=news&ie=utf-8&key=">音乐</a></li>
<li><a href="http://image.baidu.com/" data-path="search/index?ct=201326592&cl=2&lm=-1&tn=baiduimage&istype=2&fm=&pv=&z=0&word=">图片</a></li>
<li><a href="http://v.baidu.com/" data-path="v?ct=3019898888&ie=utf-8&s=2&word=">视频</a></li>
<li><a href="http://map.baidu.com/" data-path="?newmap=1&ie=utf-8&s=s%26wd%3D">地图</a></li>
<li><a href="http://wenku.baidu.com/" data-path="search?ie=utf-8&word=">文库</a></li>
<div class="header-divider"></div>
</ul>
</div>
<div id="app_tooltip_qrcode">
<img src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/img/sidebar/newErweima_9fa03e0.png">
</div>
<div id="headerwrapper">
<div id="header" alog-group="header" alog-alias="hunter-header-start">

<table class="sbox" id="sbox" alog-group="search-box">
<tr>
<td class="logo">
<div class="logo">
<a href="http://news.baidu.com/">
<!--[if !IE]><!--><img src="https://box.bdimg.com/static/fisp_static/common/img/searchbox/logo_news_276_88_1f9876a.png" alt="百度新闻" height="46px" width="137px"><!--<![endif]-->
<!--[if IE 6]><img src="https://box.bdimg.com/static/fisp_static/common/img/searchbox/logo_news_276_88_for_ie6_1597c18.png" alt="百度新闻" height="46px" width="137px"><![endif]-->
<!--[if gt IE 6]><img src="https://box.bdimg.com/static/fisp_static/common/img/searchbox/logo_news_276_88_1f9876a.png" alt="百度新闻" height="46px" width="137px"><![endif]-->
</a>
</div>
<div class="date"></div>
</td>
<td class="search">
<table>
<tr>
<td class="box"><div id="sugarea"><span class="s_ipt_wr" id="s_ipt_wr"><input class="word" id="ww" name="word" size="42"  maxlength="100" tabindex="1"></span><span class="s_btn_wr"><input class="btn" id="s_btn_wr" type="button" value="百度一下" onmousedown="this.className='btn s_btn_h'" onmouseout="this.className='btn'"></span></div></td>
<td class="help"><a href="//help.baidu.com">帮助</a></td>
</tr>
</table>
<p class="search-radios">
<input type="radio" name="tn" value="news" checked="checked" id="news">
<label for="news" class="checked">新闻全文</label>
<input type="radio" name="tn" value="newstitle" id="newstitle">
<label for="newstitle" class="not-checked">新闻标题</label>
</p>
<input type="hidden" name="from" id="from" value="news">
<input type="hidden" name="cl" id="cl" value="2">
<input type="hidden" name="rn" id="rn" value="20">
<input type="hidden" name="ct" id="ct" value="1">
</td>
</tr>
</table>

</div>

<div id="menu" class="mod-navbar" alog-group="entertainment-menu">
<div id="channel-shanghai" class="channel-shanghai clearfix"  style="display:none" >
<div class="menu-list">
<ul class="clearfix">
<li class="navitem-index "><a href="/">首页</a></li>
<li ><a href="/guonei">国内</a></li>
<li ><a href="/guoji">国际</a></li>
<li ><a href="/mil">军事</a></li>
<li ><a href="/finance">财经</a></li>
<li  class="current active"><a href="/ent">娱乐</a></li>
<li ><a href="/sports">体育</a></li>
<li ><a href="/internet">互联网</a></li>
<li ><a href="/tech">科技</a></li>
<li ><a href="/game">游戏</a></li>
<li ><a href="/lady">女人</a></li>
<li ><a href="/auto">汽车</a></li>
<li ><a href="/house">房产</a></li>
</ul>
</div>
<i class="slogan"></i>
</div>
<div id="channel-all" class="channel-all clearfix" >
<div class="menu-list">
<ul class="clearfix">
<li class="navitem-index "><a href="/">首页</a></li>
<li ><a href="/guonei">国内</a></li>
<li ><a href="/guoji">国际</a></li>
<li ><a href="/mil">军事</a></li>
<li ><a href="/finance">财经</a></li>
<li  class="current active"><a href="/ent">娱乐</a></li>
<li ><a href="/sports">体育</a></li>
<li ><a href="/internet">互联网</a></li>
<li ><a href="/tech">科技</a></li>
<li ><a href="/game">游戏</a></li>
<li ><a href="/lady">女人</a></li>
<li ><a href="/auto">汽车</a></li>
<li ><a href="/house">房产</a></li>
</ul>
</div>
<i class="slogan"></i>
</div>
</div>

</div>
<div id="body" alog-alias="b">

<script type="text/javascript">
        void function(e,t,n,a,o,i,m){e.alogObjectName=o,e[o]=e[o]||function(){(e[o].q=e[o].q||[]).push(arguments)},e[o].l=e[o].l||+new Date,i=t.createElement(n),i.asyn=1,i.src=a,m=t.getElementsByTagName(n)[0],m.parentNode.insertBefore(i,m)}(window,document,"script","https://img.baidu.com/hunter/alog.min.js","alog");
    </script>
<div class="column clearfix" id="col_toparea" alog-group="log-enternews-toparea">
<div class="toparea-carousel" alog-group="focussports-carousel">
<div class="imgplayer clearfix" id="imgplayer">
<div id="imgplayer-control">
<a href="javascript:void(0);" mon="col=carousel&pos=ctr_l&ct=1&pn=0" id="imgplayer-prev"></a>
<a href="javascript:void(0);" mon="col=carousel&pos=ctr_r&ct=1&pn=0" id="imgplayer-next"></a>
</div>
<div class="imgview" id="imgView">
<a href="javascript:void(0);" target="_blank"><img src="https://news.baidu.com/iphone/img/loading_3.gif" class="firstimg" alt=""></a>
</div>
<div class="imgnav-mask"></div>
<div class="imgnav" id="imgNav">
<a class="navbtn" index="3" mon="col=carousel&pos=dots&a=9pn=3" href="javascript:void(0);">3</a>
<a class="navbtn" index="2" mon="col=carousel&pos=dots&a=9pn=2" href="javascript:void(0);">2</a>
<a class="navbtn" index="1" mon="col=carousel&pos=dots&a=9pn=1" href="javascript:void(0);">1</a>
</div>
<div class="imgtit" id="imgTitle">
<a href="javascript:void(0);" target="_blank"></a>
</div>
</div>
</div>
<div class="l-right-col">
<div class="mod">
<div class="hd"><h3>即时新闻<span class="dec">INSTANT NEWS</span></h3></div>
<div class="bd">
<div id="instant-news">
<ul class="ulist mix-ulist">
<li><a href="http://baijiahao.baidu.com/s?id=1675264553436833716" class="title" target="_blank" mon="col=28&pn=1">肉嘟嘟的李尖尖，原来是当年的小葱花，易烊千玺：</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675264177763708260" class="title" target="_blank" mon="col=28&pn=2">老人养出千斤“猪王”，却因为一件“怪事”，商贩</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675264487457595041" class="title" target="_blank" mon="col=28&pn=3">《姜子牙》《夺冠》定档，网友爆哭</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675264191787881238" class="title" target="_blank" mon="col=28&pn=4">别再被表象欺骗了，蓝盈莹“鸡汤式”的努力，你学</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675263153973356179" class="title" target="_blank" mon="col=28&pn=5">刘亦菲拍戏最“大胆”的一次，罕见穿比基尼出镜，</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675263915104625174" class="title" target="_blank" mon="col=28&pn=6">看《这就是街舞》抢人，被王一博惊艳到只想大吼3</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675263200286562300" class="title" target="_blank" mon="col=28&pn=7">《元气满满的哥哥》：一次失败的“快综艺”改造</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675258755650504932" class="title" target="_blank" mon="col=28&pn=8">外媒：美国考虑封杀阿里？特朗普发布会可没这么说</a></li>
</ul>
</div>
</div>
</div>
</div>
</div><div class="column clearfix" id="col_focus" alog-group="log-enternews-focus" style="margin-top:25px">
<div class="l-left-col">
<div class="column-title" >
<div class="yule-column-title-border">
<h2><span class="subtitle">焦点新闻</span><span class="cname">FOCAL NEWS</span></h2>
</div>
</div><div class="b-left" >
<ul class="ulist "  >
<li class="bold-item"><a href="http://baijiahao.baidu.com/s?id=1675264860520729769" mon="col=1&amp;a=2&pn=1" target="_blank">生恩大还是养恩大？《以家人之名》五口之家引发网络热..</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1655436540741695026" mon="col=1&amp;a=2&pn=2" target="_blank">演讲紧张｜千场演讲经验的心理师，用五个字帮你搞定一..</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675232273512411935" mon="col=1&amp;a=2&pn=3" target="_blank">《以家人之名》虐心升级，家人关系日渐疏离，脱水收视..</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675068618857404569" mon="col=1&amp;a=2&pn=4" target="_blank">侏罗纪世界3片场照流出，惊现逼真恐龙，剧组需遵守1..</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675106625584310513" mon="col=1&amp;a=2&pn=5" target="_blank">留灯的神秘女子是谁？除了冻千秋，蓝轩宇终于有第二个..</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675199014284861724" mon="col=1&amp;a=2&pn=6" target="_blank">杰森·斯坦森，也只有他有那个底气嘲讽漫威电影是老奶..</a></li>
</ul>
<ul class="ulist " >
<li class="bold-item"><a href="http://baijiahao.baidu.com/s?id=1675241557130148625" mon="col=1&amp;a=2&pn=7" target="_blank">《街舞3》王一博队伍强，张艺兴被选手拒绝四连击，队..</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675235390591778367" mon="col=1&amp;a=2&pn=8" target="_blank">星太奇：挑战鬼故事大王？其实最恐怖的故事就是一句话</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675264272020129085" mon="col=1&amp;a=2&pn=9" target="_blank">“斑马死侍”，漫威画师口味到底有多奇特才能画出这一..</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675261548890823292" mon="col=1&amp;a=2&pn=10" target="_blank">泽塔奥特曼：人类妄图控制奥特曼？剧中早已暗示，F计..</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675184393260018163" mon="col=1&amp;a=2&pn=11" target="_blank">狗血老梗大集合，一样能暖到你哭，《以家人之名》：我..</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675166531789534731" mon="col=1&amp;a=2&pn=12" target="_blank">荣获国家二等功的演员，他从不拿来炫耀，儿子却一点都..</a></li>
</ul>
</div>
<div class="ilist">
<ul>
<li><a href="http://baijiahao.baidu.com/s?id=1675232734404258541" mon="col=2&amp;a=12&pn=1" target="_blank"><img r_src="https://t11.baidu.com/it/u=282653404,3909533248&amp;fm=173&amp;app=49&amp;f=JPEG?w=312&amp;h=208&amp;s=72CAB80B046362B41C35411E0100E0B1"/><span class="title">《以家人之名》三兄妹在线PK摄影技术！</span></a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1675189512904684217" mon="col=2&amp;a=12&pn=2" target="_blank"><img r_src="https://t12.baidu.com/it/u=2022903089,2853621865&amp;fm=173&amp;app=49&amp;f=JPEG?w=312&amp;h=208&amp;s=7900E7174A9D58C80CD490CE0300E030"/><span class="title">2020年暑期档综艺：类型版图有新变，高</span></a></li>
</ul>
</div></div>
<div class="l-right-col" alog-group="log-baijia-right">
<div class="mod" id="baijia-aside-recommend">
<div class="hd">
<h3>百家专栏<span class="dec">BAIJIA</span></h3>
</div>
<div class="bd">
<div id="baijia-recommend">
</div>
</div>
</div>
</div>
</div><ul id="goTop" class="mod-sidebar">
<li class="item report button-rotate" data-text="举报">
<a href="http://report.12377.cn:13225/toreportinputNormal_anis.do">举报</a>
</li>
<li class="item qr-code button-rotate" data-text="二维码">
<a href="javascript:void(0);">二维码</a>
</li>
<li class="qr-code-container clearfix">
<span class="item-container left">
<span class="img-container">
<img src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/img/sidebar/newErweima_9fa03e0.png"/>
</span>
</span>
<span class="item-container right">
<p class="title">百度新闻客户端</p>
<ul>
<li>扫描二维码下载</li>
<li>随时随地收看更多新闻</li>
</ul>
</span>
</li>
<li class="item favorite button-rotate" data-text="收藏本站">
<a href="javascript:void(0);">收藏本站</a>
</li>
<li class="item search button-rotate" data-text="搜索">
<a href="javascript:void(0);" id="search-btn">搜索</a>
</li>
<li class="item feedback button-rotate" id="feedbackbtn" data-text="用户反馈">
<a href="javascript:void(0);">用户反馈</a>
</li>
<li class="item gotop">
<a id="gotop_btn" href="javascript:void(0);" onclick="window.scroll(0, 0)"></a>
</li>
<li class="searchbox">
<span class="close-btn"></span>
<p>
<input type="hidden" name="tn" id="tn" value="news"/>
<input type="hidden" name="from" id="from" value="news"/>
<input type="hidden" name="cl" id="cl" value="2"/>
<input type="hidden" name="rn" id="rn" value="20"/>
<input type="hidden" name="ct" id="ct" value="1"/>
<input class="searchInput" type="text" value="输入搜索词" name="word" autocomplete="off" tabindex="1" maxlength="100"/>
<button class="submit-btn" type="button">搜索</button>
</p>
</li>
<li class="close-tip">收起<i class="arrow"></i></li>
</ul>
<style>
#goTop{
    position: fixed;
    width: 54px;
    left: 50%;
    margin-left: 502px;
    bottom: 20px;
    _position: absolute;
    _top: expression(eval(document.documentElement.scrollTop || document.body.scrollTop)+eval(document.documentElement.clientHeight || document.body.clientHeight)-361+'px');
    z-index:998;
}
</style>

</div>

<div id="footerwrapper">
<div class="bottombar" alog-group="log-footer-bottombar" alog-alias="hunter-start-bottombar">
<div class="bottombar-inner clearfix">
<div class="bot-left">
<div class="title-container">
<i class="icon">&nbsp;</i>
<h4>更多精彩内容</h4>
</div>
<div class="qrcode-container clearfix">
<div class="img-container">
<img src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/img/footer/newErweima_9fa03e0.png">
</div>
<div class="link-container">
<a href="http://downpack.baidu.com/baidunews_AndroidPhone_1014720b.apk" target="_blank">Android版下载</a>
<a href="https://itunes.apple.com/cn/app/id482820737" target="_blank">iPhone版下载</a>
</div>
<p class="info">扫描二维码, 收看更多新闻</p>
</div>
</div>
<div class="bot-right">
<div class="title-container">
<i class="icon">&nbsp;</i>
<h4>百度新闻独家出品</h4>
</div>
<ol>
<li>1. 新闻由机器选取每5分钟自动更新</li>
<li>2. 百度新闻搜索源于互联网新闻网站和频道，系统自动分类排序</li>
<li>3. 百度不刊登或转载任何完整的新闻内容</li>
</ol>
</div>
</div>
</div>
<div style="font-size:12px;text-align:center;">
责任编辑：胡彦BN098 刘石娟BN068 谢建BN085 李芳雨BN091 储信艳BN087 焦碧碧BN084 禤聪BN095 王鑫BN060 崔超BN071 违法和不良信息举报电话：400-921-6911</div>
<div id="footer" alog-group="log-footer" alog-alias="hunter-start-footer">
<a href="//news-bos.cdn.bcebos.com/mvideo/baidu_news_protocol.html">用户协议</a>
<a href="https://www.baidu.com/duty/wise/wise_secretright.html">隐私策略</a>
<a href="//help.baidu.com/newadd?prod_id=5&category=1">投诉中心</a>
<span>京公网安备11000002000001号</span>
<a href="//news-bos.cdn.bcebos.com/mvideo/pcnews_licence.html">互联网新闻信息服务许可</a>
<span>&copy;2020Baidu</span>
<a class="cy" href="//www.baidu.com/duty/">使用百度前必读</a>
<a target="_blank" class="img-link img-link1" href="http://net.china.cn/chinese/index.htm">
</a>
<a target="_blank" class="img-link img-link2" href="http://www.cyberpolice.cn/wfjb/">
</a>
<a target="_blank" class="img-link img-link3" href="http://www.bjjubao.org/">
</a>
</div>
</div>
<style>
#headerwrapper{
    width:100%;
}
</style>
<script type="text/javascript">
var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3Fe9e114d958ea263de46e080563e254c4' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
	  alog("set", "alias", {
         monkey: "https://img.baidu.com/hunter/alog/monkey.min.js",
         element: "https://img.baidu.com/hunter/alog/element.min.js"
     });

     alog("require", ["monkey", "element"], function(monkey, element){
         monkey.create({
             page: "news-yule", 
             pid: "241",
             p: "133",
             hid: "424",
             postUrl: window.HUNTERLOGURL,
             reports: {
                refer: 1, 
                staytime: 1 
             }
         });
     });

     alog("monkey.send", "pageview", { now: +new Date });
</script></body><script type="text/javascript" src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/lib/mod_b818356.js"></script>
<script type="text/javascript">require.resourceMap({"res":{"common:widget/lib/tangram/base/base.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/tangram/base/base_c518988.js","pkg":"common:p0"},"common:widget/lib/magic/magic.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/magic_56edf31.js","pkg":"common:p0"},"common:widget/lib/magic/Base/Base.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/Base/Base_50a505e.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js"]},"common:widget/lib/magic/control/control.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/control/control_5c7cfca.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js"]},"common:widget/lib/magic/control/Layer/Layer.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/control/Layer/Layer_ccd8d01.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/Base/Base.js","common:widget/lib/magic/control/control.js"]},"common:widget/lib/magic/Mask/Mask.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/Mask/Mask_d1105f9.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/control/Layer/Layer.js"]},"common:widget/lib/magic/setup/setup.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/setup/setup_8207eff.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js"]},"common:widget/lib/magic/_query/_query.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/_query/_query_a974d80.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js"]},"common:widget/lib/magic/control/Tab/Tab.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/control/Tab/Tab_6e3b376.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/Base/Base.js","common:widget/lib/magic/control/control.js","common:widget/lib/magic/_query/_query.js"]},"common:widget/lib/magic/setup/tab/tab.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/setup/tab/tab_7ca296e.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/setup/setup.js","common:widget/lib/magic/control/Tab/Tab.js"]},"common:widget/lib/magic/control/Dialog/Dialog.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/control/Dialog/Dialog_c2b9c1a.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/control/Layer/Layer.js"]},"common:widget/lib/magic/Background/Background.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/Background/Background_353ebd3.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/Base/Base.js"]},"common:widget/lib/magic/Dialog/Dialog.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/Dialog/Dialog_239df5f.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/control/Dialog/Dialog.js","common:widget/lib/magic/Background/Background.js"]},"common:widget/lib/magic/control/Dialog/$mask/$mask.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/control/Dialog/$mask/$mask_50466b3.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/control/Dialog/Dialog.js","common:widget/lib/magic/Mask/Mask.js"]},"common:widget/ui/jquery/jquery.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/jquery/jquery_5d7279d.js","pkg":"common:p1"},"common:widget/ui/jquery/jquery.cookie.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/jquery/jquery.cookie_e1f1479.js","pkg":"common:p1"},"common:widget/banner_ad/banner_ad.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/banner_ad/banner_ad_5c31727.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js","common:widget/ui/jquery/jquery.cookie.js"]},"common:widget/banner_ad/banner_ad_data.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/banner_ad/banner_ad_data_aff68ed.js","pkg":"common:p1"},"common:widget/dep/jQuery/plugins/jquery.lavalamp.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/dep/jQuery/plugins/jquery.lavalamp_5a9954b.js","pkg":"common:p1"},"common:widget/favorite/favorite.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/favorite/favorite_bfc0622.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js","common:widget/ui/jquery/jquery.cookie.js"]},"common:widget/feedback/feedback.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/feedback/feedback_6e10548.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js","common:widget/ui/jquery/jquery.cookie.js"]},"common:widget/fixedpannel/fixedpannel.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/fixedpannel/fixedpannel_bf4dc4c.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/control/Layer/Layer.js","common:widget/lib/magic/Mask/Mask.js","common:widget/lib/magic/setup/tab/tab.js","common:widget/lib/magic/Dialog/Dialog.js"]},"common:widget/footer/statistics.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/footer/statistics_83e2581.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js"]},"common:widget/header/header.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/header/header_c2a1ecd.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js"]},"common:widget/hunter/hunter.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/hunter/hunter_2113114.js","pkg":"common:p1"},"common:widget/navbar/navbar.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/navbar/navbar_3ad387b.js","pkg":"common:p1","deps":["common:widget/dep/jQuery/plugins/jquery.lavalamp.js","common:widget/ui/jquery/jquery.js"]},"common:widget/searchbox/searchbox.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/searchbox/searchbox_21149bc.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js"]},"common:widget/searchbox/searchboxActive.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/searchbox/searchboxActive_f139a7f.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js"]},"common:widget/searchbox/searchradio.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/searchbox/searchradio_e67ae37.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js"]},"common:widget/second_navbar/fold.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/second_navbar/fold_b1dea17.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js"]},"common:widget/show_top_qrcode/show_top_qrcode.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/show_top_qrcode/show_top_qrcode_db04dfa.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js"]},"common:widget/sidebar/sidebar.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/sidebar/sidebar_8df2d84.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js","common:widget/feedback/feedback.js"]},"common:widget/ui/jquery/jquery-ui.min.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/jquery/jquery-ui.min_793696a.js","pkg":"common:p1"},"common:widget/ui/jquery/jquery.animateEvents.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/jquery/jquery.animateEvents_fa2738c.js","pkg":"common:p1"},"common:widget/ui/vs/vs.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/vs_ac8f6e6.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js"]},"common:widget/ui/vs/observer/observer.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/observer/observer_7031f75.js","pkg":"common:p1"},"common:widget/ui/vs/ContentPlayer/ContentPlayer.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/ContentPlayer/ContentPlayer_cfa437e.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js","common:widget/ui/vs/vs.js","common:widget/ui/vs/observer/observer.js"]},"common:widget/ui/vs/DynamicList/DynamicList.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/DynamicList/DynamicList_757360e.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js","common:widget/ui/vs/vs.js","common:widget/ui/vs/observer/observer.js"]},"common:widget/ui/vs/ScrollView/ScrollView.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/ScrollView/ScrollView_e529192.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js","common:widget/ui/vs/vs.js"]},"common:widget/ui/vs/Slide/Slide.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/Slide/Slide_bcb1535.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js"]},"common:widget/ui/vs/citylist/citylist.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/citylist/citylist_39082c3.js","pkg":"common:p1"},"common:widget/ui/vs/clickMonitor/clickMonitor.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/clickMonitor/clickMonitor_3b94ea0.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js"]},"common:widget/ui/vs/delayload/delayload.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/delayload/delayload_360bc2c.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js"]},"common:widget/ui/vs/enterState/enterState.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/enterState/enterState_4f3114b.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js"]},"common:widget/ui/vs/imgLazyLoad/ImglazyLoad.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/imgLazyLoad/ImglazyLoad_f2b8599.js","pkg":"common:p1"},"common:widget/ui/vs/slider/slider.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/slider/slider_32bdf45.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js"]},"common:widget/ui/vs/suggestion/suggestion.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/suggestion/suggestion_f2b3c80.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js"]},"common:widget/ui/vs/utils/utils.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/utils/utils_73e2453.js","pkg":"common:p1"}},"pkg":{"common:p0":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/framework_static_include/framework_static_include_aa59e0d.js"},"common:p1":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/module_static_include/module_static_include_5309ae3.js"}}});</script><script type="text/javascript" src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/module_static_include/module_static_include_5309ae3.js"></script>
<script type="text/javascript" src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/framework_static_include/framework_static_include_aa59e0d.js"></script>
<script type="text/javascript">!function(){    	void function(a,b,c,d,e,f,g){a.alogObjectName=e,a[e]=a[e]||function(){(a[e].q=a[e].q||[]).push(arguments)},a[e].l=a[e].l||+new Date,d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d;var h=!0;if(a.alogObjectConfig&&a.alogObjectConfig.sample){var i=Math.random();a.alogObjectConfig.rand=i,i>a.alogObjectConfig.sample&&(h=!1)}h&&(f=b.createElement(c),f.async=!0,f.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),g=b.getElementsByTagName(c)[0],g.parentNode.insertBefore(f,g))}(window,document,"script","/hunter/alog/alog.min.js","alog"),void function(){function a(){}window.PDC={mark:function(a,b){alog("speed.set",a,b||+new Date),alog.fire&&alog.fire("mark")},init:function(a){alog("speed.set","options",a)},view_start:a,tti:a,page_ready:a}}();
      void function(n){var o=!1;n.onerror=function(n,e,t,c){var i=!0;return!e&&/^script error/i.test(n)&&(o?i=!1:o=!0),i&&alog("exception.send","exception",{msg:n,js:e,ln:t,col:c}),!1},alog("exception.on","catch",function(n){alog("exception.send","exception",{msg:n.msg,js:n.path,ln:n.ln,method:n.method,flag:"catch"})})}(window);
	}();
!function(){		alog('speed.set', 'ht', +new Date);
	}();
!function(){		var widgetList = ['Star', 'Movie', 'TV', 'Music', 'Variety', 'Picture', 'LatestNews'];
		var remainWigetList = $.extend(true, [], widgetList);
		var widgetStatus = (function () {
			var list = {};
			for (var i in widgetList) {
				list[widgetList[i]] = false;
			}
			return list;
		})();
		var widgetReferenceList = [];
		// 保证栏目按widgetList的顺序append到#body上
		var appendWidget = function (widgetName, widgetDom) {
			var previousWidgetRef = null;
			widgetReferenceList[widgetName] = $(widgetDom);
			for (var i = 0; i < widgetList.length; i++) {
				previousWidgetName = widgetList[i]
				if (previousWidgetName === widgetName) {
					break;
				}
				if (widgetReferenceList[previousWidgetName]) {
					previousWidgetRef = widgetReferenceList[previousWidgetName];
				}
			}
			if (!previousWidgetRef) {
				nextWidgetRef = null;
				for (var i = widgetList.length - 1; i >= 0; i--) {
					nextWidgetName = widgetList[i]
					if (nextWidgetName === widgetName) {
						break;
					}
					if (widgetReferenceList[nextWidgetName]) {
						nextWidgetRef = widgetReferenceList[nextWidgetName];
					}
				}
				if (!nextWidgetRef) {
					$('#body').append(widgetReferenceList[widgetName]);
				} else {
					nextWidgetRef.before(widgetReferenceList[widgetName]);
				}
			} else {
				previousWidgetRef.last().after(widgetReferenceList[widgetName]);
			}
		}

		var renderWidget = function (widgetName) {
			$.ajax({
				url: '/widget',
				type: 'GET',
				dataType: 'html',
				data: {
					id: widgetName,
					channel: 'ent',
					/*ajax: 'json',*/
					// 时间戳，防止ie6缓存ajax请求导致第二次不请求数据
					t: new Date().getTime()
				},
				timeout: 5000
			}).done(function (data) {
				appendWidget(widgetName, data);
	            require.async(['common:widget/lib/tangram/base/base.js', 'common:widget/ui/vs/delayload/delayload.js'],function(baidu,delayload){
                    baidu.dom.ready(function(){
                        //图片延迟加载
                        var delay=new delayload();

                        delay.init();
                        delay.delayLoader(1);
                        delay.bindUI();
                    });
	            });
			});
		}
		var getLoadingWidgetName = function () {
			return remainWigetList.shift();
		}
		var isChrome = navigator.userAgent.indexOf("Chrome") > -1;
		var isSafari = navigator.userAgent.indexOf("Safari") > -1;
		window.onscroll = function () {
			var body = $('body');
			var height = body.height();
			var scrollTop = 0;
			if (isChrome || isSafari) {
				scrollTop = $('body').scrollTop();
			} else {
				scrollTop = document.documentElement.scrollTop;
			}
			if (scrollTop > 1) {
				widgetName = getLoadingWidgetName();

				if (widgetStatus[widgetName] === false) {
					widgetStatus[widgetName] = true;
					renderWidget(widgetName);
				}
			}
		}
	}();
!function(){		$(function () {
			$.ajax({
				url: '/passport',
				type: 'GET',
				dataType: 'json',
				timeout: 5000
			}).done(function (data) {
				var userName = '';
				var isLogin = false;
				if(data.errno ===0 && data.data && data.data.displayname) {
					isLogin = true;
					userName = data.data.displayname;
				}
				window['isLogin'] = isLogin;
				require.async("common:widget/ui/vs/enterState/enterState.js", function (enterState) {
					enterState(userName, "")
				});
			});
		})
	}();
!function(){	window.onbeforeunload = function(e){
		window.scrollTo(0,0);
	}
	}();
!function(){    require.async(['common:widget/header/header.js'],
        function (mod) {
            mod.init();
        }
    );
}();
!function(){	require.async('common:widget/show_top_qrcode/show_top_qrcode.js', function(showqrcode) {
		showqrcode.init();
	});
}();
!function(){    require.async(["common:widget/lib/tangram/base/base.js", "common:widget/searchbox/searchbox.js", "common:widget/ui/vs/suggestion/suggestion.js"], function(baidu,searchbox,suggestion){
        baidu.dom.ready(function(){
            searchbox.searchbox();
            searchbox.searchnews();
            if (navigator.cookieEnabled && !/sug?=0/.test(document.cookie)){
                    suggestion();
            }
        });
    });
}();
!function(){    require.async(['common:widget/searchbox/searchradio.js', 'common:widget/searchbox/searchboxActive.js'], function(searchRadio, searchboxActive) {
        searchRadio();
        searchboxActive();
    });
}();
!function(){require.async(['common:widget/navbar/navbar.js'],
function (mod) {
mod.init();
}
);
}();
!function(){		require.async(['common:widget/ui/vs/clickMonitor/clickMonitor.js', 'common:widget/lib/tangram/base/base.js'], function(clickMonitor, baidu){
            if(window.on === undefined) window.on = baidu.on;
            clickMonitor.init('ONE_LEVEL_HOT', 'c=enternews&cy=0');
        });
		var extraInfo = {
			m: 11,
			c: 'top'
		};
		require.async('common:widget/ui/vs/clickMonitor/clickMonitor.js', function(clickMonitor){
		    clickMonitor.init('TOP');
		});
	    require.async(['common:widget/lib/tangram/base/base.js', 'common:widget/ui/vs/delayload/delayload.js'],function(baidu,delayload){
	      baidu.dom.ready(function(){
	        //图片延迟加载
	        var delay=new delayload();

	        delay.init();
	        delay.delayLoader(1);
	        delay.bindUI();
	      });
	    });

		var PAGE_DATA = {
		    "guess_list_num": 0,
		    "guess_jsonp_status" : true
		};
  	}();
!function(){    require.async(['common:widget/lib/tangram/base/base.js', 'common:widget/ui/vs/ContentPlayer/ContentPlayer.js'], function(T, I) {
        var G = T.dom.g;
        var on = T.event.on;
        var imgList = [];
        var cpOptions_1 = {
            getBtns: function(){
                var a, btns; 
                    btns = G('imgNav').getElementsByTagName('a');
                    a = [];
                    for(var i=btns.length - 1; i>=0; i--){
                        a.push(btns[i]);
                    }
                    return a;
                },
                mainViewContainer: G('imgView'),
                prevBtn: G('imgplayer-prev'),
                nextBtn: G('imgplayer-next'),
                changeAction: 'mouseover',
                subViewContainer: G('imgTitle'),
                style: {on: 'active', off: ''},
                mainViewTpl: '<a href="#{url}" target="_blank" mon="col=carousel&pos=img&pn=#{index}"><img src="#{imgUrl}"></a>',
                subViewTpl: '<a href="#{url}" target="_blank" mon="col=carousel&pos=title&a=9&ct=1&pn=#{index}"><strong>#{title}</strong>#{abs}</a>',
                curIndex: 0,
                data: [],
                interval: 5000
        };

        
                                            cpOptions_1.data.push({
            "index": 1,
                "title": "鬼鬼吴映洁穿彩纹开叉裙半露香肩 侧颜精致蓝色眼线吸睛",
                "url": "https:\/\/3w.huanqiu.com\/a\/64d6f1\/3zUei7VyWEt?agt=8",
                "imgUrl": "https:\/\/b.bdstatic.com\/boxlib\/20200817\/2020081717505765666807023.jpg",
                "abs": "近日，鬼鬼吴映洁晒出自己的一组照片。"
            });
            imgList.push({"url":"https:\/\/3w.huanqiu.com\/a\/64d6f1\/3zUei7VyWEt?agt=8"});
                                                        cpOptions_1.data.push({
            "index": 2,
                "title": "杨玏毛晓彤合体拍大片 撸猫对视cp感满满",
                "url": "https:\/\/3w.huanqiu.com\/a\/64d6f1\/3zUdfSUbb9G?agt=8",
                "imgUrl": "https:\/\/b.bdstatic.com\/boxlib\/20200817\/202008171750574003157746.jpg",
                "abs": "8月16日，杨玏毛晓彤合体拍摄的一组大片曝光。"
            });
            imgList.push({"url":"https:\/\/3w.huanqiu.com\/a\/64d6f1\/3zUdfSUbb9G?agt=8"});
                                                        cpOptions_1.data.push({
            "index": 3,
                "title": "黄晓明最新杂志大片曝光 大秀肱二头肌满满荷尔蒙",
                "url": "https:\/\/3w.huanqiu.com\/a\/64d6f1\/3zUdseR26IF?agt=8",
                "imgUrl": "https:\/\/b.bdstatic.com\/boxlib\/20200817\/2020081717505757855088822.jpg",
                "abs": "近日，黄晓明最新杂志高清大片曝光。"
            });
            imgList.push({"url":"https:\/\/3w.huanqiu.com\/a\/64d6f1\/3zUdseR26IF?agt=8"});
                    
        var index = 0 ; 
        var url = location.href.substr(location.href.indexOf("?")+1).split("&");
        var key ;
        for(var i = 0 ; i < url.length ; i++){
            var tmp = url[i].split("=");
            if(tmp&&tmp.length>0&&tmp[0]=="lb"){
                key = tmp[1];
            }
            }
        for(var p in imgList){
            if(imgList[p].url == key){
                index = p ;
            }
        }
        cpOptions_1.curIndex = index;
        var cp_1 = new I.Model(cpOptions_1);

        on(window, 'load', function(){
            cp_1.play(index+1);
        });

        var controlers = baidu.dom.query('#imgNav a');
        baidu.each(controlers,function(item,i){
            baidu.on(item,'mouseover',function(e){
                UserMonitor.send(e, 6, {c : "finannews", col: "carousel", ct: "1", m: "11", pn: 8-i, pos : "dots", ac : "mouseover"});
                window.alog && alog("monkey.fire", "record", {
                    type: "click",
                    target: item
                }); 
            });
        });
    });
}();
!function(){require.async(['common:widget/sidebar/sidebar.js'],
    function (Sidebar) {
        $(function () {
            var sidebar = new Sidebar();
            sidebar.init();
        });
    }
);
}();
!function(){    require.async(['common:widget/footer/statistics.js'], function (mod) {
        // 页面加载后，向biglog发送一个pv统计，传入hostname区分产品和频道
        mod.postReferToBiglog();
        // 页面加载后，初始化发送往百度统计的打点
        mod.initClickPostToTongji();
        // 页面加载后，向百度统计发送页面的refer
        mod.postReferToTongji();
    });
}();
!function(){    document.write("<img src='/mp/b.jpg?cmd=1&class=mil&cy=0&"+Math.random()+"' style='display:none;'>");
    <!-- document.write("<img id='cgif' src='http://ccccccc.baidu.com/c.gif?t=5&p=2&"+Math.random()+"' style='display:none'>"); -->

    require.async('common:widget/lib/tangram/base/base.js', function(baidu){
        baidu.each(baidu.dom.query('img'),function(item){	
            if(/eiv.baidu.com\/hmt\/icon/.test(baidu.dom.getAttr(item, 'src'))){
                item.style.display = 'none';		
            }
        });
    });
}();</script></html>
'''
# (https+.+?\.jpg|https+.+?\.png|https+.+?\.gif)
pattern = re.compile(r'(http?.+?\.jpg|http?.+?\.png|http?.+?\.gif)', re.IGNORECASE)
all_list = re.findall(pattern,str)
print(all_list)
