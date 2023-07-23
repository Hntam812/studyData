
Biên dịch mã nguồn Java để tạo file .jar:
bash
Copy code
$ javac -classpath $(hadoop classpath) WebAccessCounter.java
$ jar cvf webaccesscounter.jar WebAccessCounter*.class
Chạy công việc Hadoop bằng lệnh sau:
bash
Copy code
$ hadoop jar webaccesscounter.jar WebAccessCounter <input_path> <output_path>
Với <input_path> là đường dẫn đến tệp log đầu vào và <output_path> là đường dẫn đến thư mục đầu ra.

Sau khi công việc kết thúc, bạn sẽ tìm thấy kết quả trong thư mục đầu ra được chỉ định <output_path>. Kết quả sẽ bao gồm các trang web và số lượt truy cập tương ứng.

Nội dung của tệp input_log.txt:
bash
Copy code
2023-06-15 10:30:15 192.168.1.1 /page1.html
2023-06-15 10:32:40 192.168.1.2 /page2.html
2023-06-15 10:34:18 192.168.1.3 /page1.html
2023-06-15 10:35:55 192.168.1.4 /page3.html
Nội dung của tệp output_log.txt (tệp kết quả):
bash
Copy code
/page1.html    2
/page2.html    1
/page3.html    1


Để cài đặt và chạy code Hadoop, bạn cần thực hiện các bước sau:

Cài đặt Java Development Kit (JDK): Hadoop chạy trên Java, vì vậy bạn cần cài đặt JDK trên hệ thống của mình. Hãy tải và cài đặt JDK từ trang web chính thức của Oracle hoặc từ nguồn cung cấp khác.

Tải Hadoop: Truy cập trang web chính thức của Apache Hadoop (https://hadoop.apache.org/) và tải xuống phiên bản Hadoop phù hợp với hệ điều hành của bạn. Sau đó, giải nén tệp tin nén Hadoop vào một thư mục trên máy tính của bạn.

Cấu hình Hadoop: Mở tệp cấu hình hadoop-env.sh trong thư mục etc/hadoop của Hadoop và đặt biến JAVA_HOME để chỉ đến thư mục cài đặt JDK trên hệ thống của bạn.

Cấu hình HDFS: Mở tệp cấu hình core-site.xml trong thư mục etc/hadoop của Hadoop và đặt giá trị của thuộc tính fs.defaultFS là hdfs://localhost:9000. Điều này sẽ chỉ định rằng bạn đang sử dụng HDFS trên máy cục bộ với cổng 9000.

Cấu hình MapReduce: Mở tệp cấu hình mapred-site.xml.template trong thư mục etc/hadoop của Hadoop và lưu nó dưới tên mapred-site.xml. Trong tệp mới, đặt giá trị của thuộc tính mapreduce.framework.name là yarn.

Cấu hình YARN: Mở tệp cấu hình yarn-site.xml trong thư mục etc/hadoop của Hadoop và thêm các thuộc tính sau:

php
Copy code
<property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
</property>
<property>
    <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
    <value>org.apache.hadoop.mapred.ShuffleHandler</value>
</property>
Khởi chạy Hadoop: Mở cửa sổ terminal và điều hướng đến thư mục gốc của Hadoop. Sử dụng lệnh sau để khởi động HDFS và YARN:

bash
Copy code
$ bin/hdfs namenode -format
$ sbin/start-dfs.sh
$ sbin/start-yarn.sh
Tải lên tệp log vào HDFS: Sử dụng lệnh sau để tải tệp input_log.txt lên HDFS:

bash
Copy code
$ bin/hdfs dfs -mkdir /input
$ bin/hdfs dfs -put /path/to/input_log.txt /input
Chạy code Hadoop: Sử dụng lệnh sau để chạy code Hadoop của bạn:

bash
Copy code
$ bin/hadoop jar /path/to/your.jar <input_path> <output_path>
Thay thế <input_path> bằng đường dẫn tới tệp input_log.txt trên HDFS và <output_path> bằng đường dẫn tới thư mục đầu ra mong muốn trên HDFS.

Kiểm tra kết quả: Sử dụng lệnh sau để xem kết quả trong tệp output_log.txt:

bash
Copy code
$ bin/hdfs dfs -cat <output_path>/part-00000
Thay thế <output_path> bằng đường dẫn đến thư mục đầu ra mà bạn đã chọn trong bước trước.

Đây chỉ là một hướng dẫn cơ bản để cài đặt và chạy Hadoop. Quá trình cài đặt có thể khác nhau tùy thuộc vào phiên bản Hadoop và môi trường của bạn. Bạn cũng cần hiểu và điều chỉnh cấu hình Hadoop phù hợp với yêu cầu của bạn.


