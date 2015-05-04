// Include the headers needed for the input/output, cURL, and RapidJSON functionality
#include <iostream>
#include <fstream>
#include "curl/curl.h"
#include "curl/easy.h"
#include "rapidjson/document.h"
#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"

// Declare the namespaces we intend to use
using namespace std;
using namespace rapidjson;

// Define a structure to hold our file and string information for the callback data
struct JSONDATA
{
    fstream *file;
    string *str;
};

// The callback function used by cURL to write our file
size_t write_data(void *ptr, size_t size, size_t nmemb, JSONDATA *data) {

	size_t numBytes = size * nmemb;

    if (data->file)
        data->file->write((char*)ptr, numBytes);

    if (data->str)
        *(data->str) += std::string((char*)ptr, numBytes);
    
    return numBytes;
}

// The main function of the application
int main() {

    CURL *curl;
    CURLcode res;

    // The URI we intend to access
    string uri = "https://msesandbox.cisco.com/api/contextaware/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone";

    // The Authorization header with learning:learning base64 encoded for the user:password
    string header_authorization = "Authorization: Basic bGVhcm5pbmc6bGVhcm5pbmc=";

    // The Accept header specifying we would like JSON data returned to us from the server
    string header_accept = "Accept: application/json";

    // Add the headers to a list for cURL to use
    struct curl_slist *headers = NULL;
    headers = curl_slist_append(headers, header_authorization.c_str());
    headers = curl_slist_append(headers, header_accept.c_str());

    // Initialize cURL
    curl = curl_easy_init();

    // Declare a file called content.json
	fstream file("content.json", ios_base::out | ios_base::ate);

    // A string to store our json output
    string json;

    // An instance of our JSONDATA structure
    JSONDATA data;
	data.file = &file;
    data.str = &json;

    // If we have a valid cURL instance we can proceed
    if (curl) {

        // Set the cURL options for the URI, headers, the callback function, and callback data
        curl_easy_setopt(curl, CURLOPT_URL, uri.c_str());
		curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
		curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
		curl_easy_setopt(curl, CURLOPT_WRITEDATA, &data);

        // Actually have cURL perform the request
        res = curl_easy_perform(curl);

        // Check to see if we received an OK from cURL
        if(res != CURLE_OK)
        	cerr << "ERROR: " << curl_easy_strerror(res) << endl;
        else {

            // Create a RapidJSON document and parse the received JSON into it
        	Document document;
            document.Parse(json.c_str());

            // Get the Floor\AccessPoint value from the JSON
            Value& accessPoint = document["Floor"]["AccessPoint"];

            // Check to verify we got an array of access point values in the JSON
            assert(accessPoint.IsArray());

            // Iterate through the Access Points, printing their name
	        for (SizeType i = 0; i < accessPoint.Size(); i++) 
    		    printf("accessPoint: %s\n", accessPoint[i]["name"].GetString());
        }

        // Cleanup the cURL instance
        curl_easy_cleanup(curl);
    }

    // Return a success value from our application
    return 0;
}