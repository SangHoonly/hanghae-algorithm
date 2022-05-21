#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void printPassword(vector<char> &password)
{
  for (auto item : password)
    cout << item;
  cout << '\n';
}

bool isRightPassword(vector<char> &password)
{
  int cnt = 0;

  for (auto item : password)
    if (item == 'a' || item == 'e' || item == 'u' || item == 'i' || item == 'o')
      cnt++;

  return (cnt && (password.size() - cnt) >= 2) ? true : false;
}

void possiblePassword(int L, int C, char *words, vector<char> &passwords)
{
  if (!L)
  {
    if (isRightPassword(passwords))
      printPassword(passwords);
  }

  for (int i = 0; C > i; i++)
  {
    if (!passwords.empty() && passwords.back() >= words[i])
      continue;
    passwords.push_back(words[i]);
    possiblePassword(L - 1, C - 1, words + 1, passwords);
    passwords.pop_back();
  }
}

int main(void)
{
  int L, C;
  vector<char> passwords;

  cin >> L >> C;

  char words[C];

  for (int i = 0; C > i; i++)
    cin >> words[i];

  sort(words, words + C);

  possiblePassword(L, C, words, passwords);

  return 0;
}
