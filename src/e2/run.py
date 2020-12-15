# encoding: utf-8


import sys
import re

from pyspark.context import SparkContext
from pyspark.sql import HiveContext
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from datetime import datetime

# tx_date = sys.argv[1]
# tx_date = tx_date.strip()
# print('tx_date: %s' % (tx_date))

sparkConf = SparkConf()

sparkConf.set('spark.driver.memory', '20G')
sparkConf.set('spark.driver.cores', '20')
sparkConf.set("spark.kryoserializer.buffer.max", "128m")
sparkConf.set("spark.executor.instances", "100")
sparkConf.set("spark.driver.maxResultSize", '10G')
sparkConf.set("spark.executor.cores", "2")
sparkConf.set("spark.executor.memory", "10G")
sparkConf.set("spark.app.name", 'date_extract')


def date_extract(rdd):
    allDate1 = p1.findall(rdd[0])
    allDate2 = p2.findall(rdd[0])
    pageId = rdd[2]
    contentId = rdd[1]
    ret = ''
    if allDate1:
        ret = ','.join(allDate1)

    if allDate2:
        ret = ','.join(allDate2)
    return (contentId, pageId, ret, '1')




spark = SparkSession.builder.config(conf=sparkConf).enableHiveSupport().getOrCreate()

spark.sql('use dmc_ll')

# 日期抽取正则表达式
r1 = r'即日.[到|起|起至|起到|至|到至]*[\d{4}年]*\d{1,2}月\d{1,2}日[\d{1,2}]*:*[\d{1,2}]*'

r2 = r'[\d{4}年]*\d{1,2}月\d{1,2}日.[到|起|起至|起到|至|到至]*[\d{4}年]*\d{1,2}月\d{1,2}日[\d{1,2}]*:*[\d{1,2}]*:*[\d{1,2}]*'

p1 = re.compile(r1)
p2 = re.compile(r2)

spark_df = spark.sql(
    "select distinct a.content, a.id as content_id, a.page_id from odm.odm_cmp_nryy_ic_imagetext_element_150_i_d as a inner join odm.odm_cmp_nryy_ic_community_content_i_d as b on a.page_id = b.id where b.source_category = '信用卡_精选优惠' and a.is_deleted = 0 and b.is_deleted = 0")

newDF = spark_df.rdd.map(lambda x: date_extract(x)).toDF()
newDF.show()
newDF.registerTempTable('df_query_tmp')

spark.sql(
    """ insert overwrite table dmc_ll.dmcll_sr_brs_credit_cart_date_a_d  select _1, _3,_2,_4 from df_query_tmp """)
