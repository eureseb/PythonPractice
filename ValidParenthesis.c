#include <stdbool.h>

bool validParentheses(const char *str_in) {

    //  <----  hajime!
    int i = 0;
    bool flag = false;
    int open = 0;
    int close = 0;
    while(str_in[i] != '\0'){
      if(str_in[i] == '(')
        open++;
      if(str_in[i] == ')')
        if(open > 0)
          open--;          
        else
          return false;
      i++;
    }
    if(open == 0)
      return true;
    return false;

}