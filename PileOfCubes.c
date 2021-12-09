#include <stdio.h>
long long findNb(long long m)
{
  int long long ans = 0;
  int i = 1;
  while(ans < m){
    ans += pow(i++, 3);
  }
  
  if(ans == m) return i-1;
  else return -1;
}