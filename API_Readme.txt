#***************************************
#Project Information
#**************************************

Project Name: FaceFirst Automation
Technology Stack: Python (3.11v), PyTest, PyCharm
Framework Type: Hybrid-framwork


#********************
#Hybrid Framework Information
#********************
1) Script Development & Folder Structure:
	A) All_API_Methods_Package: In this folder, we define all the requests and create separate functions for each test case. All module folders are created separately.
	B) All_API_Test_Cases_Package: In this folder, we defined all test cases, and each module is separated by folder.
	C) Application Logs: In this folder, all logs were stored.
	D) Config_Package: In this folder, two packages are present: Excel config files in this package's xlutils file are defined, and ini config files in that package's read function are 	created for reading the ini file.
	E) Reports: In this folder, different reports will be generated in Excel and HTML. A screenshot of failed test cases will also be saved.
	F) Test Data: In this folder, all data-related packages are present. For data-driven test cases, Excel and a CSV file are used. In the data from the INI file, all locators are 	mentioned; create a separate file for each page.

2) Test Execution:
	1) Run in IDE: Run test cases with specific class-specific module test cases.
	2) Run-through Markers: We separate test cases into p1, p2, p3, p4, and p5. If we want to run only p1 test cases, then the below command is used:
	(in console): >> pytest -v -s -m "p1"
	3) Please also find the last execution status under <<Result.html>>


3) Last Automation Package Contains Following:



3.1: Module Level Information

**************************************

1)Login Module :
		
		
		
2) User Module : 
	