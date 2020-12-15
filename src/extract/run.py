# encoding: utf-8
"""
@time           : 2020/9/30
@author         : shijingui@jd.com
@file           : shell.py
@description    : repo


    ##########################################################
    #
    # 依赖的相关文章表
    # odm.odm_cmp_nryy_ic_imagetext_element_150_i_d
    # odm.odm_cmp_nryy_ic_community_content_i_d
    #
    # 输出表
    # dmc_ll.dmcll_sr_brs_credit_cart_date_a_d
    #
    # $TXPDATE
    #
    ##########################################################


"""
import sys
import re

from pyspark.context import SparkContext
from pyspark.sql import HiveContext
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from datetime import datetime

tx_date = sys.argv[1]
tx_date = tx_date.strip()
print('tx_date: %s' % (tx_date))

sparkConf = SparkConf()

sparkConf.set('spark.driver.memory', '8G')
sparkConf.set('spark.driver.cores', '8')
sparkConf.set("spark.kryoserializer.buffer.max", "128m")
sparkConf.set("spark.executor.instances", "100")
sparkConf.set("spark.driver.maxResultSize", '4G')
sparkConf.set("spark.executor.cores", "2")
sparkConf.set("spark.executor.memory", "4G")
sparkConf.set("spark.app.name", 'date_extract')

# 日期抽取正则表达式
r1 = r'即日.[到|起|起至|起到|至|到至]*[\d{4}年]*\d{1,2}月\d{1,2}日[\d{1,2}]*:*[\d{1,2}]*'

r2 = r'[\d{4}年]*\d{1,2}月\d{1,2}日.[到|起|起至|起到|至|到至]*[\d{4}年]*\d{1,2}月\d{1,2}日[\d{1,2}]*:*[\d{1,2}]*:*[\d{1,2}]*'

p1 = re.compile(r1)
p2 = re.compile(r2)


def date_extract(rdd):
    content = rdd[0]
    all_date1 = p1.findall(content)
    all_date2 = p2.findall(content)
    page_id = rdd[2]
    content_id = rdd[1]
    ret = ''
    if all_date1:
        ret = ','.join(all_date1)

    if all_date2:
        ret = ','.join(all_date2)

    return (content_id, page_id, ret, datetime.now())




spark = SparkSession.builder.config(conf=sparkConf).enableHiveSupport().getOrCreate()

spark.sql('use dmc_ll')



spark_df = spark.sql(
    "select distinct a.content, a.id as content_id, a.page_id from odm.odm_cmp_nryy_ic_imagetext_element_150_i_d as a inner join odm.odm_cmp_nryy_ic_community_content_i_d as b on a.page_id = b.id where b.source_category = '信用卡_精选优惠' and a.is_deleted = 0 and b.is_deleted = 0")

newDF = spark_df.rdd.map(lambda x: date_extract(x)).toDF()
newDF.registerTempTable('df_query_tmp')

spark.sql(
    """ insert overwrite table dmc_ll.dmcll_sr_brs_credit_cart_date_a_d  select _1, _3,_2,_4 from df_query_tmp """)