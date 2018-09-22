
deploying_aws_file = './deploying_aws.txt'

deploying_aws_metric = open(deploying_aws_file,'w+')



print("Counting")
metric_file = open("deploying_aws.txt","w+")

for i in range(10):
	metric_file.write("This is line %d\r\n" % (i+1))
	
metric_file.close()