#include "my_math.h"
#include <stdio.h>

void max_min(int x, int y)
{
  int mx,mn;
  if(x>y)
  {
    mx=x;
    mn=y;
  }
  else
  {
    mx=y;
    mn=x;
  }

  printf("%d %d",mx,mn);
}