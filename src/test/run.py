# encoding: utf-8
"""
@time           : 2020/9/17
@author         : liuning11@jd.com
@file           : shell.py
@description    : repo


    ##########################################################
    #
    # user侧特征表
    # dmc_qm.DMCQM_LHMX_COMMUNITY_FEED_DEEP_ITEM_FEATURE_I_D
    # dmc_ll.dmcll_sr_user_lhmx_community_feed_deep_item_feature_i_d
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


tx_date = sys.argv[1]
tx_date = tx_date.strip()
print('tx_date: %s' % (tx_date))



sparkConf = SparkConf()

sparkConf.set('spark.driver.memory', '20G')
sparkConf.set('spark.driver.cores', '20')
sparkConf.set("spark.kryoserializer.buffer.max", "128m")
sparkConf.set("spark.executor.instances", "100")
sparkConf.set("spark.driver.maxResultSize", '10G')
sparkConf.set("spark.executor.cores", "2")
sparkConf.set("spark.executor.memory", "10G")
sparkConf.set("spark.app.name", 'date_extract')






spark = SparkSession.builder.config(conf=sparkConf).enableHiveSupport().getOrCreate()

spark.sql('use dmc_ll')


sc = spark.sparkContext

r1 = r'即日.[到|起|起至|起到|至|到至]*[\d{4}年]*\d{1,2}月\d{1,2}日[\d{1,2}]*:*[\d{1,2}]*'

r2 = r'[\d{4}年]*\d{1,2}月\d{1,2}日.[到|起|起至|起到|至|到至]*[\d{4}年]*\d{1,2}月\d{1,2}日[\d{1,2}]*:*[\d{1,2}]*:*[\d{1,2}]*'

p1 = re.compile(r1)
p2 = re.compile(r2)


spark_df = spark.sql("select distinct a.content, a.id as content_id, a.page_id from odm.odm_cmp_nryy_ic_imagetext_element_150_i_d as a inner join odm.odm_cmp_nryy_ic_community_content_i_d as b on a.page_id = b.id where b.source_category = '信用卡_精选优惠' and a.is_deleted = 0 and b.is_deleted = 0")

print('---------------------data------------------------------')
spark_df.count()
print('---------------------data------------------------------')

def parse_babies_feas(line):
    return line.content_id, line.page_id, line.content


dataArr = spark_df.rdd.map(parse_babies_feas).collect()


resultData = []

for row in dataArr:
    allDate1 = p1.findall(row[2])
    allDate2 = p2.findall(row[2])
    pageId = row[1]
    contentId = row[0]
    ret = ''
    if allDate1:
        for d in allDate1:
            ret = d + ',' + ret

    if allDate2:
        for d in allDate2:
            ret = d + ',' + ret

    if len(ret) > 0:
        #         print(str(row[0])+","+ret)
        tupleData = (contentId, pageId, ret, 'x')
        resultData.append(tupleData)

print(len(resultData))

newDF = sc.parallelize(resultData).toDF()

print('------------------------------1')

newDF.count()
newDF.registerTempTable('df_query_tmp')


# spark.sql(
#     """ insert overwrite table dmc_ll.dmcll_sr_brs_credit_cart_date_a_d  select _1, _3,_2,_4 from df_query_tmp """)

# print(type(newDF))
# newDF.show()


