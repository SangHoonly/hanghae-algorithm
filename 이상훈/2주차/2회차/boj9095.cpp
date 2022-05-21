#include <iostream>

using namespace std;

int recursion(int n)
{
  if (n == 1 || n == 0)
    return 1; // 기저 사례

  int count = 0;

  for (int i = 1; 4 > i; i++)
    if (n - i >= 0)
      count += recursion(n - i);
  return count;
}

int main(void)
{
  int N, n;

  cin >> N;

  while (N--)
  {
    cin >> n;
    cout << recursion(n) << '\n';
  }

  return 0;
}
