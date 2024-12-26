*** Settings ***
Library       	SeleniumLibrary
Library       	DjangoLibrary

*** Variables ***
${SERVER_URL} 	http://localhost:8000
${TITLE}		The Plague
${ISBN}		    9780679720218 

*** Test Cases ***
Test Search Function
	[Documentation]   Verify that user can navigate from home page to catalog and that the search function works and brings up relevant results.
	Open Browser  	${SERVER_URL}	Chrome
	Maximize Browser Window                 # Catalog link may be obscured if window is not large enough
	Wait Until Element Is Visible	id:navbarNav   3
	Click Link    	Catalog
	Wait Until Element Is Visible	name:search	3
	Input Text    	name:search	${TITLE} 	# Search for book titled '${TITLE}'
	Press Keys    	name:search	ENTER
	Page Should Contain	${ISBN}        		# Verify that book with ISBN corresponding to title has been brought up
	[Teardown]	Close Browser



