#include <iostream>
#include "curl/curl.h"
#include "curl/easy.h"

using namespace std;

int main() {

    string uri = "http://www.cisco.com";

    CURLcode res;
    CURL *curl = curl_easy_init();
    if(curl) {

        curl_easy_setopt(curl, CURLOPT_URL, uri.c_str());
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