

'''
1. import logging
2. # ����һ��logger
3. logger = logging.getLogger('mylogger')
4. logger.setLevel(logging.DEBUG)
5. # ����һ��handler������д����־�ļ�
6. fh = logging.FileHandler('test.log')
7. fh.setLevel(logging.DEBUG)
8. # �ٴ���һ��handler���������������̨
9. ch = logging.StreamHandler()
10. ch.setLevel(logging.DEBUG)
11. # ����handler�������ʽ
12. formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
13. fh.setFormatter(formatter)
14. ch.setFormatter(formatter)
15. # ��logger���handler
16. logger.addHandler(fh)
17. logger.addHandler(ch)
18. # ��¼һ����־
19. logger.info('foorbar')??

'''

import logging

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('test.log')

