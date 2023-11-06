
import csv

def List_job(jenkins_url,jenkins_user,jenkins_pass):
        import jenkins 

        jen_server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_pass)
        user = jen_server.get_whoami()
        jobs = jen_server.get_jobs()
    

        job_stats=[]

        for i in jobs:
    
            Job_name = i['name']
            job_url = i['url']
            job_status= i['color']
            job_stats.append([Job_name,job_url,job_status])
        return job_stats


# Call the function and capture the returned value
        #job_stats = get_job_stats()

# # Write job_stats to a file
# with open("example.txt", 'a') as f:
#         content = "kkkfkfkkfkfkkkf\n"  
#         f.write(content)

# # Read and print the content of the file
# with open("example.txt", 'r') as file:
#         cont = file.read()
#         print(cont)

data=List_job('http://45.33.11.12:8080','utrains','devops')
# Open the CSV file in write mode
with open("C:/Users/Mpung/jenkins_object.csv",'w',newline='') as j:
     
 # Create a CSV writer object    
     writer_row = csv.writer(j)
 # Write the header row to the CSV file    
     writer_row.writerow(['JOB_NAME','JOB_URL','JOB_STATUS']) 
 #Write a row of data to the CSV file    
     writer_row.writerow(data)
     for item in data:
           writer_row.writerow([item])

