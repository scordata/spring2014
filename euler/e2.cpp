#include <iostream>
using namespace std;


static unsigned long mem[4000000] = {0}; 

unsigned long fib(unsigned long n){
  if ( mem[n] != 0 ) {
    return mem[n];
  } 
  if ( n < 2 ){
    mem[n] = 1;
  } else 
    mem[n] = fib(n-1) + fib(n-2);
  return mem[n];
}

unsigned long sum(){
  unsigned long r = 0;
  for ( int i = 0; i < 4000000; i++ ){
    if ( mem[i] > 4000000 )
      break;
    if ( mem[i] % 2 == 0  )
      r += mem[i];
  }
  return r;

}

int main(){
  unsigned long x = fib(10000);
  cout << x << endl;
  cout << sum() << endl;

return 0;
}
