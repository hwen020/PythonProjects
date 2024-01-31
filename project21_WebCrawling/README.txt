WEB CRAWLER:
Make sure that you have all the files under the same project.
Finally you have to run the main.py file.
Make sure that you type in the proper URL for the HOMEPAGE variable in main.py file.

FILES:
demo.py
domain.py
spider.py
main.py
link_finder.py

OUTPUT:
thesite
  -crawled.txt
  -queue.txt

demo.py:

create_project_dir(directory): Creates a new directory if it doesn't exist.
create_data_files(project_name, base_url): Creates queue and crawled data files if they don't exist.
write_file(path, data): Writes data to a file.
append_to_file(path, data): Appends data to an existing file.
delete_file_contents(path): Clears the contents of a file.
file_to_set(file_name): Reads a file and returns its content as a set.
set_to_file(links, file_name): Writes a set of links to a file.

domain.py:

get_domain_name(url): Extracts the domain name from a URL.
get_sub_domain_name(url): Extracts the subdomain name from a URL.

spider.py:

Spider class: Represents the web crawler.
init(project_name, base_url, domain_name): Initializes the Spider with project details and starts crawling.
boot(): Sets up the project directory and data files.
crawl_page(thread_name, page_url): Crawls a given page URL.
gather_links(page_url): Extracts links from the HTML of a page.
add_links_to_queue(links): Adds links to the queue if they meet certain conditions.
update_files(): Updates the queue and crawled files after crawling.

main.py:

HOMEPAGE: Needs to be set to the starting URL.
PROJECT_NAME: Specifies the project name.
DOMAIN_NAME: Extracted from the homepage URL.
QUEUE_FILE, CRAWLED_FILE: Paths to queue and crawled data files.
NUMBER_OF_THREADS: Number of threads for parallel crawling.
queue: A Queue object for managing URLs to be crawled.
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME): Initializes the Spider and starts crawling.
crawl(): Reads queued links and initiates crawling.
create_jobs(): Puts links into the queue for crawling.
create_workers(): Creates and starts worker threads.
work(): Defines the work that each thread does.

link_finder.py:

LinkFinder class (inherits HTMLParser): Parses HTML to find and extract links.
init(base_url, page_url): Initializes with base and page URLs.
handle_starttag(tag, attrs): Extracts links from 'a' tags in HTML.
page_links(): Returns the set of links extracted from the page.
To run the web crawler, set the HOMEPAGE variable in main.py to the desired starting URL and execute main.py.
The code uses threading for concurrent crawling and implements various functions for file handling, link extraction, and crawling logic.