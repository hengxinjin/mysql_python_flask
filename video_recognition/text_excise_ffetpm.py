import urllib.request
import os
import time
import pymysql
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.getcwd() + '/logs/'
log_name = log_path + rq + '.log'
print(log_name)
logfile = log_name
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)


def db_init():
    return pymysql.connect(
    host='192.168.1.23',
    port=3306,
    database='hengxinjin',
    user='root',
    passwd='123456'
)

def get_task_from_db():
    conn = db_init()
    cursor=conn.cursor()
    sql = 'select * from pictures_project where status =0'
    logger.info(sql)
    cursor.execute(sql)
    info = cursor.fetchall()
    cursor.close()
    conn.close()
    return info

def update_status(task_id, status):
    try:
        sql = "Update pictures_project set status=%s where id=%s" % (status, task_id)
        logger.info(sql)

        conn = db_init()
        cursor=conn.cursor()
        cursor.execute(sql)
        conn.commit()

        cursor.close()
        conn.close()
        logger.info('update sucessful')
        return "update sucessful"

    except:

        return "fail"

def deal_with_ffmpeg(video_url):

    logger.info("Deal with url: %s" % video_url)
    logger.info(video_url)
    save_name = video_url.split('/')[-1]
    save_path = '/home/tarena/ffmpeg_demo/download/%s' % save_name

    logger.info("Save video to: %s" % save_path)
    urllib.request.urlretrieve(video_url, save_path)
    image_dir_name = 'image_' + str(task_id)

    if not os.path.exists('/home/tarena/ffmpeg_demo/{}'.format(image_dir_name)):
        os.mkdir('/home/tarena/ffmpeg_demo/{}'.format(image_dir_name))

    cmd = "ffmpeg -i {} -r 1 -q:v 2 -f image2 /home/tarena/ffmpeg_demo/{}/%d.jpeg".format(save_path, image_dir_name)
    logger.info(cmd)

    rt_cmd = os.system(cmd)
    if rt_cmd == 0:
        logger.info('Sucess for cmd: %s' % cmd)
        logger.info('Sucess for cmd')
        return 0
    else:
        logger.info('Failure for cmd: %s' % cmd)
        logger.info('Failure for cmd')
        return 1



while True:
    try:
        # get_task
        info = get_task_from_db()

        if len(info) == 0:
            logger.info('No task found in DB')
            logger.info('No task found in DB')
            logger.info(info)


        for i in range(len(info)):
            task_id = info[i][0]
            video_url = info[i][2]
    
            # deal with ffmpeg
            rt = deal_with_ffmpeg(video_url)

            # picture recognize

            # update status
            # update status
            if rt == 0:
                update_status(task_id, 1)
            else:
                update_status(task_id, 5)

        logger.info("=============================================")
        time.sleep(2)

    except:
        logger.info("ERROR !!!")
        logger.info('ERROR!!!')
        time.sleep(2)

