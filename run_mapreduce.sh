#source ./hadoop_bashrc
#./create_10G.sh
hadoop fs -mkdir /sortip
hadoop fs -put data_file.txt /sortip/
hadoop fs -ls /sortip
#hs sort_mapper.py sort_reducer.py /sortip /sortop
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar -mapper sort_mapper.py -reducer sort_reducer.py -file sort_mapper.py -file sort_reducer.py -input /sortip -output /sortop
hadoop fs -ls /sortip
