## 将原来的直连方式改为中转

### 1. 获取数据库中 inbounds 表中的 remark 和 code 字段
### 2. 将获取到的内容构造为如下表示：
```text
{"dest":["dev0.vikingsword:57956"],"listen_port":57956,"name":"dev-1042610331-hk"}
{"dest":["dev0.vikingsword:30297"],"listen_port":30297,"name":"dev-qu-专线2"}
{"dest":["dev0.vikingsword:42388"],"listen_port":42388,"name":"dev-gfd-专线2"}
```
以上是代码要实现的部分
### 3. cf添加解析字段
原来的域名`dev.vikingsword.top`做`cname`解析到`relay1.1593570.xyz`

