# douban2018
抓取豆瓣2018年书单

通过对原始网站https://book.douban.com/annual/2018?source=navigation#1进行分析，
找到数据存放的地址https://book.douban.com/ithil_j/activity/book_annual2018/widget/1
在spider中引入json库，用json库对数据进行提取
将提取到的数据存入items中
