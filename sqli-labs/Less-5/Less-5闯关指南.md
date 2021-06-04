# Less-5

第五关好像开始变得大不一样了

```http
http://localhost:8080/sqli-labs/Less-5/?id=1
```

![1622165936765](1622165936765.png)

## 5.1 判断sql注入类型

尝试了加上单引号，发现有报错信息，再添加注释符后页面改变说明存在sql注入

```http
http://localhost:8080/sqli-labs/Less-5/?id=1'
http://localhost:8080/sqli-labs/Less-5/?id=1' --+
```

![1622166226784](1622166226784.png)

提取报错中的有效信息

```mysql
1'' 
```

看样子好像也只是Less-3单引号字符型，甚至还没有括号，但按照前几关的方法想接着往下走却是行不通T^T

尝试盲注

