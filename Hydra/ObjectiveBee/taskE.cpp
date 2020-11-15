#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

string n, str;
int len, mass = 0;

string ans = "0 ";

void read_input(void)
{
  ifstream fin("input.txt");

  getline(fin, n);
  getline(fin, str);

  len = stoi(n);
}

vector<int> split(string str)
{
  vector<int> result;
  istringstream iss(str);
  for (string str; iss >> str;)
    result.push_back(stoi(str));

  return result;
}

int main(void)
{
  int operations = 0;
  bool not_sorted = true;
  string temp;
  int temp_int;

  read_input();
  vector<int> ord = split(str);
  vector<int> temp_ord;

  temp_ord = vector<int>(ord.begin(), ord.begin() + 2);


  for (int i = 0; i < temp_ord.size(); i++)
    cout << temp_ord[i] << ' ';




  /*
  for (int i = 1; i < len; i++) {
    temp_ord =
    operations = 0;
    not_sorted = true;
    while (not_sorted) {
      for (int j = 0; j < (temp_ord.size() - 1); j++) {
        if (temp_ord[i] > temp_ord[j+1]) {
          temp = temp_ord[j+1];
          temp_ord[j+1] = temp_ord[j];
          temp_ord[j] = temp;
          mass += temp_ord[j+1];

          temp_int = ord[j+1];
          ord[j+1] = ord[j];
          ord[j] = temp_int;
        }
        else if (j == (temp_ord.size() - 2))
          not_sorted = false;
        else
          continue;
      }
      ans.append(to_string(mass) + " ");
    }
  }*/
  return 0;
}
