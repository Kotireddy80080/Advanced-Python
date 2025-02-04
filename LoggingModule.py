print("Example-1")
import time 
import logging 
logging.basicConfig(filename="ihub_k.txt",level=logging.DEBUG)
print("----Welcome to Logging Module----")
logging.debug("Debug Information")
logging.warning("Warning Information")
logging.info("Infor Information")
logging.error("Error Information")
logging.critical("Critical Information")
print()
time.sleep(2)
print("End of an application")

print("Example-2")
import time 
import logging 
logging.basicConfig(filename="ihub_k.txt",level=logging.DEBUG,filemode="w")
print("----Welcome to Logging Module----")
logging.debug("Debug Information")
logging.warning("Warning Information")
logging.info("Infor Information")
logging.error("Error Information")
logging.critical("Critical Information")
print()
time.sleep(2)
print("End of an application")

print("Example-3")
import time 
import logging 
logging.basicConfig(filename="ihub_1.txt",level=10,filemode="w")
print("----Welcome to Logging Module----")
logging.debug("Debug Information")
logging.warning("Warning Information")
logging.info("Infor Information")
logging.error("Error Information")
logging.critical("Critical Information")
print()
time.sleep(2)
print("End of an application")


print("Example-4")
import time 
import logging 
logging.basicConfig(filename="ihub_1.txt",filemode="w")
print("----Welcome to Logging Module----")
logging.debug("Debug Information")
logging.warning("Warning Information")
logging.info("Infor Information")
logging.error("Error Information")
logging.critical("Critical Information")
print()
time.sleep(2)
print("End of an application")

print("Example-5")
import time 
import logging 
logging.basicConfig(filename="ihub_1.txt",level=logging.CRITICAL,filemode="w")
print("----Welcome to Logging Module----")
logging.debug("Debug Information")
logging.warning("Warning Information")
logging.info("Infor Information")
logging.error("Error Information")
logging.critical("Critical Information")
print()
time.sleep(2)
print("End of an application")


print("Example-6")
import time 
import logging 
logging.basicConfig(format="%(levelname)s",level=logging.DEBUG)
print("----Welcome to Logging Module----")
logging.debug("Debug Information")
logging.warning("Warning Information")
logging.info("Infor Information")
logging.error("Error Information")
logging.critical("Critical Information")
print()
time.sleep(2)
print("End of an application")

print("Example-7")
import time 
import logging 
logging.basicConfig(format="%(message)s",level=logging.DEBUG)
print("----Welcome to Logging Module----")
logging.debug("Debug Information")
logging.warning("Warning Information")
logging.info("Infor Information")
logging.error("Error Information")
logging.critical("Critical Information")
print()
time.sleep(2)
print("End of an application")
