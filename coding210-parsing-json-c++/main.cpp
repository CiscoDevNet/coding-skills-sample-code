#include <iostream>
#include <fstream>
#include "curl/curl.h"
#include "curl/easy.h"
#include "rapidjson/document.h"
#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"

using namespace std;
using namespace rapidjson;

struct JSONDATA
{
    fstream *file;
    string *str;
};

size_t write_data(void *ptr, size_t size, size_t nmemb, JSONDATA *data) {

    size_t numBytes = size * nmemb;

    if (data->file)
        data->file->write((char*)ptr, numBytes);

    if (data->str)
        *(data->str) += std::string((char*)ptr, numBytes);

    return numBytes;
}

int main() {

    CURL *curl;
    CURLcode res;

    string uri = "https://msesandbox.cisco.com/api/contextaware/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone";
    string header_authorization = "Authorization: Basic bGVhcm5pbmc6bGVhcm5pbmc=";
    string header_accept = "Accept: application/json";

    struct curl_slist *headers = NULL;
    headers = curl_slist_append(headers, header_authorization.c_str());
    headers = curl_slist_append(headers, header_accept.c_str());

    curl = curl_easy_init();

    fstream file("content.json", ios_base::out | ios_base::ate);
    string json;

    JSONDATA data;
    data.file = &file;
    data.str = &json;

    if(curl) {

        curl_easy_setopt(curl, CURLOPT_URL, uri.c_str());
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &data);

        res = curl_easy_perform(curl);

        if(res != CURLE_OK)
            cerr << "ERROR: " << curl_easy_strerror(res) << endl;
        else {

            Document document;
            document.Parse(json.c_str());

            Value& accessPoint = document["Floor"]["AccessPoint"];
            assert(accessPoint.IsArray());

            // Iterate through the Access Points
            for (SizeType i = 0; i < accessPoint.Size(); i++)
                printf("accessPoint: %s\n", accessPoint[i]["name"].GetString());
        }

        curl_easy_cleanup(curl);
    }

    return 0;
}