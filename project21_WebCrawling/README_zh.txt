demo.py:

create_project_dir(directory): 如果目录不存在，则创建新目录。
create_data_files(project_name, base_url): 如果不存在，创建队列和已爬取数据文件。
write_file(path, data): 将数据写入文件。
append_to_file(path, data): 将数据追加到现有文件。
delete_file_contents(path): 清空文件内容。
file_to_set(file_name): 读取文件并将其内容返回为集合。
set_to_file(links, file_name): 将链接集合写入文件。

domain.py:

get_domain_name(url): 从URL中提取域名。
get_sub_domain_name(url): 从URL中提取子域名。

spider.py:

Spider类: 表示网络爬虫。
init(project_name, base_url, domain_name): 使用项目详情初始化Spider并开始爬取。
boot(): 设置项目目录和数据文件。
crawl_page(thread_name, page_url): 爬取给定的页面URL。
gather_links(page_url): 从页面的HTML中提取链接。
add_links_to_queue(links): 如果符合某些条件，将链接添加到队列中。
update_files(): 在爬取后更新队列和已爬取文件。

main.py:

HOMEPAGE: 需要设置为起始URL。
PROJECT_NAME: 指定项目名称。
DOMAIN_NAME: 从主页URL中提取。
QUEUE_FILE, CRAWLED_FILE: 队列和已爬取数据文件的路径。
NUMBER_OF_THREADS: 并行爬取的线程数。
queue: 用于管理待爬取的URL的队列对象。
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME): 初始化Spider并开始爬取。
crawl(): 读取队列中的链接并启动爬取。
create_jobs(): 将链接放入队列以进行爬取。
create_workers(): 创建并启动工作线程。
work(): 定义每个线程的工作。

link_finder.py:

LinkFinder类 (继承HTMLParser): 解析HTML以查找并提取链接。
init(base_url, page_url): 使用基本URL和页面URL初始化。
handle_starttag(tag, attrs): 从HTML中的'a'标签中提取链接。
page_links(): 返回从页面提取的链接集合。
要运行网络爬虫，请将main.py中的HOMEPAGE变量设置为所需的起始URL，并执行main.py。该代码使用线程进行并发爬取，并实现了用于文件处理、链接提取和爬取逻辑的各种函数