#include <iostream>
#include "curl/curl.h"
#include "curl/easy.h"

using namespace std;

int main() {

    string uri = "https://msesandbox.cisco.com/api/contextaware/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone";
    string header_authorization = "Authorization: Basic bGVhcm5pbmc6bGVhcm5pbmc=";
    string header_accept = "Accept: application/json";

    struct curl_slist *headers = NULL;
    headers = curl_slist_append(headers, header_authorization.c_str());
    headers = curl_slist_append(headers, header_accept.c_str());

    CURLcode res;
    CURL *curl = curl_easy_init();
    if(curl) {

        curl_easy_setopt(curl, CURLOPT_URL, uri.c_str());
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        res = curl_easy_perform(curl);

        if(res != CURLE_OK)
            cerr << "ERROR: " << curl_easy_strerror(res) << endl;
        else {
            // We should have received data from the URI
        }

        curl_easy_cleanup(curl);
    }

    return 0;
}