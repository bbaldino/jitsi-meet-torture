#!/usr/bin/python

import sys
import requests

if len(sys.argv) < 2:
    print("Usage: %s <psnr_output_file_path> <dashboard_service_url> \n" % (sys.argv[0]))
    sys.exit(1)

psnr_output_file_path = sys.argv[1]
dashboard_service_url = sys.argv[2]
jenkins_build_number = sys.env("BUILD_NUMBER")
jenkins_job_name = sys.env("JOB_NAME")

with open(psnr_output_file_path, "r") as f:
    line = f.readline()

psnr = float(line)

print("got psnr value %f for jenkins job %s, build number %s\n", % (psnr, jenkins_job_name, jenkins_build_number))

jsonData = {
    "buildNum": jenkins_build_number,
    "psnrValue": psnr
}

r = request.post(dashboard_service_url, json=jsonData)
if r.status_code != requests.codes.ok:
    print("Error pushing psnr data to dashboard: %s" % r.status_code)
    sys.exit(1)
