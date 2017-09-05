

'''
1. import logging
2. # 创建一个logger
3. logger = logging.getLogger('mylogger')
4. logger.setLevel(logging.DEBUG)
5. # 创建一个handler，用于写入日志文件
6. fh = logging.FileHandler('test.log')
7. fh.setLevel(logging.DEBUG)
8. # 再创建一个handler，用于输出到控制台
9. ch = logging.StreamHandler()
10. ch.setLevel(logging.DEBUG)
11. # 定义handler的输出格式
12. formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
13. fh.setFormatter(formatter)
14. ch.setFormatter(formatter)
15. # 给logger添加handler
16. logger.addHandler(fh)
17. logger.addHandler(ch)
18. # 记录一条日志
19. logger.info('foorbar')??

'''

import logging

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('test.log')

