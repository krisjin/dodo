from pyspark import SparkContext



sc = SparkContext("local", "count app")



words = sc.parallelize (
   ["scala",
   "java",
   "hadoop",
   "spark",
   "akka",
   "spark vs hadoop",
   "pyspark",
   "pyspark and spark"]
)


def g(x):
   print(x)

counts = words.count()

words.foreach(g)

print(type(words.collect()))
print ("Number of elements in RDD -> %i" % (counts))