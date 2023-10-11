#include <cstring>
#include <iostream>
#include <regex>
#include <string>
#include <vector>

std::string trim(const std::string &str);

using namespace std;

int main() {

  string remix;
  getline(cin, remix);
  string det = "WUB";
  while (remix.find("WUB") != string::npos) {
    remix.replace(remix.find("WUB"), 3, " ");
  }

  while (remix.find("  ") != string::npos) {
    remix.replace(remix.find("  "), 2, " ");
  }

  cout << trim(remix.c_str()) << endl;
  return 0;
}

std::string trim(const std::string &str) {
  size_t first = str.find_first_not_of(" \t\n\r");
  size_t last = str.find_last_not_of(" \t\n\r");

  if (first == std::string::npos) {
    return "";
  }

  return str.substr(first, last - first + 1);
}