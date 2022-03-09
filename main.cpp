#include <iostream>
#include "skiplist.h"
#define FILE_PATH "./store/dumpFile"

int main() {

    // 键值中的key用int型，如果用其他类型，需要自定义比较函数
    // 而且如果修改key的类型，同时需要修改skipList.load_file函数
    SkipList<int, std::string> skipList(6);
	skipList.insert_element(1, "不是原作者"); 
	skipList.insert_element(3, "原作者是carl"); 
	skipList.insert_element(7, "该项目用来学习跳表"); 
	skipList.insert_element(8, "wangyifan"); 
	skipList.insert_element(9, "de"); 
	skipList.insert_element(19, "xuexi"); 
	skipList.insert_element(19, "项目"); 

    std::cout << "skipList size:" << skipList.size() << std::endl;

    skipList.dump_file();

    // skipList.load_file();

    skipList.search_element(9);
    skipList.search_element(18);


    skipList.display_list();

    skipList.delete_element(3);
    skipList.delete_element(7);

    std::cout << "skipList size:" << skipList.size() << std::endl;

    skipList.display_list();
}
