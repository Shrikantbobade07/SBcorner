def log_execution(funct):
    def wrraper():
        print("Start exection data Pipline.....")
        funct()
        print("end execution data pipline....")
    return wrraper

@log_execution
def run_pipline():
    print("loding pipline ......")

run_pipline()